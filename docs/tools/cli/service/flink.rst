``avn service flink``
==================================================================

Here you'll find the full list of commands for ``avn service flink``.


.. Warning::

    The Aiven for Apache Flink® CLI commands have been updated, and to execute them, you must use ``aiven-client`` version ``2.18.0``.


Manage Aiven for Apache Flink® applications
-------------------------------------------

.. _avn service flink create-application:

``avn service flink create-application``
''''''''''''''''''''''''''''''''''''''''''

Create a new Aiven for the Apache Flink® application in the specified service and project. 

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service
  * - ``application_properties``
    - Application properties definition for Aiven for Flink application, either as a JSON string or a file path (prefixed with '@') containing the JSON configuration

The ``application_properties`` parameter should contain the following common properties in JSON format:

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information

  * - ``name``
    -  The name of the application
  * - ``application_version``
    - (Optional)The version of the application

**Example:** Creates an Aiven for Apache Flink application named ``DemoApp`` in the service ``flink-democli`` and project ``my-project``. 

::

  avn service flink create-application flink-democli  \
    --project my-project                              \
    "{\"name\":\"DemoApp\"}"

An example of ``avn service flink create-application`` output:

.. code:: text

  {
    "application_versions": [],
    "created_at": "2023-02-08T07:37:25.165996Z",
    "created_by": "wilma@example.com",
    "id": "2b29f4aa-a496-4fca-8575-23544415606e",
    "name": "DemoApp",
    "updated_at": "2023-02-08T07:37:25.165996Z",
    "updated_by": "wilma@example.com"
  }

