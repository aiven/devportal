Create MySQL Remote Replica
===========================

The goal of the remote replica is to provide a read-only instance of your managed MySQL service in another geographically diverse region. 

This works as an extra measure to protect your data from the unlikely event that a whole region would go down. It can also improve performance if a read replica is placed closer to your end-users that read from the database.

Here are the steps to provision remote replica

1. Login into the Aiven console using your credentials

2. Navigate to the MySQL instances for which you wish to create a remote replica

3. Click  the "Create a read replica" button

4. For the remote replica, give your service a name, select the cloud provider and region, and choose a suitable Aiven for MySQL plan.

5. Click "Create"

That's it. You will see the read replica being created and listed as any other Aiven service on the Services page on the console.
