Dashboard preview for Aiven for Grafana®
========================================

Grafana's Dashboard Previews feature is a great way to get an overview of all your dashboards. Instead of a list view of all your dashboards, you can now see a graphical representation for each dashboard configured.

The dashboard previews feature is an opt-in beta feature available in Grafana 9.0+. This feature is disabled by default on the Aiven for Grafana® service. 

.. note:: 
    Dashboard previews are not available for Hobbyist and Startup-1 plans.

Enable dashboard previews
-------------------------

Follow these steps to enable dashboard previews for your Aiven for Grafana service:

1. Log in to the `Aiven Console <https://console.aiven.io/>`_.
2. On the **Services** page, click the Grafana service for which you want to enable dashboard previews. 
3. On the **Services overview** page, scroll down to the **Advanced configuration** section. 
4. Click the **Change** button.
5. In the **Edit advanced configuration** pop-up screen, turn the toggle on next to ``dashboad_previews_enabled`` to enable the feature. 
6. Click the **Save advanced configuration** button. You will notice the status next to ``dashboad_previews_enabled`` change from ``not synced`` to ``synced``. 

.. image:: /images/products/grafana/enable-dashboard-previews.png
    :alt: Enable dashboard previews in Advanced configuration

7. Using the **Service URI**, open the Grafana login page. 
8. Enter the username and password, and click **Log in**. 
9.  Click **Dashboards** on the left side menu, and select the grid layout to view dashboard previews of all the dashboards. Dashboard previews are rendered as thumbnails and can be sorted alphabetically. 

.. image:: /images/products/grafana/dashboard-previews-on-grafana.png
    :alt: Dashboard previews on Grafana

Limitations
-----------
* Dashboard previews are not available for Hobbyist and Startup-1 plans.
* Before downgrading your service plan to Hobbyist or Startup-1, where dashboard previews are unavailable, you need first to disable it on the current service. 

.. seealso::
    For more information on Dashboard previews, see `Grafana documentation <https://grafana.com/docs/grafana/latest/search/dashboard-previews/>`_. 
