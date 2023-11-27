Scale your Aiven service disks automatically
============================================

Discover the service disk autoscaler and its capabilities. Find out it works and how to use it with your Aiven for service.

About disk autoscaling
----------------------

.. seealso::

   For more information on service disk autoscaler, check.

Why use it
----------


How it works
------------

.. topic:: Flow of actions

.. seealso::

   For more information on how service disk autoscaler works, check

Prerequisites
-------------

* Aiven organization, project, and service (Aiven for PostgreSQL)
* Depending on what interface you'd like to use for interacting with service disk autoscaler, you might need the following:
    * Access to `Aiven Console <https://console.aiven.io/>`_
    * SQL
    * `Aiven API <https://api.aiven.io/doc/>`_
    * :doc:`Aiven CLI client </docs/tools/cli>`

Enable service disk autoscaler
-------------------

You can enable the extension in `Aiven Console <https://console.aiven.io/>`_, using Aiven API, or Aiven CLI client.

Enable in Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   In `Aiven Console <https://console.aiven.io/>`_, you can enable service disk autoscaler at the service level only. To enable the extension on a database or for a user, you need to use SQL.

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and navigate to a desired organization, project, and service.
2. On the **Overview** page of your service, navigate to **Advanced configuration** > **Configure** > **Add configuration options**.
3. Find the **service disk autoscaler.enabled** parameter, set it to **true**, and select **Save configuration**.

Enable with Aiven API
~~~~~~~~~~~~~~~~~~~~~

You can use `Aiven API <https://api.aiven.io/doc/>`_ to enable service disk autoscaler on your service. Call the
`ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ endpoint passing ``{"service disk autoscaler": {"enabled": true}}`` in the ``user_config`` object.

Enable with Aiven CLI
~~~~~~~~~~~~~~~~~~~~~

You can use the :doc:`Aiven CLI client </docs/tools/cli>` to enable service disk autoscaler for your service by running the following command:

.. code-block:: bash

   avn service update -c service disk autoscaler.enabled=true SERVICE_NAME

Configure service disk autoscaler
----------------------

service disk autoscaler is pre-configured with default settings but you can modify its configuration parameters in `Aiven Console <https://console.aiven.io/>`_, using Aiven API, or Aiven CLI.

You might want to configure the following parameters:

* ``service disk autoscaler.enabled`` (to enable or disable the service disk autoscaler extension)
* ``service disk autoscaler.track_pg_catalog`` (to enable or disable service disk autoscaler on pg_catalog)
* ``service disk autoscaler.sample_rate`` (to set the granularity of service disk autoscaler analysis and statistics returned)
    * Allowed values: ``0`` - ``1``, where ``1`` means analysis and statistics on every single query, and ``0`` means there are no queries analysed.
    * Default value: ``1/max_connections``
* ``service disk autoscaler.track_constants`` (to enable or disable service disk autoscaler on constants)

.. topic:: Sample service disk autoscaler configuration
   
   .. code-block:: bash

      service disk autoscaler.enabled = on
      service disk autoscaler.sample_rate = 0.1

.. seealso::

   For more confuguration options, check `powa-team's service disk autoscaler configuration <https://github.com/powa-team/service disk autoscaler>`_.

Configure in Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   In `Aiven Console <https://console.aiven.io/>`_, you can configure service disk autoscaler at the service level only. To configure the extension on a database or for a user, you need to use SQL.

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and navigate to a desired organization, project, and service.
2. On the **Overview** page of your service, navigate to **Advanced configuration** > **Configure** > **Add configuration options**.
3. Find a desired service disk autoscaler parameter (all prefixed with ``service disk autoscaler``), set its value as needed, and select **Save configuration**.

Configure with Aiven API
~~~~~~~~~~~~~~~~~~~~~~~~

You can use `Aiven API <https://api.aiven.io/doc/>`_ to configure service disk autoscaler on your service. Call the
`ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ endpoint passing desired service disk autoscaler parameters in the ``user_config`` object.

Configure with Aiven CLI
~~~~~~~~~~~~~~~~~~~~~~~~

You can use the :doc:`Aiven CLI client </docs/tools/cli>` to configure service disk autoscaler on your service by running the following command:

.. code-block:: bash

   avn service update -c service disk autoscaler.PARAMETER_NAME=PARAMETER_VALUE SERVICE_NAME

Disable service disk autoscaler
--------------------

You can disable the extension in `Aiven Console <https://console.aiven.io/>`_, using Aiven API, or Aiven CLI.

Disable in Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   In `Aiven Console <https://console.aiven.io/>`_, you can disable service disk autoscaler at the service level only, which deactivates the extension globally for the whole service: all the databases and user roles in this service. To disable the extension on a particular database or for a specific user only, you need to use SQL.

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and navigate to a desired organization, project, and service.
2. On the **Overview** page of your service, navigate to **Advanced configuration** > **Configure** > **Add configuration options**.
3. Find the **service disk autoscaler.enabled** parameter, set it to **false**, and select **Save configuration**.

Disable with Aiven API
~~~~~~~~~~~~~~~~~~~~~~

You can use `Aiven API <https://api.aiven.io/doc/>`_ to disable service disk autoscaler on your service. Call the
`ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ endpoint passing ``{"service disk autoscaler": {"enabled": false}}`` in the ``user_config`` object.

Disable with Aiven CLI
~~~~~~~~~~~~~~~~~~~~~~

You can use the :doc:`Aiven CLI client </docs/tools/cli>` to disable service disk autoscaler on your service by running the following command:

.. code-block:: bash

   avn service update -c service disk autoscaler.enabled=false SERVICE_NAME

Related reading
---------------
