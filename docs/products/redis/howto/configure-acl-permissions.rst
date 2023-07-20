Configure ACL permissions in Aiven for Redis®*
==============================================

Redis®* uses `Access Control Lists (ACLs) <https://redis.io/docs/management/security/acl/>`_ to restrict the usage of commands and keys based on specific username and password combinations. In Aiven for Redis®*, the direct use of  `ACL * <https://redis.io/commands/acl-list/>`_ commands is not allowed to maintain the reliability of replication, configuration management, and disaster recovery backups for the default user. However, you have the flexibility to create custom ACLs using either the `Aiven Console <https://console.aiven.io/>`_ or the :doc:`Aiven CLI </docs/tools/cli>`.

With the Aiven Console or Aiven CLI, you can customize ACL permissions to align with your requirements. This gives you granular control over access and ensures optimal security within your Aiven for Redis®* service.


Create user and configure ACLs using console
-----------------------------------------------
Follow the steps below to create a Redis user and configure ACLs: 

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and select your Aiven for Redis service from the list of available services.
2. Select **Users** from the left sidebar.
3. Select **Create user**, and provide the following details: 
   
   * **Username:** Specify a username for the user.
   * **Categories:** Specify the command categories the user can access within Aiven for Redis. For example, you can use the prefix ``+@all`` or a similar convention to grant users access to all categories. Separate each category entry with a single space.
   * **Commands:** Specify the commands the user can execute, separating each command by a single space. For example, you can enter ``+set -get`` to grant the user permission to execute the SET command and deny access to the GET command. 
   * **Channels:** Specify the channels the user can access within the Publish/Subscribe (Pub/Sub) messaging pattern. Separate each channel entry with a single space.
   * **Keys:** Specify the keys the user can interact with. For example, you can specify keys like ``user:123`` or  ``product:456``, or ``order:789`` to grant the user access to interact with these specific keys in Aiven for Redis. 
  
4. Once you have defined the ACL permissions for the user, select **Save** to create the user.


User management
----------------
You have various management options available for Aiven for Redis users. Follow the instructions below for each operation:

Reset password
`````````````````
1. Select **Users** from the left sidebar, locate the user you want to reset the password and select the ellipses next to their row.
2. Select **Reset password** from the drop-down menu.
3. Confirm the password reset by selecting **Reset** on the confirmation screen.

Edit ACL rules
```````````````
1. Select **Users** from the left sidebar, locate the user you want to edit ACL rules and select the ellipses next to their row.
2. Select **Edit ACL rules** from the drop-down menu.
3. Make the desired changes to the ACL rules on the **Edit access control** screen.
4. Select the **Save**  to apply the modifications.

Duplicate user
```````````````
1. Select **Users** from the left sidebar, locate the user you want to duplicate and select the icon next to their row.
2. Select **Duplicate user** from the options in the drop-down menu.
3. Enter a name for the new user in the **Duplicate user** screen.
4. Click on the **Add user** button to create a duplicate user.

Delete user
`````````````
1. Locate the user you want to delete from the user list and select the icon next to their row.
2. Select **Delete** from the options in the drop-down menu.
3. Confirm the deletion by selecting **Delete** on the confirmation screen.


Create user and configure ACLs using Aiven CLI
-----------------------------------------------

To create a user and configure ACLs using the Aiven CLI, follow these steps:

1. Set up the :doc:`CLI tool </docs/tools/cli>`. 

2. Create a user named ``mynewuser`` with read-only access to the ``mykeys.*`` keys using the following command:

   ::

      avn service user-create --project myproject myservicename --username mynewuser --redis-acl-keys 'mykeys.*' --redis-acl-commands '+get' --redis-acl-categories ''

3. Confirm the ACL is applied by connecting to the service using the new username and password: 
   
   ::

      redis-cli --user mynewuser --pass ... --tls -h myservice-myproject.aivencloud.com -p 12719

      myservice-myproject.aivencloud.com:12719> get mykeys.hello
      (nil)
      myservice-myproject.aivencloud.com:12719> set mykeys.hello world
      (error) NOPERM this user has no permissions to run the 'set' command or its subcommand
