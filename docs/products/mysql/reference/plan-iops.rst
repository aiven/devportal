IOPS capability of plans
========================

When creating or updating an Aiven service, you can choose the plan, driving the amount of resources available. The type of virtual machines created depends by the cloud provider chosen, and each one has different IOPS (Input/output Operations Per Second) limits. This reference provides the mapping between the common plans in Aiven for MySQL and the related virtual machine types in the major clouds.

Hobbyist
''''''''

.. list-table::
    :header-rows: 1

    * - Plan
      - AWS
      - GCP
      - Azure
    * - **Hobbyist**
      - ``t3.micro``
      - ``g1-small``
      - not available


Startup
'''''''

.. list-table::
    :header-rows: 1

    * - Plan
      - AWS
      - GCP
      - Azure
    * - **startup-4**
      - ``t3.medium``
      - ``e2-medium``
      - ``standard_d1_v2``
    * - **startup-8**
      - ``m5.large``
      - ``n1-standard-2``
      - ``standard_d2_v2``
    * - **startup-16**
      - ``t3.xlarge``
      - ``n1-standard-4``
      - ``standard_d3_v2``     
    * - **startup-32**
      - ``t3.2xlarge``
      - ``n1-standard-8``
      - ``standard_d4_v2`` 
    * - **startup-64**
      - ``m5.4xlarge``
      - ``n1-standard-16``
      - ``standard_l8s_v2`` 
    * - **startup-120**
      - ``m5.8xlarge``           
      - custom type             
      - ``standard_l16s_v2``
    * - **startup-190**
      - ``m5.12xlarge``          
      - custom type             
      - not available
    * - **startup-240**
      - ``m5.16xlarge``
      - ``n1-standard-64``          
      - ``standard_l32s_v2``
    * - **startup-360**
      - ``m5.24xlarge``        
      - ``n2d-standard-96``         
      - not available

Business and premium
'''''''''''''''''''''

The cloud instance types in the Business and premium plans are equal to the startup ones. The difference is the cluster size with 2 nodes for Business plans and 3 node high availability set for Premium plans.

Single node IOPS capacity
'''''''''''''''''''''''''

The single node IOPS limitation detail can be found in the cloud vendor dedicated documentation:

AWS: https://aws.amazon.com/ec2/instance-types/

GCP: https://cloud.google.com/compute/docs/general-purpose-machines

Azure: https://docs.microsoft.com/en-us/azure/virtual-machines/sizes-previous-gen

The instance types can vary to other equivalent types in different regions.

.. note:: For custom plans, if you want to know the node types for IOPS limitation, please contact support team at ``support@aiven.io``.