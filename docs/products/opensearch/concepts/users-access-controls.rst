Understanding access control in Aiven for OpenSearch®
=====================================================

Implementing access control and permissions is essential in maintaining secure access to data stored in Aiven for OpenSearch®. This article provides an overview of how access control works in Aivne for OpenSearch®, including the different types of permissions that can be used to control access.

Patterns and permissions
-------------------------

Access control in OpenSearch is achieved through the use of patterns and permissions. A pattern is a string in glob-style that specifies the indices to which the permission applies, while the permission defines the level of access granted to the user for the matching indices.

Patterns
``````````
Patterns are glob-style strings that use the following syntax:

* ``*``: Matches any number of characters (including none)
*  ``?``: Matches any single character

Permissions
````````````
The permissions available in Aiven for OpenSearch®, ordered by importance, are:

* ``deny``: Explicitly denies access
* ``admin``: Allows unlimited access to the index
* ``readwrite``: Grants full access to documents
* ``read``: Allows only searching and retrieving documents
* ``write``: Allows updating, adding, and deleting documents


API access
```````````
The permission also determines which index APIs the user can access:

* ``deny``: No access
* ``admin``: No restrictions
* ``readwrite``: Allows access to ``_search``, ``_mget``, ``_bulk``, ``_mapping``, ``_update_by_query``, and ``_delete_by_query`` APIs
* ``read``: Allows access to ``_search`` and ``_mget`` APIs
* ``write``: Allows access to ``_bulk``, ``_mapping``, ``_update_by_query``, and ``_delete_by_query`` APIs

.. note:: 
    * When no rules match, access is implicitly denied.
    * The ``write`` permission allows creating indices that match the rule's index pattern but does not allow deleting them. Indices can only be deleted when a matching ``admin`` permission rule exists.


Example
--------
As an example, consider the following set of rules:

* ``logs_*/read``
* ``events_*/write``
* ``logs_2018*/deny``
* ``logs_201901*/read``
* ``logs_2019*/admin``

This set of rules would allow the service user to:

* Add documents to ``events_2018`` (second rule)
* Retrieve and search documents from ``logs_20171230`` (first rule)
* Gain full access to ``logs_20190201`` (fifth rule)
* Gain full access to ``logs_20190115`` (fifth rule, as the ``admin`` permission gets higher priority than the ``read`` permission in the fourth rule)

This same set of rules would deny the service user from:

* Gain any access to ``messages_2019`` (no matching rules)
* Read or search documents from ``events_2018`` (the second rule only grants ``write`` permission)
* Write to or use the API ``for logs_20171230`` (the first rule only grants ``read`` permission)

Access control for aliases 
---------------------------
Access control and aliases are key concepts in OpenSearch. Aliases are virtual indices that can reference one or more physical indices, simplifying the management and search of data. You can define access control rules for aliases to ensure proper security and control over data access.

When working with aliases in OpenSearch, it's essential to remember how access control rules apply to them: 

* Aliases are not automatically expanded in access control. Therefore, the ACL must explicitly include a rule that matches the alias pattern.
* Only access control rules that match the alias pattern will be applied, while rules that match the physical indices the alias expands to will not be used.


Access to top-level APIs
-------------------------

You can control access to "top-level" APIs in addition to indices using ACLs. This can be achieved by creating an API-specific rule to manage access to these APIs.

Service controlled APIs
````````````````````````
The following top-level APIs are controlled by the OpenSearch service and not by the ACLs defined by you:
* ``_cluster``
* ``_cat``
* ``_tasks``
* ``_scripts``
* ``_snapshot``
* ``_nodes``

.. note:: 
    Enabling OpenSearch Security management provides control over the top-level APIs - ``_mget``, ``_msearch``, and ``_bulk``.


Using ACLs to control access
`````````````````````````````
Only rules starting with ``_ ``are considered for controlling access to top-level APIs, and normal index rules do not grant access to these APIs. For example, a rule like ``*search/admin`` only grants access to indices that match the pattern, not to ``_msearch``.

Example: 

* ``_*/admin`` grants unlimited access to all top-level APIs
* ``_msearch/admin`` grants unlimited access to the ``_msearch`` API only

ACLs **only control access to the API** and not its usage. Granting access to the top-level API will effectively bypass index-specific rules. For example, granting ``_msearch/admin`` access allows searching any index via the API as the indices to search are defined in the request body itself.

.. warning:: 
    When granting top-level API access via an explicit ACL, the requested content is not examined.


Access control and OpenSearch Dashboards 
-----------------------------------------

Enabling ACLs does not restrict access to OpenSearch Dashboards. However, all requests made by OpenSearch Dashboards are checked against the current user's ACLs.

.. note:: 
    You might encounter ``HTTP 500`` internal server errors when you try to view dashboards as a service user with read-only access to certain indices, as these dashboards call the ``_msearch`` API. o prevent this, add a new ACL rule that grants ``admin`` access to ``_msearch`` for that service user.


Next steps
----------
Learn how to :doc: `enable and manage access control <../howto/control_access_to_content>` for your Aiven for OpenSearch® service. 