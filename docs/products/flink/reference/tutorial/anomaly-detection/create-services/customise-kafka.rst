Customise the Aiven for Apache Kafka service
============================================

After creating the service, you'll be redirected to the service details page. You can now customise the service to enable the needed components in the *Overview* tab:

1. **Kafka REST API (Karapace)** > **Enable**

   .. Note:: 
    The **Kafka REST API** enables you to manage Apache Kafka via REST APIs and also to view the data in your Apache Kafka® topics.

2. **Advanced configuration** > **Add configuration option** > ``kafka.auto_create_topics_enable``, switch the setting on and then click **Save advanced configuration**

   .. Note:: 
    The ``kafka.auto_create_topics_enable`` setting allows you to create new Apache Kafka® topics as you configure your Apache Flink® data tables, so that you do not need to create the topics in advance.

.. button-link:: create-postgresql.html
    :align: right
    :color: primary
    :outline:

    Next