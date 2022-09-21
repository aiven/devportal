Private access error when using VPC 
===================================

When trying to set the Terraform argument ``private_access`` you may encounter the following error message:

.. Error::
   Error: Private only access to service ports cannot be enabled for the service's network

This error message is seen because the ``private_access`` argument is restricted to certain specific networks within Aiven's internal systems.

Projects that are in a VPC are **designed private by default**, so there is no need to set ``private_access`` in your Terraform resource, and any attempt to do so will result in the above error message.

Refer to the official Terraform registry for `Aiven Provider for Terraform <https://registry.terraform.io/providers/aiven/aiven/latest>`_ to learn about the usage of ``private_access`` argument in further detail.
