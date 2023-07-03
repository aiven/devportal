Create Aiven for MySQL® remote replicas
=======================================

Learn how to create an Aiven for MySQL® remote replica to provide a read-only instance of your managed MySQL service in another geographically-autonomous region.

About remote replicas
---------------------

Aiven for MySQL read-only replicas provide a great way to reduce the load on the primary server by enabling read-only queries to be performed against the replica. It is also a good way to optimise query response times across different geographical locations since, with Aiven, the replica can be placed in different regions or even different cloud providers.

Using read-only replicas works as an extra measure to protect your data from the unlikely event that a whole region would go down. It can also improve performance if a read-only replica is placed closer to your end-users that read from the database.

Create a remote replica
-----------------------

Take the following steps to provision a remote replica:

1. Log in to the `Aiven console <https://console.aiven.io/>`_  using your credentials.

2. Navigate to Aiven for MySQL services for which you wish to create a remote replica.

3. In the **Overview** tab, go to section **Read-only replicas** and select **Create replica**.

.. image:: /images/products/mysql/create-replica.png
   :alt: Start creating a read-only replica 

1. For the remote replica, give your service a name, select the cloud provider and region, and choose a suitable Aiven for MySQL plan.

2. Select **Create**.

.. image:: /images/products/mysql/mysql-create-read-only-replica-choose-plan.png
   :alt: Create replica wizard

.. topic:: Result

   You can see the read-only replica being created and listed as any other Aiven service on the **Services** page in the console.
