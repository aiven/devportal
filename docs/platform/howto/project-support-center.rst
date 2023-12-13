Support 
========

The Basic support tier is provided to all customers on paid service plans. Aiven offers three additional support tiers with faster response times, phone support, and other services. For more information about the tiers, check out the `Aiven support details page <https://aiven.io/support-services>`_ or contact sales@Aiven.io. 

For other services included in your support tier - such as business reviews or disaster recovery planning - contact the sales team at sales@Aiven.io. If you are using a free service, you can ask questions in the `Aiven Community Forum <https://aiven.io/community/forum/>`_. 

The Aiven service level agreement (SLA) is available on `the SLA page <https://aiven.io/sla>`_. Custom SLAs are available for premium plans. Contact the sales team at sales@Aiven.io for more details.


.. _upgrade-support-tier:

Upgrade your support tier
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have questions or want to downgrade your support tier, contact your account team. 

To upgrade your organization's support tier in the `Aiven Console <https://console.aiven.io/>`_:

#. In the organization, click **Support**.

#. In the **Current support tier** section, click **Upgrade to Enterprise**. 

#. Choose the support tier you want to upgrade to and click **Choose tier**. 

#. Select a **Start date**. 
    
   .. note::
    If you select the current month, you will be charged a percentage of the total service spend for the whole month, starting from the 1st.

#. Select a **Billing group**. 

   .. important::
    The support costs for all current and future services in the selected organization and all of its organizational units will be added to the invoice for this billing group.

#. Click **Upgrade tier**.

It typically takes 1-2 business days to set up the new support tier. You can view the status of your request on the support page under **Current support tier**.


Create a support ticket
~~~~~~~~~~~~~~~~~~~~~~~~

#. In the `Aiven Console <https://console.aiven.io/>`_, click **Support**.

#. Click **Go to Aiven Support Center**.

#. Click **Create ticket**. 

#. Enter email addresses to CC in the support ticket. All new comments and updates will be sent to these emails.

#. Enter a **Subject**.

#. Select a **Severity** level:

   * Low: The primary functions are working, but some secondary functionality is not working.
   * High: The primary functions are working, but severely limited or slow.
   * Critical: The primary functions are not working and it's not possible to find workarounds.

#. Optional: Enter the ID of the affected projects and services.

#. Select the affected **Product** and the reason for creating the ticket.

#. Enter a detailed **Description** of the issue. 

   .. note::

    Include the following information in the description to help the support team provide timely assistance:
   
    * The affected functionality (for example, networking, metrics, deployment)
    * Steps to reproduce the problem
    * Any error messages
    * Any languages or frameworks you are using

#. Optional: Upload files such as screenshots, logs, or :ref:`HAR files <create-har-files>`.
   
   .. important::
        Aiven support will never ask you to provide sensitive data such as passwords or personal information. Remove or replace sensitive data in files that you attach to a support ticket.

#. Click **Create ticket**. 

You can track the status of your tickets on the **My tickets** page. `Response times <https://aiven.io/support-services>`_ vary by case severity and support tier. If you are not satisfied with the processing of your ticket, add ``#escalate`` in the comments.


Add participants to a support ticket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to give every organization user access to all support tickets in your organization contact your account team.

To add Aiven users to a support ticket:

#. On the **My tickets** page, open the ticket.

#. Click **Add to conversation**.

#. Add the email addresses in the **CC** field separated by a space. This must be the same email address they use to log in.

#. Enter a comment and click **Submit**.


Get notifications for all support tickets 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Super admin can get notifications for updates on all tickets in their organization. 

#. Click **My tickets**.

#. On the **Tickets in my organization** tab, click **Follow all tickets**.

You will get email notifications for all updates on both existing and new tickets. You can unfollow them at any time.


.. _create-har-files:

Create HAR files
~~~~~~~~~~~~~~~~~

Aiven support may need information about the network requests that are generated in your browser when you experience a problem. Browsers can capture a log of these network requests in a HAR (HTTP Archive) file. 

If the support team asks for a HAR file:

#. Use your browser to create the HAR file while you go through the steps to reproduce the problem:

   * Follow the `instructions for Internet Explorer/Edge, Firefox, and Chrome <https://toolbox.googleapps.com/apps/har_analyzer/>`_.
   * For Safari, make sure you can access the `developer tools <https://support.apple.com/en-ie/guide/safari/sfri20948/mac>`_ and then follow the instructions for `exporting a HAR file <https://webkit.org/web-inspector/network-tab/>`_. 

#. Replace sensitive data in the file with placeholders while retaining the JSON structure and format. Examples of sensitive data include:
   
   * Personal identifiers such as email addresses and phone numbers
   * Authentication tokens or passwords
   * Sensitive URLs
   * Sensitive cookies or headers

#. Send the sanitized file to the support team in your reply to their email or in the ticket's comments.
