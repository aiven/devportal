Issue when enabling private access in terraform 
===============================================

When trying to set the Terraform argument ``private_access`` you may encounter the following error message:

.. Error::
   Error: Private only access to service ports cannot be enabled for the service's network

This error message is seen because the ``private_access`` argument is restricted to certain specific networks within Aiven's internal systems.

Projects that are in a VPC are **designed private by default**, so there is no need to set ``private_access`` in your Terraform resource, and any attempt to do so will result in the above error message.

The ``private_access`` argument in the Terraform provider Aiven is described in further detail at the `Terraform Registry <https://registry.terraform.io/providers/aiven/aiven/latest/docs/resources/redis>`_.
