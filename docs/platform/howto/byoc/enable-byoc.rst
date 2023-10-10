Enable bring your own cloud (BYOC)
==================================

Enabling :doc:`the bring your own cloud (BYOC) feature </docs/platform/concepts/byoc>` allows you to :doc:`create custom clouds </docs/platform/howto/byoc/create-custom-cloud>` in your Aiven organization.

.. note::

   Enabling :doc:`the BYOC feature </docs/platform/concepts/byoc>` or creating custom clouds in your Aiven environment does not affect your existing organizations, projects, or services. This only makes the new BYOC capabilities available in your environment.

This article provides you with instructions on how to request enabling BYOC in your Aiven organization.

About enabling BYOC
-------------------

To be able to create custom clouds on the Aiven platform, first you need to enable the BYOC feature. `Aiven Console <https://console.aiven.io/>`_ offers a quick and easy way to set up a short call with the Aiven sales team to confirm your requirements and expectations. In the call, you make sure BYOC can address them and check your environment eligibility for the feature.

.. important::
    
   Before getting down to enabling BYOC, check the availability of the feature in :ref:`Who is eligible for BYOC <eligible-for-byoc>`, make sure you understand all the :ref:`limitations <byoc-enable-limitations>`, and meet all the :ref:`prerequisites <byoc-enable-prerequisites>`.

.. _byoc-enable-limitations:

Limitations
-----------

* You need at least the Priority tier of Aiven support services to be eligible for activating BYOC.
* BYOC is supported with the :ref:`standard deployment <byoc-deployment>` model only.
* Only organization's administrators can request enabling BYOC.

.. _byoc-enable-prerequisites:

Prerequisites
-------------

* Administrator's role for your Aiven organization
* Access to `Aiven Console <https://console.aiven.io/>`_
* Active account with your cloud provider

Enable BYOC
-----------

1. Log in to `Aiven Console <https://console.aiven.io/>`_ as an administrator.
2. Select the organization you want to use from the dropdown menu in the top right corner.
3. From the top navigation bar, select **Admin**.
4. From the left sidebar, select **Bring your own cloud**.
5. In the **Bring your own cloud** view, select **Contact us**.
6. In the **Contact us** window, enter your email address and country. Select the cloud provider you want to use, add any other information you think might be relevant, and select **Confirm**.

.. topic:: Result

   The scheduling assistant shows up so that you can schedule a short call with the Aiven sales team to proceed on your BYOC enablement request.

7. Using the scheduling assistant, select a date and time when you want to talk to our sales team to share your requirements and make sure BYOC suits your needs. Confirm the selected time, make sure you add the call to your calendar, and close the the scheduling assistant.
8. Join the scheduled call with our sales team to follow up with them on enabling BYOC in your environment.

.. topic:: Result
   
   If the call reveals BYOC addresses your needs and your environment is eligible for BYOC, the feature will be enabled for your Aiven organization.

Next steps
----------

With BYOC activated in your Aiven organization, it's possible for you to have custom clouds created:

* Either :ref:`by yourself using Aiven Console if the cloud provider you selected was AWS <create-cloud-aws>`
* Or :ref:`by the Aiven team if the cloud provider you selected was GCP or Azure <create-cloud-non-aws>`.

Related reading
---------------

* :doc:`Create a custom cloud </docs/platform/howto/byoc/create-custom-cloud>`
* :doc:`About bring your own cloud (BYOC) </docs/platform/concepts/byoc>`
* :doc:`Assign a project to your custom cloud </docs/platform/howto/byoc/assign-project-custom-cloud>`
* :doc:`Add customer's contact information for your custom cloud </docs/platform/howto/byoc/add-customer-info-custom-cloud>`
* :doc:`Rename your custom cloud </docs/platform/howto/byoc/rename-custom-cloud>`