``avn service flink list-applications``
'''''''''''''''''''''''''''''''''''''''''
Lists all the Aiven for Apache Flink® applications in a specified project and service. 

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service

**Example:** Lists all the Aiven for Flink applications for the service ``flink-democli`` in the project ``my-project``. 

::

  avn service flink list-applications flink-democli \
    --project my-project 

An example of ``avn service flink list-applications`` output:

.. code:: text

  {
    "applications": [
        {
            "created_at": "2023-02-08T07:37:25.165996Z",
            "created_by": "wilma@example.com",
            "id": "2b29f4aa-a496-4fca-8575-23544415606e",
            "name": "DemoApp",
            "updated_at": "2023-02-08T07:37:25.165996Z",
            "updated_by": "wilma@example.com"
        }
    ]
  }

``avn service flink get-application``
''''''''''''''''''''''''''''''''''''''
Retrieves the information about the Aiven for Flink® applications in a specified project and service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service
  * - ``application-id``
    - The ID of the Aiven for Flink application to retrieve information about. 

**Example:** Retrieves information about Aiven for Flink® application with application-id ``2b29f4aa-a496-4fca-8575-23544415606e`` for service ``flink-democli`` and project ``my-project`` 

::
  
  avn service flink get-application flink-democli \
    --project my-project                          \
    --application-id 2b29f4aa-a496-4fca-8575-23544415606e

An example of ``avn service flink list-applications`` output:

.. code:: text

  {
      "application_versions": [],
      "created_at": "2023-02-08T07:37:25.165996Z",
      "created_by": "wilma@example.com",
      "id": "2b29f4aa-a496-4fca-8575-23544415606e",
      "name": "DemoApp",
      "updated_at": "2023-02-08T07:37:25.165996Z",
      "updated_by": "wilma@example.com"
  }


``avn service flink update-application``
''''''''''''''''''''''''''''''''''''''''''
Update an Aiven for Flink® application in a specified project and service. 

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service
  * - ``application-id``
    - The ID of the Aiven for Flink application to update 
  * - ``application-properties``
    - Application properties definition for Aiven for Flink® application, either as a JSON string or a file path (prefixed with '@') containing the JSON configuration

The ``application_properties`` parameter should contain the following common properties in JSON format

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information

  * - ``name``
    -  The name of the application

**Example:** Updates the name of the Aiven for Flink application from ``Demo`` to ``DemoApp`` for application-id ``986b2d5f-7eda-480c-bcb3-0f903a866222`` in the service ``flink-democli`` and project ``my-project``. 
::
  
  avn  service flink update-application flink-democli     \
    --project my-project                                  \
    --application-id 986b2d5f-7eda-480c-bcb3-0f903a866222 \
    "{\"name\":\"DemoApp\"}"



``avn  service flink delete-application``
''''''''''''''''''''''''''''''''''''''''''
Delete an Aiven for Flink® application in a specified project and service. 

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service
  * - ``application-id``
    - The ID of the Aiven for Flink application to delete 

**Example:** Deletes the Aiven for Flink application with application-id  ``64192db8-d073-4e28-956b-82c71b016e3e`` for the service ``flink-democli`` in the project ``my-project``. 

::
  
  avn  service flink delete-application flink-democli \
    --project my-project                              \
    --application-id 64192db8-d073-4e28-956b-82c71b016e3e

``avn service flink create-application-version``
''''''''''''''''''''''''''''''''''''''''''''''''''
Create an Aiven for Flink® application version in a specified project and service. 

.. Warning::

  Before creating an application, you need to :doc:`create integrations </docs/products/flink/howto/create-integration>` between Aiven for Apache Flink and the source/sinks data services. As of now you can define integration with:

  * Aiven for Apache Kafka® as source/sink
  * Aiven for Apache PostgreSQL® as source/sink
  * Aiven for OpenSearch® as sink

  Sinking data using the :doc:`Slack connector </docs/products/flink/howto/slack-connector>`, doesn't need an integration.

  **Example**: to create an integration between an Aiven for Apache Flink service named ``flink-democli`` and an Aiven for Apache Kafka service named ``demo-kafka`` you can use the following command::

    avn service integration-create    \
      --integration-type flink        \
      --dest-service flink-democli    \
      --source-service demo-kafka
  
  All the available command integration options can be found in the :ref:`dedicated document <avn_service_integration_create>`

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service
  * - ``application-id``
    - The ID of the Aiven for Flink application to create a version 
  * - ``application_version_properties``
    - Application version properties definition for Aiven for Flink® application, either as a JSON string or a file path (prefixed with '@') containing the JSON configuration


The ``application_version_properties`` parameter should contain the following common properties in JSON format:

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information

  * - ``sinks``
    -  An array of objects that contains the table creation statements creation statements of the sinks
  * - ``create_table``
    - A string that defines the CREATE TABLE statement of the sink including the integration ID. The integration ID can be found with the :ref:`integration-list<avn_service_integration_list>` command
  * - ``source``
    - An array of objects that contains the table creation statements of the source
  * - ``create_table``
    - A string that defines the CREATE TABLE statement of the source including the integration ID. The integration ID can be found with the :ref:`integration-list<avn_service_integration_list>` command
  * - ``statement``
    -  The transformation SQL statement of the application

**Example:** Creates a new Aiven for Flink application version for application-id ``986b2d5f-7eda-480c-bcb3-0f903a866222`` with the following details:

* **Source**: a table, named ``special_orders`` coming from an Apache Kafka® topic named ``special_orders_topic`` using the integration with id ``4ec23427-9e9f-4827-90fa-ea9e38c31bc3`` and the following columns::

    id INT, 
    name VARCHAR, 
    topping VARCHAR

* **Sink**: a table, called ``pizza_orders``, writing to an Apache Kafka® topic named ``pizza_orders_topic`` using the integration with id ``4ec23427-9e9f-4827-90fa-ea9e38c31bc3`` and the following columns::

    id INT, 
    name VARCHAR, 
    topping VARCHAR

* **SQL statement**::

    INSERT INTO special_orders 
    SELECT id, 
      name, 
      c.topping 
    FROM pizza_orders 
      CROSS JOIN UNNEST(pizzas) b 
      CROSS JOIN UNNEST(b.additionalToppings) AS c(topping) 
    WHERE c.topping IN ('🍍 pineapple', '🍓 strawberry','🍌 banana')

::
  
  avn service flink create-application-version flink-democli        \
    --project my-project                                            \
    --application-id 986b2d5f-7eda-480c-bcb3-0f903a866222           \
    """{
      \"sources\": [ 
        { 
          \"create_table\": 
            \"CREATE TABLE special_orders (                         \
                id INT,                                             \
                name VARCHAR,                                       \
                topping VARCHAR                                     \
                )                                                   \
              WITH (                                                \
                'connector' = 'kafka',                              \
                'properties.bootstrap.servers' = '',                \
                'scan.startup.mode' = 'earliest-offset',            \
                'value.fields-include' = 'ALL',                     \
                'topic' = 'special_orders_topic',                   \
                'value.format' = 'json'                             \
              )\", 
              \"integration_id\": \"4ec23427-9e9f-4827-90fa-ea9e38c31bc3\" 
        } ],   
      \"sinks\": [ 
        { 
          \"create_table\": 
            \"CREATE TABLE pizza_orders (                                                   \
                id INT,                                                                     \
                shop VARCHAR,                                                               \
                name VARCHAR,                                                               \
                phoneNumber VARCHAR,                                                        \
                address VARCHAR,                                                            \
                pizzas ARRAY<ROW(pizzaName VARCHAR, additionalToppings ARRAY <VARCHAR>)>)   \
              WITH (                                                                        \
                'connector' = 'kafka',                                                      \
                'properties.bootstrap.servers' = '',                                        \
                'scan.startup.mode' = 'earliest-offset',                                    \
                'topic' = 'pizza_orders_topic',                                             \
                'value.format' = 'json'                                                     \
              )\",                                                                          
              \"integration_id\": \"4ec23427-9e9f-4827-90fa-ea9e38c31bc3\"                  
          } 
          ],
      \"statement\": 
        \"INSERT INTO special_orders                                        \
          SELECT id,                                                        \
            name,                                                           \
            c.topping                                                       \
          FROM pizza_orders                                                 \
            CROSS JOIN UNNEST(pizzas) b                                     \
            CROSS JOIN UNNEST(b.additionalToppings) AS c(topping)           \
          WHERE c.topping IN ('🍍 pineapple', '🍓 strawberry','🍌 banana')\"
    }"""




``avn service flink validate-application-version``
''''''''''''''''''''''''''''''''''''''''''''''''''
Validates the Aiven for Flink® application version in a specified project and service.

.. Warning::

  Before creating an application, you need to :doc:`create integrations </docs/products/flink/howto/create-integration>` between Aiven for Apache Flink and the source/sinks data services. As of now you can define integration with:

  * Aiven for Apache Kafka® as source/sink
  * Aiven for Apache PostgreSQL® as source/sink
  * Aiven for OpenSearch® as sink

  Sinking data using the :doc:`Slack connector </docs/products/flink/howto/slack-connector>`, doesn't need an integration.

  **Example**: to create an integration between an Aiven for Apache Flink service named ``flink-democli`` and an Aiven for Apache Kafka service named ``demo-kafka`` you can use the following command::

    avn service integration-create    \
      --integration-type flink        \
      --dest-service flink-democli    \
      --source-service demo-kafka
  
  All the available command integration options can be found in the :ref:`dedicated document <avn_service_integration_create>`

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service
  * - ``application-id``
    - The ID of the Aiven for Flink application to create a version 
  * - ``application_version_properties``
    - Application version properties definition for Aiven for Flink application, either as a JSON string or a file path (prefixed with '@') containing the JSON configuration


The ``application_version_properties`` parameter should contain the following common properties in JSON format

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information

  * - ``sinks``
    -  An array of objects that contains the table creation statements creation statements of the sinks
  * - ``create_table``
    - A string that defines the CREATE TABLE statement of the sink including the integration ID. The integration ID can be found with the :ref:`integration-list<avn_service_integration_list>` command
  * - ``source``
    - An array of objects that contains the table creation statements of the source
  * - ``create_table``
    - A string that defines the CREATE TABLE statement of the source including the integration ID. The integration ID can be found with the :ref:`integration-list<avn_service_integration_list>` command
  * - ``statement``
    -  The transformation SQL statement of the application


**Example:** Validates the Aiven for Flink application version for the application-id ``986b2d5f-7eda-480c-bcb3-0f903a866222``. 

::
  
  avn service flink validate-application-version flink-democli        \
    --project my-project                                            \
    --application-id 986b2d5f-7eda-480c-bcb3-0f903a866222           \
    """{
      \"sources\": [ 
        { 
          \"create_table\": 
            \"CREATE TABLE special_orders (                         \
                id INT,                                             \
                name VARCHAR,                                       \
                topping VARCHAR                                     \
                )                                                   \
              WITH (                                                \
                'connector' = 'kafka',                              \
                'properties.bootstrap.servers' = '',                \
                'scan.startup.mode' = 'earliest-offset',            \
                'value.fields-include' = 'ALL',                     \
                'topic' = 'special_orders_topic',                   \
                'value.format' = 'json'                             \
              )\", 
              \"integration_id\": \"4ec23427-9e9f-4827-90fa-ea9e38c31bc3\" 
        } ],   
      \"sinks\": [ 
        { 
          \"create_table\": 
            \"CREATE TABLE pizza_orders (                                                   \
                id INT,                                                                     \
                shop VARCHAR,                                                               \
                name VARCHAR,                                                               \
                phoneNumber VARCHAR,                                                        \
                address VARCHAR,                                                            \
                pizzas ARRAY<ROW(pizzaName VARCHAR, additionalToppings ARRAY <VARCHAR>)>)   \
              WITH (                                                                        \
                'connector' = 'kafka',                                                      \
                'properties.bootstrap.servers' = '',                                        \
                'scan.startup.mode' = 'earliest-offset',                                    \
                'topic' = 'pizza_orders_topic',                                             \
                'value.format' = 'json'                                                     \
              )\",                                                                          
              \"integration_id\": \"4ec23427-9e9f-4827-90fa-ea9e38c31bc3\"                  
          } 
          ],
      \"statement\": 
        \"INSERT INTO special_orders                                        \
          SELECT id,                                                        \
            name,                                                           \
            c.topping                                                       \
          FROM pizza_orders                                                 \
            CROSS JOIN UNNEST(pizzas) b                                     \
            CROSS JOIN UNNEST(b.additionalToppings) AS c(topping)           \
          WHERE c.topping IN ('🍍 pineapple', '🍓 strawberry','🍌 banana')\"
    }"""


``avn service flink get-application-version``
''''''''''''''''''''''''''''''''''''''''''''''
Retrieves information about a specific version of an Aiven for Flink® application in a specified project and service. 

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service
  * - ``application-id``
    - The ID of the Aiven for Flink application
  * - ``application-version-id``
    - The ID of the Aiven for Flink application version to retrieve information about


