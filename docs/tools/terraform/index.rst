Aiven Terraform provider
========================

With Aiven's `Terraform <https://www.terraform.io>`_ provider, you can use an open-source infrastructure as code software tool to declare and manage your cloud services.

See the `Aiven Terraform provider documentation <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ to learn about the services and resources,and visit the `GitHub repository <https://github.com/aiven/terraform-provider-aiven>`_ to report any issues or contribute to the project.

.. caution::

  Recreating stateful services with Terraform will possibly delete the service and all its data before creating it again. Whenever the Terraform plan indicates that a service will be deleted or replaced, a catastrophic action is possibly about to happen.

  Some properties, like project and the resource name, cannot be changed and it will trigger a resource replacement.

  We recommend you set the ``termination_protection`` property to true on all production services, it will prevent Terraform from removing the service. Be aware that any logical databases, topics or other configurations may be removed even when this setting is enabled. Be very careful!

Getting started
---------------

Check out the :doc:`getting started guide <get-started>` for your first Terraform project.

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
