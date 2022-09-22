Create billing groups
=====================

With billing groups you can set up billing profiles to be used across multiple projects. A consolidated invoice is created for each billing group. To learn more about the key benefits of billing groups read the :doc:`related documentation <../concepts/billing-groups>`.


Billing groups and Aiven accounts
---------------------------------

An Aiven **Account** is the entry point for creating and managing billing groups:

- Within an account you can create one or more billing groups.
- You can assign an account's projects to a billing group and move projects from one billing group to another.
- You can set the :doc:`primary billing group </docs/platform/howto/use-billing-groups>`, which is the account's default billing group.

Aiven credits are available for all projects associated with the account. You can choose to apply the credits to a specific project within the account.

Create a new billing group
--------------------------

#. In the account that you want to add a billing group to, click **Billing**.

#. Click **Create billing group**.

#. Enter a name for the billing group and click **Continue**.

#. Enter the billing details. You can also copy these details from another billing group by selecting it from the list. Click **Continue**.

#. Select the projects that you want to add to this billing group. You can also skip this and add projects later. Click **Continue**.

#. Check the information on the **Summary**. You can edit the name, information, or projects by clicking **Edit**.

#. When you have confirmed everything is correct, click **Create**.

The costs of the projects assigned to this billing group will be consolidated into a single :doc:`invoice</docs/platform/howto/use-billing-groups>`.


