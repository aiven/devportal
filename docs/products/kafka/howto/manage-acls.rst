Manage users and access control lists
=======================================
Aiven for Apache Kafka® uses access control lists (ACL) and user definitions to grant specific rights for producing or consuming topics. For detailed information on permission mapping, see  :doc:`Access control lists and permission mapping <../concepts/acl>` section. 

To manage users and ACL entries, access the corresponding sections in the left sidebar of the service page within the `Aiven Console <https://console.aiven.io/>`_. 

Add a user
----------

.. Warning:: 

    A user with the ``Admin`` permission can create topics with any name, as the ``CreateTopics`` permission is applied at the cluster level. 
    
    All other permissions related to a topic (``Alter``, ``Delete``) **only** apply to the topics matching the pattern that you specify.

To add a new user, follow these steps: 

#. Log in to `Aiven Console <https://console.aiven.io/>`_ and select your service.

#. Select **Users** from the left sidebar.

#. Enter a name for the new user and then select **Add service user**.

#. The new user appears on the *Users* page, with links to the user-specific access key and certificate.


Add a new ACL grant
-------------------

To add new access control list, follow these steps: 

You can add a new access control list grant via the `Aiven Console <https://console.aiven.io/>`_ with:

#. Log in to `Aiven Console <https://console.aiven.io/>`_ and select your service.

#. Select **ACL** from the left sidebar and select **Add entry**. 
#. On the **Add access control entry** screen, select the desired ACL type:

   a. For **ACL for Topics**, enter the following details:
    
      * Username
      * Topic
      * Permissions

   b. For ACL for Schema Registry, enter the following details:
    
      * Username
      * Resources
      * Permissions

   Refer to the :doc:`Access control lists and permission mapping </docs/products/kafka/concepts/acl>` section for more information.

#. Click **Add ACL entry**.

   .. Tip:: 
    
      When using the :doc:`Aiven Terraform Provider </docs/tools/terraform>`, you can add the ``default_acl`` key to your ``resource`` and set it to ``false`` if you do not want to create the admin user with wildcard permissions.

#. Once you start defining custom ACLs, it's recommended to delete the default ``avnadmin`` rule by clicking the **Remove** icon. 

   .. Warning:: 

      ACL restrictions currently do not apply to Kafka REST. Rules are applied based on the username and topic names, but there are no restrictions on consumer group names.

      We are working on extending the same restrictions to Kafka REST.
