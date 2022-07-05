``avn service schema-registry-acl``
============================================

Here you’ll find the full list of commands for ``avn service schema-registry-acl``.


Manage Apache Kafka® Karapace schema registry access control lists
------------------------------------------------------------------

Commands for managing :doc:`Aiven for Apache Kafka® Karapace schema registry authorization </docs/products/kafka/concepts/schema-registry-authorization>` via ``avn`` commands.

``avn service schema-registry-acl-add``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Adds an Aiven for Apache Kafka® Karapace schema registry ACL entry. The detailed explanation of parameters can be found in the :ref:`dedicated page <karapace_schema_registry_acls>`.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``--permission``
    - The permission type: possible values are ``schema_registry_read`` or ``schema_registry_write``
  * - ``--resource``
    - The resource to grant access to, can be in the form of ``Config:`` or ``Subject:<subject>``, accepts * and ? as wildcard characters accepts ``*`` and ``?`` as wildcard characters. More information can be found in the :ref:`dedicated page <karapace_schema_registry_acls>`.
  * - ``--username``
    - The username pattern: accepts ``*`` and ``?`` as wildcard characters

**Example:** Add an ACLs for users with username starting with ``userAB`` to write (``schema_registry_write``) subjects having name starting with ``s123`` in the service ``kafka-doc``.

::

  avn service schema-registry-acl-add kafka-doc \
    --username 'userAB*'                        \
    --permission schema_registry_write          \
    --resource 'Subject:s123*'



``avn service schema-registry-acl-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Deletes an Aiven for Apache Kafka® Karapace schema registry ACL entry.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``acl_id``
    - The id of the Karapace schema registry ACL to delete


**Example:** Delete the Karapace schema registry ACLs with id ``acl3604f96c74a`` on the Aiven for Apache Kafka instance named ``kafka-doc``.

::

  avn service schema-registry-acl-delete kafka-doc acl3604f96c74a

``avn service schema-registry-acl-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists Aiven for Apache Kafka® Karapace schema registry ACL entries.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** List the ACLs defined for a service named ``kafka-doc``.

::

  avn service schema-registry-acl-list kafka-doc


The command output is:

.. code:: text

    ID                        USERNAME  RESOURCE         PERMISSION
    ========================  ========  ===============  =====================
    default-sr-admin-config   avnadmin  Config:          schema_registry_write
    default-sr-admin-subject  avnadmin  Subject:*        schema_registry_write
    acl12345678901            userAB*   Subject:s123*    schema_registry_write