**Example:** Retrieves the information specific to the Aiven for Flink® application for the service ``flink-demo-cli`` and project ``my-project`` with:

* Application id: ``986b2d5f-7eda-480c-bcb3-0f903a866222``
* Application version id: ``7a1c6266-64da-4f6f-a8b0-75207f997c8d``


::
  
  avn service flink get-application-version flink-democli \
    --project my-project                                  \
    --application-id 986b2d5f-7eda-480c-bcb3-0f903a866222 \
    --application-version-id 7a1c6266-64da-4f6f-a8b0-75207f997c8d



``avn service flink delete-application-version``
''''''''''''''''''''''''''''''''''''''''''''''''''
Deletes a version of the Aiven for Flink® application in a specified project and service. 

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service
  * - ``application-id``
    - The ID of the Aiven for Flink application
  * - ``application-version-id``
    - The ID of the Aiven for Flink application version to delete


**Example:** Delete the Aiven for Flink application version for service ``flink-demo-cli`` and project ``my-project`` with: 

* Application id: ``986b2d5f-7eda-480c-bcb3-0f903a866222``
* Application version id: ``7a1c6266-64da-4f6f-a8b0-75207f997c8d``

::
  
  avn service flink delete-application-version flink-democli  \
    --project my-project                                      \
    --application-id 986b2d5f-7eda-480c-bcb3-0f903a866222     \
    --application-version-id 7a1c6266-64da-4f6f-a8b0-75207f997c8d


