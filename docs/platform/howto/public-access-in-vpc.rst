Enable public access in a VPC
==============================

To enable public access for a service which is running within a virtual private cloud (VPC), follow these steps:

#. Log in to the Aiven web console and select your service.
#. On the *Overview* page, scroll down to the *Advanced configuration* section and click **Add configuration option**.
#. Select an option which starts with ``public_access.`` and follows with the type of service you use and switch it on.
#. Click **Save advanced configuration**. The *Overview* page now has an **Access Route** setting inside the *Connection information* with **Public** and **Dynamic** options.
#. Select **Public** to see the public URL for your service.

The connection with the **Dynamic** option is not possible outside the VPC, while the connection with the **Public** option is accessible over the public internet. *The IP allow list* applies to all connection types (Dynamic and Public, in this example).

.. note:: You can change the **public_access** settings without any downtime for your service.