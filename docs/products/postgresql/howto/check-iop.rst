IOP capability of plans
-----------------------

This article will explain what is the typical IOP capability used for common plans in pg:

Hobbyist
''''''''

==============================     ================     ===================     ================
  Plan                                AWS                  GCP                     Azure
==============================     ================     ===================     ================
 Hobbyist                            t3.micro             g1-small                 not available                
==============================     ================     ===================     ================


Startup
'''''''

==============================     ================     ===================     ================
  Plan                                AWS                  GCP                     Azure
==============================     ================     ===================     ================
 Startup-4                          t3.medium            e2-medium               standard_d1_v2                
 Startup-8                          m5.large             e2-standard-2           standard_d2_v2
 startup-16                         i3.large             e2-standard-2           standard_d3_v2
 startup-32                         i3.xlarge            n1-standard-8           standard_d4_v2
 startup-64                         i3.2xlarge           n1-standard-16          standard_l8s_v2
 startup-120                        i3.4xlarge           custom type             standard_l16s_v2
 startup-190                        m5.12xlarge          custom type             not available
 startup-240                        i3.8xlarge           n1-standard-64          standard_l32s_v2
 startup-360                        m5ad.24xlarge        n2d-standard-96         not available
 startup-512                        not available        n2d-standard-128        not available
 startup-512 compute-optimized      m5.2xlarge           not available           not available
 startup-512 storage-optimized      m5.large             not available           not available
 startup-512 io-optimized           i3.large             not available           not available
 startup-896                        not available        n2d-standard-224        not available
==============================     ================     ===================     ================


Business and premium
'''''''''''''''''''''

The VM type is similar as startup while with 2 and 3 node high availability set.

Node capacity
'''''''''''''

The IOP limitation can be found as per:

AWS: https://aws.amazon.com/ec2/instance-types/

GCP: https://cloud.google.com/compute/docs/general-purpose-machines

Azure: https://docs.microsoft.com/en-us/azure/virtual-machines/sizes-previous-gen

While the VM type may vary because of different regions to another equivalent type.

.. note:: For custom plans, if you want to know the node types for IOP limitation, please contact support team.