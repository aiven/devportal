
.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``custom_domain``
    - ['string', 'null']
    - Custom domain Serve the web frontend using a custom CNAME pointing to the Aiven DNS name
  * - ``ip_filter``
    - array
    - IP filter Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'
  * - ``static_ips``
    - boolean
    - Static IP addresses Use static public IP addresses
  * - ``private_access``
    - object
    - Allow access to selected service ports from private networks 
  * - ``public_access``
    - object
    - Allow access to selected service ports from the public Internet 
  * - ``privatelink_access``
    - object
    - Allow access to selected service components through Privatelink 
  * - ``kafka``
    - object
    - Kafka broker configuration values 
  * - ``kafka_authentication_methods``
    - object
    - Kafka authentication methods 
  * - ``kafka_connect``
    - boolean
    - Enable Kafka Connect service 
  * - ``kafka_connect_config``
    - object
    - Kafka Connect configuration values 
  * - ``kafka_rest``
    - boolean
    - Enable Kafka-REST service 
  * - ``kafka_version``
    - ['string', 'null']
    - Kafka major version 
  * - ``schema_registry``
    - boolean
    - Enable Schema-Registry service 
  * - ``kafka_rest_config``
    - object
    - Kafka REST configuration 
  * - ``schema_registry_config``
    - object
    - Schema Registry configuration 