``avn service flink list-application-deployments``
''''''''''''''''''''''''''''''''''''''''''''''''''''
Lists all the Aiven for Flink® application deployments in a specified project and service. 

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service
  * - ``application-id``
    - The ID of the Aiven for Flink application

**Example:** Lists all the Aiven for Flink application deployments for application-id ``f171af72-fdf0-442c-947c-7f6a0efa83ad`` for the service ``flink-democli``, in the project ``my-project``. 

::
  
  avn service flink list-application-deployments flink-democli \
    --project my-project                                       \
    --application-id f171af72-fdf0-442c-947c-7f6a0efa83ad


``avn service flink get-application-deployment``
''''''''''''''''''''''''''''''''''''''''''''''''''
Retrieves information about an Aiven for Flink® application deployment in a specified project and service. 

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service
  * - ``application-id``
    - The ID of the Aiven for Flink application
  * - ``deployment-id``
    - The ID of the Aiven for Flink application deployment. This ID can be obtained from the output of the ``avn service flink list-application-deployments`` command


**Example:** Retrieves the details of the Aiven for Flink application deployment for the application-id ``f171af72-fdf0-442c-947c-7f6a0efa83ad``, deployment-id ``bee0b5cb-01e7-49e6-bddb-a750caed4229`` for the service ``flink-democli``, in the project ``my-project``. 

::
  
  avn service flink get-application-deployment flink-democli \
    --project my-project                                     \
    --application-id f171af72-fdf0-442c-947c-7f6a0efa83ad     \
    --deployment-id bee0b5cb-01e7-49e6-bddb-a750caed4229


``avn service flink create-application-deployment``
''''''''''''''''''''''''''''''''''''''''''''''''''''

