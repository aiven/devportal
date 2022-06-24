Manage users and access control lists
=======================================

Aiven for Apache Kafka® uses access control lists (ACL) and user definitions in order to establish individual rights to produce or consume a topic.
More information about permissions mapping can be found in the :doc:`dedicated documentation <../concepts/acl>`. 

You can manage users and ACL entries in the corresponding tabs of the service page in the `Aiven web console <https://console.aiven.io/>`_.

Add a user
----------

.. Warning:: 

    A user with the ``Admin`` permission can create topics with any name, as the ``CreateTopics`` permission is applied at the cluster level. 
    
    All other permissions related to a topic (``Alter``, ``Delete``) **only** apply to the topics matching the pattern that you specify.

You can add a new user via the `Aiven console <https://console.aiven.io/>`_ with:

#. Log in to the Aiven web console and select your service.

#. Click the **Users** tab.

#. Enter a name for the new user and then click **Add service user**.

#. The new user appears on the *Users* page, with links to the user-specific access key and certificate.

Add a new ACL grant
-------------------

You can add a new access control list grant via the `Aiven console <https://console.aiven.io/>`_ with:

1. Click the **ACL** tab.

2. Enter the username and topic that the grant applies to.

3. Select the **Permission** that you want to apply.
   
   Details of each available option are described in the :doc:`permission mapping documentation <../concepts/acl>`

4. Click **Add ACL entry**.

.. Tip:: 
    
    When using the :doc:`Aiven Terraform Provider </docs/tools/terraform/terraform>`, you can add the ``default_acl`` key to your ``resource`` and set it to ``false`` if you do not want to create the admin user with wildcard permissions.

5. Once you start defining custom ACLs, it's recommended to delete the default ``avnadmin`` rule by clicking the **Remove** icon. 

.. Warning:: 

    ACL restrictions currently do not apply to Kafka REST. Rules are applied based on the username and topic names, but there are no restrictions on consumer group names.

    We are working on extending the same restrictions to Kafka REST.
