Deploy a PostgreSQL® service with custom configurations
=======================================================

PostgreSQL® has been a popular choice as an open source, relational database to run in production. This example shows how to use Terraform to create a single PostgreSQL service in a single cloud and region with some custom configurations applied to the service.

The following image shows that the `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ calls the Aiven API under the hood to create an Aiven for PostgreSQL® service on the Google Cloud Platform (Europe):

.. mermaid::

   flowchart LR
      id1[[Terraform]]
      id2>Aiven Terraform Provider]
      subgraph Aiven Platform
      id3[(Aiven for PostgreSQL)]
      end
      id1 --> id2 --> id3

Let's cook!
'''''''''''''''''''''''''''''''''''

The following sample Terraform script stands up the single PostgreSQL service with some custom configurations. 

Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name``, ``api_token``, ``admin_username``, and ``admin_password``.

.. dropdown:: Expand to check out the relevant common files needed for this recipe.

    Navigate to a new folder and add the following files.

    1. Add the following to a new ``provider.tf`` file:

    .. code:: terraform

       terraform {
         required_providers {
           aiven = {
             source  = "aiven/aiven"
             version = ">= 3.7"
           }
         }
       }
   
       provider "aiven" {
         api_token = var.aiven_api_token
       }
   
    You can also set the environment variable ``AIVEN_TOKEN`` for the ``api_token`` property. With this, you don't need to pass the ``-var-file`` flag when executing Terraform commands.
 
    2. To avoid including sensitive information in source control, the variables are defined here in the ``variables.tf`` file. You can then use a ``*.tfvars`` file with the actual values so that Terraform receives the values during runtime, and exclude it.

    The ``variables.tf`` file defines the API token, the project name to use, and the prefix for the service name:

    .. code:: terraform

       variable "aiven_api_token" {
         description = "Aiven console API token"
         type        = string
       }
   
       variable "project_name" {
         description = "Aiven console project name"
         type        = string
       }
   
       variable "admin_username" {
         description = "Your preferred username for the PostgreSQL service"
         type        = string
       }

       variable "admin_password" {
         description = "Your preferred password for the PostgreSQL service"
         type        = string
       }

    3. The ``var-values.tfvars`` file holds the actual values and is passed to Terraform using the ``-var-file=`` flag.

    ``var-values.tfvars`` file:

    .. code:: terraform

       aiven_api_token     = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
       project_name        = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"
       admin_username      = "<YOUR-PREFERRED-SERVICE-USERNAME>"
       admin_password      = "<YOUR-PREFERRED-SERVICE-PASSWORD>"

``services.tf`` file:

.. code:: terraform
  
  resource "aiven_pg" "pg" {
    project                 = var.project_name
    cloud_name              = "google-europe-west1"
    plan                    = "startup-4"
    service_name            = "my-pg1-gcp-eu"
    maintenance_window_dow  = "monday"
    maintenance_window_time = "10:00:00"
    termination_protection  = true
  
    pg_user_config {
      pg_version                = 14
      backup_hour               = 01
      backup_minute             = 30
      shared_buffers_percentage = 40
  
      ip_filter           = ["0.0.0.0/0"]
      admin_username      = var.admin_username
      admin_password      = var.admin_password
      
      ## project_to_fork_from  = "source-project-name" 
      ## service_to_fork_from  = "source-pg-service"   
      ## pg_read_replica       = true                  
  
      pg {
        idle_in_transaction_session_timeout = 900
        log_min_duration_statement          = 1000
        deadlock_timeout                    = 2000
      }
    }
  }

.. dropdown:: Expand to check out how to execute the Terraform files.

    The ``init`` command performs several different initialization steps in order to prepare the current working directory for use with Terraform. In our case, this command automatically finds, downloads, and installs the necessary Aiven Terraform provider plugins.
    
    .. code:: shell

       terraform init

    The ``plan`` command creates an execution plan and shows you the resources that will be created (or modified) for you. This command does not actually create any resource; this is more like a preview.

    .. code:: bash

       terraform plan -var-file=var-values.tfvars

    If you're satisfied with the output of ``terraform plan``, go ahead and run the ``terraform apply`` command which actually does the task or creating (or modifying) your infrastructure resources. 

    .. code:: bash

       terraform apply -var-file=var-values.tfvars

When running a database in production, there are lots of fine tunings that need to happen. Let's go over some of these optional custom configurations used and understand when to use them. 

First, you can choose the PostgreSQL version using the ``pg_version`` parameter. A default version is chosen for you if you don't specify the version.
``backup_hour`` and ``backup_minute`` denote the hour and minute of the day (in UTC) when backup for the service is started. In this example, the backup starts at 1:30 AM UTC daily. ``shared_buffers_percentage`` sets the percentage of memory in your system that the database server uses for shared memory buffers.
To learn more about these settings, please refer to the PostgreSQL resource consumption docs mentioned under the **More resources** section. 

The ``ip_filter`` parameter filters incoming connections based on the mentioned IP addresses. The example of **"0.0.0.0/0"** is an allow-all value. 
If there are only specific IP addresses that you'd like to allow for clients, you'd put those IP addresses on this list. When you create an Aiven for PostgreSQL service, the database admin username and password are generated for you. You can set your preferred values by using ``admin_username`` and ``admin_password`` parameters.

If you wanted this PostgreSQL service to be a read replica of an existing PostgreSQL service, you could do that by declaring the ``project_to_fork_from``, ``service_to_fork_from`` and setting the value of ``pg_read_replica`` to **true**. Since the service in this example is not a read replica, these configuration lines are commented out.
If you choose to set ``pg_read_replica`` to **true**, then the custom ``admin_username`` and ``admin_password`` will no longer work because the configurations from the master node will be used.
 
If a transaction is waiting for a client query, there might be a time limit after which you want the session to time out. This is exactly what ``idle_in_transaction_session_timeout`` will do for you if you set a limit. Keep in mind that a value of zero, which is the default value, will disable the timeout.
Once you have some idea of how long a typical query statement should take to execute, ``log_min_duration_statement`` setting allows you to log only the ones that exceed some threshold you set. And then, you'll only see statements that take longer than the specified time to run. This can be extremely handy in finding the source of outlier statements that take much longer than most to execute.
The ``deadlock_timeout`` is the amount of time that PostgreSQL waits on a lock before it checks for a deadlock condition. The deadlock check is an expensive operation, so it is not run every time the server waits for a lock. The default is one second, but this can be increased for heavily loaded servers. All of these times are taken as milliseconds if specified without units.


More resources
'''''''''''''''''

To learn how to get started with Aiven Terraform Provider and specific PostgreSQL configurations for you use case, check out the following resources:

- `What is PostgreSQL®? <https://aiven.io/blog/an-introduction-to-postgresql>`_
- `Configuration options for PostgreSQL <https://developer.aiven.io/docs/products/postgresql/reference/list-of-advanced-params.html>`_
- `PostgreSQL Resource Consumption <https://www.postgresql.org/docs/current/runtime-config-resource.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
