Control access to content in your service
=========================================

This article shows you how to set up access control lists (ACL) for content in Aiven for OpenSearch services.

See the :doc:`related documentation <../concepts/access_control>` for more information on the permissions and patterns that are supported in ACL rules.

To define ACLs for your service:

1. Log in to the Aiven web console and select your OpenSearch service.

   
2. Click the **ACL** tab.

3. Switch on **Enable ACL**.

   This creates a set of rules that grant full access (``_*/admin``, ``*/admin``) for each existing service user.

   .. note::
      After you switch on ACL support, the service does not automatically add an ACL for new service users that you add. By default, access is denied.

   
4. If you want to enforce index rules in a limited fashion for requests that use the ``_mget``, ``_msearch``, and ``_bulk`` APIs for this service user, switch on **Enable extended ACLs**.
   
5. To define new ACLs:

   a. Click **Create user ACL**.
   b. Select the service user that you want to use.
   c. Click **Add rule**.
   d. Select the permission that you want to add.
   e. Enter the pattern for indexes that the ACL applies to.
   f. Add more rules to the ACL if required.
   g. Click **Create**.

