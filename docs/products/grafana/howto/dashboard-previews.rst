Dashboard preview for Aiven for Grafana®
========================================

Grafana's Dashboard Previews feature is a great way to get an overview of all your dashboards. Instead of a list view of all your dashboards, you can now see a graphical representation for each dashboard configured.

The dashboard previews feature is an opt-in beta feature available in Grafana 9.0+. This feature is disabled by default on the Aiven for Grafana® service. 

.. note:: 
    Dashboard previews are not available for Hobbyist and Startup-1 plans.

Enable dashboard previews
-------------------------

Follow these steps to enable dashboard previews for your Aiven for Grafana service:

1. In the `Aiven Console <https://console.aiven.io/>`_, select your project and then choose your Aiven for Grafana® service.
2. In the service page, select **Service settings** from the sidebar. 
3. On the **Service settings** page, scroll down to the **Advanced configuration** section, and click **Configure**.
4. In the **Advanced configuration** dialog, click **Add configuration option**.
5. Find and set ``dashboad_previews_enabled`` to **Enabled** position. 
6. Click the **Save configuration**. You will notice the status next to ``dashboad_previews_enabled`` change from ``not synced`` to ``synced``. 
7. Using the **Service URI**, open the Grafana login page. 
8. Enter the username and password, and click **Log in**. 
9. Click **Dashboards** on the left side menu, and select the grid layout to view dashboard previews of all the dashboards. Dashboard previews are rendered as thumbnails and can be sorted alphabetically. 

   .. image:: /images/products/grafana/dashboard-previews-on-grafana.png
      :alt: Dashboard previews on Grafana

Limitations
-----------
* Dashboard previews are not available for Hobbyist and Startup-1 plans.
* Before downgrading your service plan to Hobbyist or Startup-1, where dashboard previews are unavailable, you need first to disable it on the current service. 

.. seealso::
    For more information on Dashboard previews, see `Grafana documentation <https://grafana.com/docs/grafana/latest/dashboards/>`_.