Creates a new Aiven for Flink® application deployment in a specified project and service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service
  * - ``application-id``
    - The ID of the Aiven for Flink application
  * - ``deployment_properties``
    - The deployment properties definition for Aiven for Flink application, either as a JSON string or a file path (prefixed with '@') containing the JSON configuration


The ``deployment_properties`` parameter should contain the following common properties in JSON format

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``parallelism``
    - The number of parallel instance for the task
  * - ``restart_enabled``
    - Specifies whether a Flink Job is restarted in case it fails
  * - ``starting_savepoint``
    - (Optional)The the savepoint from where you want to deploy.
  * - ``version_id``
    - The ID of the application version. 

**Example:** Create a new Aiven for Flink application deployment for the application id ``986b2d5f-7eda-480c-bcb3-0f903a866222``.

::

  avn service flink create-application-deployment  flink-democli  \
    --project my-project                                          \
    --application-id 986b2d5f-7eda-480c-bcb3-0f903a866222         \
    "{\"parallelism\": 1,\"restart_enabled\": true,  \"version_id\": \"7a1c6266-64da-4f6f-a8b0-75207f997c8d\"}"


``avn service flink delete-application-deployment``
''''''''''''''''''''''''''''''''''''''''''''''''''''''
Deletes an Aiven for Flink® application deployment in a specified project and service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service
  * - ``application-id``
    - The ID of the Aiven for Flink® application
  * - ``deployment-id``
    - The ID of the Aiven for Flink® application deployment to delete

**Example:** Deletes the Aiven for Flink application deployment with application-id ``f171af72-fdf0-442c-947c-7f6a0efa83ad`` and deployment-id ``6d5e2c03-2235-44a5-ab8f-c544a4de04ef``.

::
  
  avn service flink delete-application-deployment flink-democli   \
    --project my-project                                          \
    --application-id f171af72-fdf0-442c-947c-7f6a0efa83ad         \
    --deployment-id 6d5e2c03-2235-44a5-ab8f-c544a4de04ef

``avn service flink stop-application-deployment``
''''''''''''''''''''''''''''''''''''''''''''''''''
Stops a running Aiven for Flink® application deployment in a specified project and service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service
  * - ``application-id``
    - The ID of the Aiven for Flink application
  * - ``deployment-id``
    - The ID of the Aiven for Flink application deployment to stop



**Example:** Stops the Aiven for Flink application deployment with application-id ``f171af72-fdf0-442c-947c-7f6a0efa83ad`` and deployment-id ``6d5e2c03-2235-44a5-ab8f-c544a4de04ef``.

::
  
  avn service flink stop-application-deployment flink-democli   \
    --project my-project                                          \
    --application-id f171af72-fdf0-442c-947c-7f6a0efa83ad         \
    --deployment-id 6d5e2c03-2235-44a5-ab8f-c544a4de04ef

``avn service flink cancel-application-deployments``
'''''''''''''''''''''''''''''''''''''''''''''''''''''
Cancels an Aiven for Flink® application deployment in a specified project and service. 

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``project``
    - The name of the project
  * - ``service_name``
    - The name of the service
  * - ``application-id``
    - The ID of the Aiven for Flink application
  * - ``deployment-id``
    - The ID of the Aiven for Flink application deployment to cancel


**Example:** Cancels the Aiven for Flink application deployment with application-id ``f171af72-fdf0-442c-947c-7f6a0efa83ad`` and deployment-id ``6d5e2c03-2235-44a5-ab8f-c544a4de04ef``.

::
  
  avn service flink cancel-application-deployments flink-democli   \
    --project my-project                                          \
    --application-id f171af72-fdf0-442c-947c-7f6a0efa83ad         \
    --deployment-id 6d5e2c03-2235-44a5-ab8f-c544a4de04ef


