Aiven for Grafana® quickstart
==============================

To start using Aiven for Grafana®, the first step is to create a service. You can do this in the `Aiven web console <https://console.aiven.io/>`_ or with the `Aiven CLI <https://github.com/aiven/aiven-client>`_.

This quickstart section provides the steps to create an Aiven for Grafana service and how to log in to Aiven for Grafana®. 

Create an Aiven for Grafana service
-----------------------------------

1. Log in to the `Aiven Console <https://console.aiven.io/>`_.

2. Follow :doc:`these instructions </docs/platform/howto/create_new_service>` to create a new Aiven for Grafana service.

Once the service is ready, the status changes to *Running*. Depending on your selected cloud provider and region, this generally takes a couple of minutes.

Log in to Grafana
-----------------
After starting the Aiven for Grafana service, you can follow these steps to access Grafana:

1. From the `Aiven Console <https://console.aiven.io/>`_, access your Aiven for Grafana service.
2. In the **Overview** tab, copy or click on the **Service URI** to launch the Grafana login page in a browser.
3. On the login page, enter or copy and paste the **User** and **Password** details from the *Connection information* section, and select **Log in**. 

You can begin visualizing your data sources using the default dashboards or create your own.

Integrates with your existing Aiven tools
------------------------------------------

Grafana is highly compatible with other Aiven products. You can set up your other Aiven services as data sources for Grafana, and monitor their health.


Check out all the features on our `Grafana product page <https://aiven.io/grafana>`_. 

Grafana resources
---------------------

* `Open source Grafana page <https://grafana.com/oss/grafana/>`_

* `Grafana docs <https://grafana.com/docs/>`_

* `Aiven Terraform Provider - Grafana resource docs <https://registry.terraform.io/providers/aiven/aiven/latest/docs/resources/grafana>`_ and `Grafana data source docs <https://registry.terraform.io/providers/aiven/aiven/latest/docs/data-sources/grafana>`_
