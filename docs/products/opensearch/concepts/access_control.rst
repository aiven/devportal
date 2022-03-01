Access control
==============

Aiven for OpenSearch® supports index-level access control lists (ACL) to control permissions. This approach allows you to limit the operations that are available to specific connections and to restrict access to certain data sets, which improves the security of your data.

You can grant the following permissions:

* ``deny``: no access
* ``admin``: full access to APIs and documents 
* ``readwrite``: full access to documents
* ``read``: allow only searching and retrieving documents
* ``write``: allow updating, adding, and deleting documents

  .. note::
     Write permission allows the service user to create new indexes that match the pattern, but it does not allow deletion of those indexes.


Rules are defined separately for each user as ``pattern/permission`` combinations. The ``pattern`` defines the indexes that the permission applies to. Patterns are glob-style, where ``*`` matches any number of characters and ``?`` matches any character. 

When multiple rules match, they are applied in the order listed above. If no rules match, access is denied.

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

The permission also implies which index APIs the service user can access:

* ``read``:  ``_search``, ``_mget``
* ``write``: ``_bulk``, ``_mapping``, ``_update_by_query``, ``_delete_by_query``
* ``admin``: no restrictions 

  

Controlling access to top-level APIs
------------------------------------

OpenSearch has several "top-level" API endpoints (``_mget``, ``_msearch``, and so on), where you have to grant access separately. To do this, use patterns similar to the index patterns, for example:

* ``_*/admin`` would grant unlimited access to all top-level APIs
* ``_msearch/admin`` grants unlimited access to the ``_msearch`` API only

.. note::
   You might encounter ``HTTP 500`` internal server errors when you try to view dashboards as a service user that has read-only access to certain indexes, as these dashboards call the ``_msearch`` API. In such cases, add a new ACL rule that grants **Admin** access to ``_msearch`` for that service user.

Only rules where the pattern starts with ``_`` are considered for top-level API access. Normal rules do not grant access to these APIs. For example, ``*search/admin`` only grants access to indexes that match the pattern, not to ``_msearch``.

You can switch on the ``ExtendedAcl`` option for the service to enforce index rules in a limited fashion for requests that use the ``_mget``, ``_msearch``, and ``_bulk`` APIs (and only those). When this option is in use, service users can access these APIs as long as all operations only target indexes that they have appropriate permissions for. 

.. note::
   To enforce the rules with ``ExtendedACL``, the service must inspect the content of the request, which can cause performance and latency issues. All requests are also limited to a maximum of 16 KiB in size. If the request is too large or if any of the operations or indexes are not allowed, the entire request is rejected.


Access control and aliases
--------------------------

Aliases are not expanded. If you use aliases, the ACL must include a rule that matches the alias. 


Access control and OpenSearch Dashboards
----------------------------------------

Enabling ACLs does not restrict access to OpenSearch Dashboards itself, but all requests done by OpenSearch Dashboards are checked against the current user's ACLs. 

In practice, for OpenSearch Dashboards to function properly, you must grant the user admin-level access to the ``_msearch`` interface (permission: ``admin``, pattern: ``_msearch``) or switch on the ``ExtendedAcl`` option.

