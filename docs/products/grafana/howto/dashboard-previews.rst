Dashboard preview for Aiven for Grafana®
========================================

Grafana's Dashboard Previews feature is a great way to get an overview of all your dashboards. Instead of a list view of all your dashboards, you can now see a graphical representation for each dashboard configured.

The dashboard previews feature is an opt-in beta feature available in Grafana 9.0+. This feature is disabled by default on the Aiven for Grafana® service. 

.. note:: 
    Dashboard previews are not available for Hobbyist and Startup-1 plans.

Enable dashboard previews
-------------------------

To enable dashboard previews for your Aiven for Grafana service, follow these steps:

1. Log in to `Aiven Console <https://console.aiven.io/>`_, and select the Aiven for Grafana service where you want to enable dashboard previews.
2. Click **Service settings** on the sidebar. 
3. Scroll to the **Advanced configuration** section, and select **Configure**.
4. On the **Advanced configuration** screen, click **Add configuration options**.
5. Locate ``dashboard_previews_enabled`` using the search bar and set it to the **Enabled** position.
6. Select **Save configuration**. You will see the status next to ``dashboard_previews_enabled`` change from ``not synced`` to ``synced``.
7. Go to the **Overview** page and use the **Service URI** to open the Grafana login page.
8. Enter your username and password, then click **Log in**.
9. To view dashboard previews, click **Dashboards** in the left menu and choose the grid layout. Previews will appear as thumbnails and can be organized alphabetically.

.. image:: /images/products/grafana/dashboard-previews-on-grafana.png
    :alt: Dashboard previews on Grafana

Limitations
-----------
* Dashboard previews are not available for Hobbyist and Startup-1 plans.
* Before downgrading your service plan to Hobbyist or Startup-1, where dashboard previews are unavailable, you need first to disable it on the current service. 

.. seealso::
    For more information on Dashboard previews, see `Grafana documentation <https://grafana.com/docs/grafana/latest/search/dashboard-previews/>`_. 
