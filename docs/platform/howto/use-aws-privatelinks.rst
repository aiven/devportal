Use AWS PrivateLink with Aiven services
=======================================

.. important::

    AWS PrivateLink is a :doc:`limited availability feature </docs/platform/concepts/beta_services>`, which you can request from the sales team (sales@Aiven.io) or your account manager. During the limited availability stage, you can use the feature at no cost. If you want to continue using AWS PrivateLink after it reaches general availability, you'll be billed according to the latest applicable price.

AWS `PrivateLink <https://aws.amazon.com/privatelink/>`__ brings Aiven
services to the selected virtual private cloud (VPC) in your AWS
account. In a traditional setup that uses :ref:`VPC peering <platform_howto_setup_vpc_peering>`, traffic is routed through an AWS VPC peering connection to your Aiven
services. With PrivateLink, you can create a VPC endpoint to your own
VPC and access an Aiven service from that. The VPC endpoint creates
network interfaces (NIC) to the subnets and availability zones that you
choose and receives the private IP addresses that belong to the IP range
of your VPC. The VPC endpoint is routed to your Aiven service located in
one of Aiven's AWS accounts.

You can enable PrivateLink for Aiven services located in project VPC.
Before you can set up AWS PrivateLink, :ref:`create a VPC <platform_howto_setup_vpc_peering>` and launch the
services that you want to connect to that VPC. As there is no network
routing between the VPC, you can use any private IP range for the VPC,
unless you also want to connect to the project VPC using VPC peering
connections. This means that overlaps in the IP range are not an issue.

You can use either the `Aiven Console <https://console.aiven.io>`__
or the :doc:`Aiven CLI </docs/tools/cli>` to set up
AWS PrivateLink. You also need the AWS CLI to create a VPC endpoint.

**Note:** Aiven for Apache Cassandra® and Aiven for M3 services do not
currently support AWS PrivateLink.

#. | Create an AWS PrivateLink resource on the Aiven service:
   
   | The Amazon Resource Name (ARN) for the principals that are allowed
     to connect to the VPC endpoint service and the AWS network load
     balancer requires your Amazon account ID. In addition, you can set
     the access scope for an entire AWS account, a given user account,
     or a given role. Only give permissions to roles that you trust, as
     an allowed role can connect from any VPC.

   -  Using the Aiven CLI, run the following command including your AWS
      account ID, the access scope, and the name of your Aiven service:

      ::

         $ avn service privatelink aws create --principal arn:aws:iam::$AWS_account_ID:$access_scope $Aiven_service_name

      For example:

      ::

         $ avn service privatelink aws create --principal arn:aws:iam::012345678901:user/mwf my-kafka

   -  Using `Aiven Console <https://console.aiven.io>`__:

      #. Log in to `Aiven Console <https://console.aiven.io>`__ and select the service that you
         want to use.

      #. On the **Overview** page of your service, select **Network** from the sidebar.

      #. On the **Network** page, select **Create Privatelink** .

      #. In the **Create Privatelink** window, enter the Amazon Resource Names (ARN) for the principals that you want to use, and select **Create** .

   | This creates an AWS network load balancer dedicated to your Aiven
     service and attaches it to an AWS VPC endpoint service that you can
     later use to connect to your account's VPC endpoint.

   | The PrivateLink resource stays in the initial ``creating`` state
     for up to a few minutes while the load balancer is being launched.
     After the load balancer and VPC endpoint service have been created,
     the state changes to ``active`` and the ``aws_service_id`` and
     ``aws_service_name`` values are set.

#. In the AWS CLI, run the following command to create a VPC endpoint:

   ::

      $ aws ec2 --region eu-west-1 create-vpc-endpoint --vpc-endpoint-type Interface --vpc-id $your_vpc_id --subnet-ids $space_separated_list_of_subnet_ids --security-group-ids $security_group_ids --service-name com.amazonaws.vpce.eu-west-1.vpce-svc-0b16e88f3b706aaf1

   | 
   | Replace the ``--service-name`` value with the value shown next to
     **Network** > **AWS service name** in `Aiven Console <https://console.aiven.io>`__ or by
     running the following command in the Aiven CLI:

   ::

      $ avn service privatelink aws get aws_service_name

   | 
   | Note that for fault tolerance, you should specify a subnet ID for
     each availability zone in the region. The security groups determine
     the instances that are allowed to connect to the endpoint network
     interfaces created by AWS into the specified subnets.

   | Alternatively, you can create the VPC endpoint in `Aiven Console <https://console.aiven.io>`__ under **Integration endpoints** > **Add new endpoint** . See the `AWS documentation <https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint>`__ for details.

   | **Note:** For Aiven for Apache Kafka® services, the security group
     for the VPC endpoint must allow ingress in the port range
     ``10000-31000`` to accommodate the pool of Kafka broker ports used
     in our PrivateLink implementation.
   
   | It takes a while before the endpoint is ready to use as AWS
     provisions network interfaces to each of the subnets and connects
     them to the Aiven VPC endpoint service. Once the AWS endpoint state
     changes to ``available`` , the connection is visible in Aiven.

