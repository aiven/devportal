Perform migration check
=======================

In this article, we show how to find potential errors before starting your database migration process. 
This can be done by using either the `Aiven CLI <https://github.com/aiven/aiven-client>`_  or `Aiven REST API <https://api.aiven.io/doc/#section/Introduction>`_. 

When migrating a database to Aiven, you may find errors such as:

.. code-block:: shell

    {
        "migration": {
            "error": "Migration process failed",
            "method": "",
            "seconds_behind_master": null,
            "source_active": true,
            "status": "done"
        },
        "migration_detail": []
    }
    -----Response End-----
    STATUS METHOD ERROR
    ====== ====== ========================
    done Migration process failed



To avoid these types of failures during the migration process we recommend you run some checks in advance. In this article, we will show how you can run those checks for your MySQL migration process.

Aiven CLI
---------

**Step 1: create a task to perform the migration check.**


You can create the task of migration, for example, from a MySQL DB to an Aiven service (``project``: ``MY_PROJECT_NAME``, ``service``: ``mysql``):

.. code-block:: shell
    
    avn service task-create --operation migration_check --source-service-uri mysql://user:password@host:port/databasename --project MY_PROJECT_NAME mysql

You can see the information about the task including the ID.

.. code-block:: shell

    TASK_TYPE              SUCCESS  TASK_ID                             
    =====================  =======  ====================================
    mysql_migration_check  null     e2df7736-66c5-4696-b6c9-d33a0fc4cbed


.. tip::
    
    You can find more options available via the -h menu, for example, to ignore certain databases for the check. Please note that filter databases are supported by MySQL only at the moment.

**Step 2: retrieve your task's status.**

You can check the status of your task by running::

    avn service task-get --task-id e2df7736-66c5-4696-b6c9-d33a0fc4cbed --project MY_PROJECT_NAME mysql

You can find whether the operation succeeds and more relevant information about the migration.

.. code-block:: shell

    TASK_TYPE              SUCCESS  TASK_ID                               RESULT                                                                              
    =====================  =======  ====================================  ====================================================================================
    mysql_migration_check  true     e2df7736-66c5-4696-b6c9-d33a0fc4cbed  All pre-checks passed successfully, preferred migration method will be [Replication]

Aiven REST API
--------------

The same checks can be performed via the REST API. More details can be found here:

* `Create a new task for service <https://api.aiven.io/doc/#operation/ServiceTaskCreate>`_
* `Get task result <https://api.aiven.io/doc/#operation/ServiceTaskGet>`_