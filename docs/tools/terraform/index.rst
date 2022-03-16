Aiven Terraform provider
========================

    Terraform is an open-source infrastructure as code software tool that provides a consistent CLI workflow to manage hundreds of cloud services. Terraform codifies cloud APIs into declarative configuration files. `Terraform website <https://www.terraform.io/>`_.

With Aiven's Terraform Provider you can manage all your services programmatically.

See the `official documentation <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ to learn about all the possible services and resources and the `GitHub repository <https://github.com/aiven/terraform-provider-aiven>`_ for reporting issues and contributing.

.. caution::
  Recreating stateful services with Terraform will possibly delete the service and all its data before creating it again. Whenever the Terraform plan indicates that a service will be deleted or replaced, a catastrophic action is possibly about to happen.

  Some properties, like project and the resource name, cannot be changed and it will trigger a resource replacement.

  To avoid any issues, please set the termination_protection property to true on all production services, it will prevent Terraform to remove the service until the flag is set back to false again. While it prevents a service to be deleted, any logical databases, topics or other configurations may be removed even when this section is enabled. Be very careful!

Getting started
---------------

Please refer to the :doc:`getting started guide <get-started>` for your first Terraform project.

.. panels::

    💻 :doc:`howto`

    ---

    📖 :doc:`reference`

    ---

    👨‍🍳 :doc:`reference/cookbook`  

Learn more
----------
Check out these resources to learn more about Terraform and our Provider:

* `Learn Terraform <https://learn.hashicorp.com/collections/terraform/aws-get-started>`_
* `Aiven Terraform Provider documentation <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_

Get involved
------------
If you have any comments or want to contribute to the tool, please join us on the `GitHub repository <https://github.com/aiven/terraform-provider-aiven>`_.
