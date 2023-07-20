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

1. Log in to `Aiven Console <https://console.aiven.io/>`_ using your credentials.
2. In the **Services** page, select an Aiven for MySQL service for which you wish to create a remote replica.
3. In the **Overview** page of your service, go to section **Read-only replicas** and select **Create replica**.
4. In the **Create a MySQL read replica** window, give your service a name, select the cloud provider and region, and choose a suitable Aiven for MySQL plan. Select **Create** to add the defined replica.

.. topic:: Result

   You can see the read-only replica being created and listed next to other Aiven service in the **Services** page in `Aiven Console <https://console.aiven.io/>`_.
