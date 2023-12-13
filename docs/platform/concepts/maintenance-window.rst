Service maintenance
===================

Maintenance window
------------------

The **maintenance window** is a time window during which the nodes behind Aiven services are switched to new upgraded version and, once the process is completed, the overall URI DNS name is pointed at the new location.

The upgrade is done during the maintenance window that you can set from the `Aiven Console <https://console.aiven.io/>`_, in service details page. During the maintenance window some services could have a minimal downtime period.

.. Note:: 
    For example, if there is a mandatory service updates for Apache Kafka®, the following `upgrade procedure <https://docs.aiven.io/docs/products/kafka/concepts/upgrade-procedure.html>`_ is executed.

Aiven service upgrades are performed in rolling forward style, which means that new service nodes are first created alongside with the older nodes one at a time, after which the old nodes are retired.

In case of **MySQL®**, **PostgreSQL®** and **Redis®*** the maintenance window usually lasts around several seconds. The downtime comes from old master stopping itself in a controlled manner and new master executing promotion sequence after this. Once the promotion is complete the old master node starts forwarding requests to the new master node so the service is accessible before DNS updates are propagated, though clients that end up reconnecting to the old master node will see additional disconnection once the old master is permanently retired.

In case of **Apache Kafka®** and **OpenSearch®** the service DNS address resolves to all the available service nodes. During an upgrade the DNS address changes to reflect the added and removed nodes. For example, during an `Apache Kafka upgrade procedure <https://docs.aiven.io/docs/products/kafka/concepts/upgrade-procedure.html>`_, a three node plan will have a minimum of three nodes available at all times during the whole upgrade operation. 

.. Note:: 

    While the DNS name remains the same, the IP address it points to, will change during a maintenance break. To know more about static IP addresses, check the :doc:`related documentation <static-ips>`.

.. note:: 
    Starting with Aiven for OpenSearch® versions 1.3.13 and 2.10, OpenSearch Dashboards will remain available during a maintenance update that also consists of version updates to your Aiven for OpenSearch service.

Maintenance updates
-------------------

Security updates, platform updates that affect reliability or stability of the service nodes, and quarterly patch updates are always mandatory. Other updates are initially optional. Advance notice is given for all updates. After optional updates have been available for six months, they become mandatory and are applied on the next week's maintenance window at the earliest. This means you have at least 7 days advance notice with exception of critical security updates. These critical updates are applied in the maintenance window of the current week. During service upgrades, maintenance updates are automatically applied and do not require any action from you.

You can view maintenance updates pending for your service using the following: 

- `Aiven Console <https://console.aiven.io/>`_ > **Service settings** page > **Service management** section 

- ``avn service get`` command in `Aiven CLI <https://docs.aiven.io/docs/tools/cli/service#avn-service-get>`_

- ``service`` endpoint in `Aiven REST API <https://api.aiven.io/doc/#tag/Service/operation/ServiceGet>`_

Periodic infrastructure updates
--------------------------------

There are regular maintenance updates for service nodes based on their age. Maintenance updates are scheduled automatically for services with nodes active for 180 days and more.

.. important::

   Periodic infrastructure updates are mandatory for all the services except for those with maintenance disabled.
