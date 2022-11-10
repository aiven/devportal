``avn service schema-registry-acl``
============================================

Here you’ll find the full list of commands for ``avn service schema-registry-acl``.


Manage Karapace schema registry access control lists for Apache Kafka®
----------------------------------------------------------------------

Using the following commands you can manage :doc:`Karapace schema registry authorization </docs/products/kafka/karapace/concepts/schema-registry-authorization>` for your Aiven for Apache Kafka® service via the ``avn`` commands.


``avn service schema-registry-acl-add``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
You can add a Karapace schema registry ACL entry by using the command::

  avn service schema-registry-acl-add

Where:

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``--permission``
    - The permission type: 
  
      - ``schema_registry_read``
      -  ``schema_registry_write``
  * - ``--resource``
    - The resource format can be ``Config:`` or ``Subject:<subject>``. For more information, see :doc:`ACLs definition <karapace_schema_registry_acls>`.
  * - ``--username``
    - The name of a service user

**Example**

The following example shows you how to add an ACL entry to grant a user (``user_1``) read options (``schema_registry_read``) to subject ``s1``. Replace the placeholders ``PROJECT_NAME`` and ``APACHE_KAFKA_SERVICE_NAME`` with the name of the project and the Aiven for Apache Kafka® service.

::

  avn service schema-registry-acl-add kafka-doc \
    --username 'user_1'                        \
    --permission schema_registry_read          \
    --resource 'Subject:s1'

.. Note:: 
  You cannot edit a Karapace schema registry ACL entry. You need to create a new entry and delete the older entry. 

``avn service schema-registry-acl-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
You can delete a Karapace schema registry ACL entry using the command::

  avn service schema-registry-acl-delete

Where: 

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``acl_id``
    - The ID of the Karapace schema registry ACL to delete

**Example**
The following example deletes the Karapace schema registry ACL with ID ``acl3604f96c74a`` on the Aiven for Apache Kafka® instance named ``kafka-doc``.
::

  avn service schema-registry-acl-delete kafka-doc acl3604f96c74a

``avn service schema-registry-acl-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
You can view a list of all Karapace schema registry ACL entries defined using the command::

  avn service schema-registry-acl-list

Where: 

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** 
The following example lists the ACLs defined for an Aiven for Apache Kafka® service named ``kafka-doc``.

::

  avn service schema-registry-acl-list kafka-doc


The command output is:

.. code:: text

    ID                        USERNAME  RESOURCE         PERMISSION
    ========================  ========  ===============  =====================
    default-sr-admin-config   avnadmin  Config:          schema_registry_write
    default-sr-admin-subject  avnadmin  Subject:*        schema_registry_write
    acl12345678901            userAB*   Subject:s123*    schema_registry_write
