Dashboard preview for Aiven for Grafana®
========================================

The Dashboard previews feature in Grafana provides an overview of all your dashboards. Instead of a list view of all your dashboards, you can now see previews for each dashboard configured. 

The dashboard previews feature is an opt-in beta feature available in Grafana 9.0+. This feature is disabled by default on the Aiven for Grafana® service. 

.. note:: 
    Dashboard previews are not available for Hobbyist and Startup-1 plans.

Enable dashboard preview
------------------------

Follow these steps to enable dashboard previews for your Aiven for Grafana service:

1. Log in to the `Aiven Console <https://console.aiven.io/>`_.
2. On the **Services** page, click the Grafana service for which you want to enable dashboard previews. 
3. On the **Services overview** page, scroll down to the **Advanced configuration** section. 
4. Click the **Change** button.
5. In the Edit advanced configuration pop-up screen, turn the toggle on next to ``dashboad_previews_enabled`` to enable the feature. 
6. Click the **Save advanced configuration** button. You will notice the status next to ``dashboad_previews_enabled`` change from ``not synced`` to ``synced``. 

.. image:: /images/products/grafana/enable-dashboard-previews.png
    :alt: Enable dashboard previews in Advanced configuration

7. Using the **Service URI**, open the Grafana login page. 
8. Enter the username and password, and click **Log in**. 
9.  Click **Dashboards** on the left side menu, and you will see previews of all the dashboards.

.. image:: /images/products/grafana/dashboard-previews-on-grafana.png
    :alt: Dashboard previews on Grafana





