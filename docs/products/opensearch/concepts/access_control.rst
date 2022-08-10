Access control
==============

Aiven for OpenSearch® supports index-level access control lists (ACL) to control permissions.
This approach allows you to limit the operations that are available to specific service users and
restrict access to certain data sets.

.. note::
   When access control is initially enabled for the service, a set of rules that allows
   full unlimited access to existing service users is created automatically.

Rules are defined separately for each user as ``pattern/permission`` combinations. The ``pattern`` defines the indices that the permission applies to.
Patterns are glob-style, where ``*`` matches any number of characters (including none) and ``?`` matches any character.

You can grant the following permissions:

* ``deny``: explicitly deny access
* ``admin``: unlimited access to the index
* ``readwrite``: full access to documents
* ``read``: allow only searching and retrieving documents
* ``write``: allow updating, adding, and deleting documents

The permission also implies which *index APIs* the service user can access:

* ``deny``: no access
* ``admin``: no restrictions
* ``readwrite``: ``_search``, ``_mget``, ``_bulk``, ``_mapping``, ``_update_by_query``, ``_delete_by_query``
* ``read``: ``_search``, ``_mget``
* ``write``: ``_bulk``, ``_mapping``, ``_update_by_query``, ``_delete_by_query``

.. note::
   When no rules match, access is **implicitly denied**.

.. note::
   ``write`` permission allows creating indices that match the rule's index pattern but does now allow deleting them.
   Indices can only be deleted when a matching ``admin`` permission rule exists.

When multiple rules match, they are applied in the order listed above regardless of the rule order (see the example below).

Example
-------

As an example, we can use the following set of rules:

* ``logs_*/read``
* ``events_*/write``
* ``logs_2018*/deny``
* ``logs_201901*/read``
* ``logs_2019*/admin``

This set would allow the service user to

* add documents to ``events_2018`` (second rule),
* retrieve and search documents from ``logs_20171230`` (first rule),
* gain full access to ``logs_20190201`` (fifth rule), and
* gain full access to ``logs_20190115`` (fifth rule, as the ``admin`` permission gets higher priority than the ``read`` permission in the fourth rule.

The same set would deny the service user to

* gain any access to ``messages_2019`` (no matching rules),
* read or search documents from ``events_2018`` (the second rule only grants ``write`` permission), and
* write to or use the API for ``logs_20171230`` (the first rule only grants ``read`` permission).

Controlling access to top-level APIs
------------------------------------

In addition to indices, ACLs can be used to control access to "top-level" APIs by creating a API specific rule.

.. note::
   Access to the ``_cluster``, ``_cat``, ``_tasks``, ``_scripts``, ``_snapshot``, and ``_nodes`` APIs is controlled
   by the service itself, not by these ACLs.

.. note::
    Access to the top-level ``_mget``, ``_msearch``, and ``_bulk`` APIs can also be controlled by enabling ``ExtendedACL``.

Using ACLs to control access
++++++++++++++++++++++++++++

Only rules where the pattern starts with ``_`` are considered for top-level API access.
Normal index rules do not grant access to these APIs. For example, ``*search/admin`` only grants access to indices that match the pattern, not to ``_msearch``.

Examples
::::::::

* ``_*/admin`` would grant unlimited access to all top-level APIs
* ``_msearch/admin`` grants unlimited access to the ``_msearch`` API only

The ACL **only controls access to the API** and not what it can be used for. Giving access to the top-level API will in effect circumvent index specific rules, for example ``_msearch/admin`` access
allows searching any index via the API as the indices to search are defined in the request body itself.

.. note::
   When top-level API access is granted via explicit ACL the request content is not examined.

Enabling extended ACLs
++++++++++++++++++++++

Instead of creating a rule that allows access to the top-level ``_mget``, ``_msearch`` and ``_bulk`` APIs, you can switch on the ``ExtendedAcl``.
This will automatically enable these APIs for the user and each API request is checked to make sure operations only target indices
that the user has appropriate permissions for (as defined by the normal index ACLs).

As the service must inspect the content of the request, this *can cause* performance and latency issues. The requests are also **limited to a maximum of 15000 bytes** in size.
If the request is **too large** or if **any** of the operations or indices are not allowed by the ACLs, the *entire request* is rejected.

.. note::
   ACLs permitting access to top-level API will always take precedence over ``ExtendedACL``, you can for example allow access to ``_bulk`` for a trusted service account to
   do mass updates.


Access control and aliases
--------------------------

Aliases are **not expanded**. If you use aliases, the ACL must include a rule where the pattern matches the alias.

.. note::
   Rules matching the indices the alias "expands" to are not used, only the rule where the pattern matches the alias itself.


Access control and OpenSearch Dashboards
----------------------------------------

Enabling ACLs does not restrict access to OpenSearch Dashboards itself, but all requests done by OpenSearch Dashboards are checked against the current user's ACLs.

.. note::
   You might encounter ``HTTP 500`` internal server errors when you try to view dashboards as a service user that has read-only access to certain indices, as these dashboards call the ``_msearch`` API.
   In such cases, add a new ACL rule that grants **Admin** access to ``_msearch`` for that service user.
