Control access to content in your service
=========================================

This article shows you how to set up access control lists (ACL) for content in Aiven for OpenSearch® services.

See the :doc:`related documentation <../concepts/access_control>` for more information on the permissions and patterns that are supported in ACL rules.

Switch on ACL support for your service
--------------------------------------

1. Log in to the `Aiven web console <https://console.aiven.io>`_ and select your OpenSearch service.

2. Click the **ACL** tab.

3. Switch on **Enable ACL**.

   This creates a set of rules that grant full access (``_*/admin``, ``*/admin``) for each existing service user.

   .. note::
      After you switch on ACL support, the service does not automatically add an ACL for new service users that you add. By default, access is denied.

   
4. If you want to enforce index rules in a limited fashion for requests that use the ``_mget``, ``_msearch``, and ``_bulk`` APIs for this service user, switch on **Enable extended ACLs**.


Define ACLs
-----------

When you have switched on ACL support in your service, define the new ACLs:

1. Log in to the `Aiven web console <https://console.aiven.io>`_ and select your OpenSearch service.
2. Click the **ACL** tab.
3. Click **Create user ACL**.
4. Select the service user that you want to use.
5. Click **Add rule**.
6. Select the permission that you want to add.
7. Enter the pattern for indexes that the ACL applies to.
8. Add more rules to the ACL if required.
9. Click **Create**.

