Upgrade the Aiven Terraform Provider from v1 to v2
==================================================

Version 2 of the Aiven Terraform Provider was released in `October of
2020 <https://aiven.io/blog/aiven-terraform-provider-v2-release>`__.
This article will walk you through upgrading from Aiven Terraform Provider v1 to v2, including some tips if you are upgrading Terraform as well (0.12 or later).

To handle the various versions of Terraform, we will be using the ``tfenv``
tool (`see the project page <https://github.com/tfutils/tfenv>`_), but you can use
direct releases from Hashicorp if you prefer.

Major changes in v2
'''''''''''''''''''

Aiven Terraform Provider has a `detailed changelog <https://github.com/aiven/terraform-provider-aiven/blob/master/CHANGELOG.md>`_ but the main additions in v2 are:

-  Billing Groups have been introduced instead of needing to provide
   Card ID
-  Work is being done to deprecate ``aiven_service`` in order to support
   individual service configuration better, using ``aiven_kafka`` for
   example
-  New services are available in the updated provider, such as
   ``aiven_flink`` and ``aiven_opensearch``.

Upgrade Aiven Terraform provider
''''''''''''''''''''''''''''''''

Update the Aiven Terraform Provider by
editing the providers block of your script to include the latest version of
the Aiven Terraform Provider (v2.3.1 at the time of writing)::

    terraform {
      required_providers {
        aiven = {
          source = "aiven/aiven"
          version = "2.3.1"
        }
      }
    }

Upgrade Terraform
'''''''''''''''''

We recommend keeping your Terraform version up to date.
If you have v0.12 then follow the steps below.
Users with 0.13 (and the related syntax update) can skip the next section.

Upgrade Terraform 0.12 to 0.13
''''''''''''''''''''''''''''''

Between v0.12 and v0.13, the syntax of Terraform files changed. If you have the older syntax,
follow these steps to get the updated syntax:


1. Upgrade your modules first by installing Terraform v0.13.x (i.e. 0.13.7):
``tfenv install 0.13.7 && tfenv use 0.13.7`` and then using ``0.13upgrade`` tool.

2. Update ``required_version`` from ``>= 0.12`` to ``>= 0.13`` in the requirements block.

3. Update the existing state file, by running:
``terraform state replace-provider registry.terraform.io/-/aiven registry.terraform.io/aiven/aiven``
you will replace old Aiven terraform provider references to the new format.

4. Run ``terraform 0.13upgrade`` to see any additional fixes recommended by Hashicorp.
If you are using more providers than Aiven provider you most likely need to upgrade them as well.
More information `here <https://www.terraform.io/upgrade-guides/0-13.html>`__.

5. Run ``terraform init -upgrade``

.. image:: /images/tools/terraform/terraform-upgrade.jpg
   :alt: Screenshot of the upgrade command in action

You may see warnings or errors like the above, these will point towards
changes made between the release you are running and the latest release.

The warnings will provide recommendations on the changes to make and you
can get more information using our
`docs <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`__.

Now we can remove the old Terraform folder ``rm -rf ~/.terraform.d``.

6. As the last step run ``terraform plan``

Upgrade Terraform from 0.13 or later
''''''''''''''''''''''''''''''''''''

Any version above 0.13 can be upgraded to latest without any special steps.

.. note::
  If you are using Aiven Terraform provider v1 with Terraform 0.14 ``dev_overrides`` (see `<https://www.terraform.io/cli/config/config-file#provider-installation>`__ )
  you will need to add Aiven provider to the ``exclude`` block or remove ``dev_overrides`` completely.

1. Use ``tfenv`` to get the latest version (1.0.10 at the time of writing) ``tfenv install latest && tfenv use latest``

2. Run ``terraform init -upgrade``

3. Run ``terraform plan``

Update to service specific resource syntax
''''''''''''''''''''''''''''''''''''''''''

V2 of the Aiven Terraform Provider moves away from using ``aiven_service`` as a resource, and instead provides specific service resources such as ``aiven_kafka``. Since we probably don't want to destroy the existing resources and making new ones, this guide will help you perform the migration safely.

.. warning::
    Since ``aiven_service`` and the new services such as ``aiven_kafka`` are different kinds of resources, simply rewriting the code would cause destructive actions. These steps will preserve your resources.

Please also note that running ``terraform state mv <a> <b>`` is not recommended because these are different resource types.

To safely make this change you will:

-  Change the code first
-  Backup your Terraform state file (if available), just in case of potential rollback
-  Remove old resource from the state
-  Import already existing service to the Terraform state.

1. To change from the old ``aiven_service`` to the new ``aiven_kafka``
resource, the resource type should be changed, and the old ``service_type``
field removed. Any references to ``aiven_service.kafka.*`` should be updated to instead read ``aiven_kafka.kafka.*`` instead. Here's an example showing the update in action::

    - resource "aiven_service" "kafka" {
    -    service_type            = "kafka"
    + resource "aiven_kafka" "kafka" {
        ...
    }
    resource "aiven_service_user" "kafka_user" {
      project      = var.aiven_project_name
    -  service_name = aiven_service.kafka.service_name
    +  service_name = aiven_kafka.kafka.service_name
      username     = var.kafka_user_name
    }


2. Check the current state of the world::

    terraform state list | grep kf

3. Remove the service from Terraform's control, and write a backup of the state into your local directory::

    terraform state rm -backup=./ aiven_service.kafka

.. tip::
    Use the ``-dry-run`` flag to see this change before it is actually made

4. Add the service back to Terraform by importing it as a new service with the new service type::

    terraform import aiven_kafka.kafka demo-project/existing-kafka

5. Check that the import is going to run as you expect::

    terraform plan

6. Finally, go ahead and apply the new configuration::

    terraform apply

Further reading
'''''''''''''''

There are examples of migrating each of the available service types on the
`Aiven examples repository <https://github.com/aiven/aiven-examples/tree/master/terraform>`__
on GitHub.