#. | Enable PrivateLink access for Aiven service components:
   
   | You can control each service component separately - for example,
     you can enable PrivateLink access for Kafka while allowing Kafka
     Connect to connect via VPC peering connections only.

   -  In the Aiven CLI, set
      ``user_config.privatelink_access.<service component>`` to ``true``
      for the components that you want to enable. For example:

      ::

         $ avn service update -c privatelink_access.kafka=true $Aiven_service_name
         $ avn service update -c privatelink_access.kafka_connect=true $Aiven_service_name
         $ avn service update -c privatelink_access.kafka_rest=true $Aiven_service_name
         $ avn service update -c privatelink_access.schema_registry=true $Aiven_service_name

   -  In `Aiven Console <https://console.aiven.io>`__:

      #. Go to the **Overview** page of your service, and scroll down to **Advanced
         configuration**.

      #. Select **Change**, add the components that you
         want, and switch them on.

         .. image:: /images/platform/howto/use-aws-privatelink_image1.png
            :alt: Aiven Console private link configuration

      #. Select **Save advanced configuration** .

   It takes a couple of minutes before connectivity is available after
   you enable a service component. This is because AWS requires an AWS
   load balancer behind each VPC endpoint service, and the target rules
   on the load balancer for the service nodes need at least two
   successful heartbeats before they transition from the ``initial``
   state to ``healthy`` and are included in the active forwarding rules of the load balancer.

.. _h_b6605132ff:

Acquire connection information
------------------------------

.. _one-connection:

One AWS PrivateLink connection
''''''''''''''''''''''''''''''

Once you have enabled PrivateLink access for a service component, a
switch for the ``privatelink`` access route appears under **Connection
information** on the **Overview** page in `Aiven Console <https://console.aiven.io>`__. The ``host`` -
and for some service components such as Kafka, ``port`` - values differ
from the default ``dynamic`` access route that is used to connect to the
service. You can use the same credentials with any access route.

Multiple AWS PrivateLink connections
''''''''''''''''''''''''''''''''''''

If you have more than one AWS PrivateLink connection, you can get connection information for the first connection as described in :ref:`One AWS PrivateLink connection <one-connection>` from `Aiven Console <https://console.aiven.io>`__. For connection information on the remaining connections, you need to use CLI.

Each endpoint (connection) has PRIVATELINK_CONNECTION_ID, which you can check using the ``avn service privatelink aws connection list SERVICE_NAME`` command.

* To acquire SSL connection information for your service using AWS PrivateLink, run the following command:

.. code-block:: bash

   avn service connection-info UTILITY_NAME SERVICE_NAME -p PRIVATELINK_CONNECTION_ID

.. topic:: Where

  * UTILITY_NAME is ``kcat``, for example
  * SERVICE_NAME is ``kafka-12a3b4c5``, for example
  * PRIVATELINK_CONNECTION_ID is ``plc39413abcdef``, for example

* To acquire connection information for your service using AWS PrivateLink with SASL enabled, run the following command:

.. code-block:: bash

   avn service connection-info UTILITY_NAME SERVICE_NAME -p PRIVATELINK_CONNECTION_ID -a sasl

.. topic:: Where

  * UTILITY_NAME is ``kcat``, for example
  * SERVICE_NAME is ``kafka-12a3b4c5``, for example
  * PRIVATELINK_CONNECTION_ID is ``plc39413abcdef``, for example

.. note::

   SSL certificates and SASL credentials are the same for all the connections.

.. _h_2a1689a687:

Update the allowed principals list
----------------------------------

To change the list of AWS accounts or IAM users or roles that are
allowed to connect a VPC endpoint:

-  Use the ``update`` command of the Aiven CLI:

   ::

      # avn service privatelink aws update --principal arn:aws:iam::$AWS_account_ID:$access_scope $Aiven_service_name

   | **Note:** When you add an entry, also include the ``--principal`` arguments for existing entries.

-  In `Aiven Console <https://console.aiven.io>`__:

   #. Select your service from the **Services** page.

   #. Select **Network** from the sidebar.

   #. In the **Network** page, select **Edit principals**.

   #. Enter the principals that you want to include.

   #. Select **Save** .

.. _h_8de68d5894:

Deleting a privatelink connection
---------------------------------

-  Using the Aiven CLI, run the following command:

   ::

      $ avn service privatelink aws delete $Aiven_service_name

   ::

      AWS_SERVICE_ID             AWS_SERVICE_NAME                                        PRINCIPALS                         STATE
      ========================== ======================================================= ================================== ========
      vpce-svc-0b16e88f3b706aaf1 com.amazonaws.vpce.eu-west-1.vpce-svc-0b16e88f3b

-  Using `Aiven Console <https://console.aiven.io>`__:

   #. Select **Network** from the sidebar on your service's page.

   #. Select the trash can icon on the right of the **AWS PrivateLink** row.

   #. Select **Confirm** .

This deletes the AWS load balancer and VPC service endpoint.
