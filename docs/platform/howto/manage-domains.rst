Manage domains
===============

.. important:: 
    The domains feature is an :doc:`early availability feature </docs/platform/concepts/beta_services>`. To use it, enable the managed users :doc:`feature preview </docs/platform/howto/feature-preview>` in your user profile.

Verified domains let you manage users in your organization.

There are two ways you can verify a domain:

* by adding a DNS TXT record to the domain (recommended)
* by uploading an HTML file to your website

.. note::
    After adding a domain, your organization users will automatically become managed users. 

Add a domain using a DNS TXT record
-------------------------------------

1. In the organization you want to add a domain to, click **Admin**.

2. Click **Domains**.

3. Click **Add domain**.

4. Enter a **Domain name**.

5. In the **Verification method**, select **Add a DNS TXT record to your domain host**.

6. Click **Add domain**.

7. In the **Verification method** column, click **DNS TXT record**.

8. Copy the TXT record value.

9. In another browser tab or window, log in to your domain hosting provider.

10. Go to the DNS settings.

11. In the DNS settings for your domain provider, create a TXT record with the following:

    .. list-table::
          :header-rows: 1
          :align: left

          * - Field name
            - Value
          * - Name
            - ``_aiven-challenge.{your domain}``
          * - Record value 
            - The TXT record value you copied in the format ``token=<random_string>,expiry=never``
          * - Type
            - ``TXT``

12. In the Aiven Console, open the **Actions** menu and click **Verify**.

It can take up to 72 hours for your DNS records to update the domain to be verified. If the domain is still not verified after that time, you can retry it by repeating the last step.


Add a domain using an HTML file 
--------------------------------

#. In the organization that you want to add a domain to, click **Admin**.

#. Click **Domains**.

#. Click **Add domain**.

#. Enter a **Domain name**.

#. In the **Verification method**, select **Upload an HTML file to your website**.

#. Click **Add domain**.

#. In the **Verification method** column, click **HTML file upload**.

#. Download the HTML file.

#. Upload the HTML file to your website in the path ``/.well-known/aiven``.

#. In the Aiven Console, open the **Actions** menu and click **Verify**.


Remove a domain
-----------------

.. important::
    Removing a domain is an irreversible action.

#. In the organization that you want to remove a domain from, click **Admin**.

#. Click **Domains**.

#. Find the domain that you want to remove and open the **Actions** menu.

#. Click **Remove**.

#. Confirm you want to remove the domain by clicking **Remove domain**. 