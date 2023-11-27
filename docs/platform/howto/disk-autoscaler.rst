Scale your Aiven service disks automatically
============================================

Discover the service disk autoscaler and its capabilities. Find out how it works and how to use it with your Aiven for service.

.. topic:: Pricing

   Costs of using disk autoscaler depend on your service type and plan. You don't pay a fixed amount monthly but you're charged based on your actual usage. For information on the costs of using disk autoscaler, check the same for dynamic disk sizing (DDS) in `Aiven Plans and Pricing <https://aiven.io/pricing?product=kafka>`_ or contact us at sales@Aiven.io.

Why use disk autoscaling
------------------------

Service disk autoscaler increases disk storage capacity automatically when the disk is running out of space. Disk autoscaling allows you to improve the cost-efficiency of operating your Aiven services: you can start with a relatively small-sized disk and only have it scaled up when needed with no risk of running out of disk space at any point.

How it works
------------

There are a few steps illustrating how disk autoscaler works:

1. You create an disk autoscaler integration endpoint in your Aiven project setting the maximum additional storage at the same time.
2. You enable a disk autoscaler integration for your service using the new disk autoscaler integration endpoint.
3. From that point onward, the evaluation of disk space availability for your service is done every 30 seconds.
4. When disk storage consumption reaches the threshold for a specific service, disk autoscaler increases available storage space by 10% every time taking the currently-used service plan as a baseline.

.. topic:: AUTOSCALE THRESHOLDS PER SERVICE TYPE

   The threshold at which disk autoscaling is triggered is a percentage of the available disk storage capacity and depends on a service type:

   * Aiven for Apache Cassandra®: 35% of the available disk storage capacity
   * Aiven for OpenSearch®: 75% of the available disk storage capacity
   * All the other Aiven service types: 85% of the available disk storage capacity

Prerequisites
-------------

* Aiven organization, project, and service up and running
* :doc:`Dynamic disk sizing (DDS) </docs/platform/concepts/dynamic-disk-sizing>` supported for the service plan and the cloud hosting the service
* Role of the operator for your Aiven organization, project, and service
* Depending on what interface you'd like to use for interacting with disk autoscaler:
    * Access to `Aiven Console <https://console.aiven.io/>`_
    * `Aiven API <https://api.aiven.io/doc/>`_
    * :doc:`Aiven CLI client </docs/tools/cli>`

Enable disk autoscaler
----------------------

To enable disk autoscaling on your Aiven service, you need to create an autoscaler integration enpoint and enable autoscaler integration with your service using the new enpoint. You can set up disk autoscaling in `Aiven Console <https://console.aiven.io/>`_, using Aiven API, or Aiven CLI client.

Enable in Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~

Create an autoscaler endpoint
'''''''''''''''''''''''''''''

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and navigate to a desired organization and project.
2. On the **Services** page of your project, select **Integration endpoints** from the sidebar.
3. On the **Integration endpoints** page, select **Disk autoscaler** > **Add new endpoint**.
4. In the **Create new autoscaler endpoint** window, enter an endpoint name, specify a maximum additional disk storage that you want to allow for disk autoscaling purposes, and select **Create**.

Enable on a service
'''''''''''''''''''

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and navigate to a desired organization, project, and service.
2. On the **Overview** page of your service, select **Integrations** from the sidebar.
3. On the **Integrations** page, navigate to **External integrations** and select **Disk autoscaler**.
4. In the **Autoscaler integration** window, select the newly-created autoscaler integration endpoint from the dropdown manu and select **Enable**.

Enable with Aiven API
~~~~~~~~~~~~~~~~~~~~~

To enable disk autoscaler on your service via `Aiven API <https://api.aiven.io/doc/>`_, call the
`ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ endpoint passing ``{"service disk autoscaler": {"enabled": true}}`` in the ``user_config`` object.

Enable with Aiven CLI
~~~~~~~~~~~~~~~~~~~~~

You can use the :doc:`Aiven CLI client </docs/tools/cli>` to enable disk autoscaler for your service by running the following command:

.. code-block:: bash

   avn service update -c service disk autoscaler.enabled=true SERVICE_NAME

Configure disk autoscaler
-------------------------

After enabling disk autoscaler, any time later you can update the maximum additional disk storage allowed for autoscaling purposes. You can use `Aiven Console <https://console.aiven.io/>`_, Aiven API, or Aiven CLI to do that.

Configure in Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and navigate to a desired organization and project.
2. On the **Services** page of your project, select **Integration endpoints** from the sidebar.
3. On the **Integration endpoints** page, select **Disk autoscaler**, find your endpoint on the list of the existing autoscaler endpoints, select the **Edit endpoint** icon.
4. In the **Edit endpoint** window, specify a new value for the maximum additional disk storage to be allowed for autoscaling, and select **Update**.

Configure with Aiven API
~~~~~~~~~~~~~~~~~~~~~~~~

You can use `Aiven API <https://api.aiven.io/doc/>`_ to configure disk autoscaler on your service. Call the
`ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ endpoint passing desired service disk autoscaler parameters in the ``user_config`` object.

Configure with Aiven CLI
~~~~~~~~~~~~~~~~~~~~~~~~

You can use the :doc:`Aiven CLI client </docs/tools/cli>` to configure disk autoscaler on your service by running the following command:

.. code-block:: bash

   avn service update -c service disk autoscaler.PARAMETER_NAME=PARAMETER_VALUE SERVICE_NAME

Disable disk autoscaler
-----------------------

To disable disk autoscaling on your Aiven service, you need to disconnect the service from the autoscaler integration enpoint. You can also delete the integration enpoint itself if you don't need it for future purposes. You can disable disk autoscaling in `Aiven Console <https://console.aiven.io/>`_, using Aiven API, or Aiven CLI client.

Disable in Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~~

Disable on a service
''''''''''''''''''''

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and navigate to a desired organization, project, and service.
2. On the **Overview** page of your service, select **Integrations** from the sidebar.
3. On the **Integrations** page, find your autoscaler service integration at the top, select the **Actions** (**...**) menu > **Disconnect**.
4. In the **Disconnet service integration** window, select **Disconnect**.

Delete an autoscaler endpoint
'''''''''''''''''''''''''''''

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and navigate to a desired organization and project.
2. On the **Services** page of your project, select **Integration endpoints** from the sidebar.
3. On the **Integration endpoints** page, select **Disk autoscaler**, find your endpoint on the list of the existing autoscaler endpoints, select the **Delete endpoint** icon and **Delete** in the **Confirmation** window.

Disable with Aiven API
~~~~~~~~~~~~~~~~~~~~~~

You can use `Aiven API <https://api.aiven.io/doc/>`_ to disable disk autoscaler on your service. Call the
`ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ endpoint passing ``{"service disk autoscaler": {"enabled": false}}`` in the ``user_config`` object.

Disable with Aiven CLI
~~~~~~~~~~~~~~~~~~~~~~

You can use the :doc:`Aiven CLI client </docs/tools/cli>` to disable disk autoscaler on your service by running the following command:

.. code-block:: bash

   avn service update -c service disk autoscaler.enabled=false SERVICE_NAME

Related reading
---------------

:doc:`Dynamic disk sizing (DDS) </docs/platform/concepts/dynamic-disk-sizing>`
