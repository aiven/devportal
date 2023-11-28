Manage project and service notifications
=========================================

To stay up to date with the latest information about services and projects, you can set service and project contacts to receive email notifications. Notifications include information about plan sizes, performance, outages, and scheduled maintenance. 

The contacts for a project can be set to the admin and operators of that project, or to specific email addresses. Project contacts receive notifications about the project. They also receive the notifications for all services, unless you set a separate service contact for a service.

Service contacts by default are the project contacts. However, if you set other email addresses as serivce contacts for a service, email notifications will only be sent to those contacts for that specific service.

.. _set-project-contacts:

Set project contacts 
"""""""""""""""""""""

#. In the project, click **Settings**.

#. On the **Notifications** tab, select the project contacts that you want to receive email notifications.

#. Click **Save changes**. 

.. _set-service-contacts:

Set service contacts 
"""""""""""""""""""""

#. In the service, open the menu in the top right.

#. Select **Change service contacts**.

#. Select the contacts that you want to receive email notifications.

#. Click **Save**. 


Set up Slack notifications
"""""""""""""""""""""""""""

To get notifications in Slack, you can add a Slack channel's or DM email address to the technical contacts for an Aiven project:

#. In Slack, `create an email address for a channel or DM <https://slack.com/help/articles/206819278-Send-emails-to-Slack#h_01F4WDZG8RTCTNAMR4KJ7D419V>`_.

   .. note::
       If you don't see the email integrations option, ask the owner or admin of the workspace or organization to `allow incoming emails <https://slack.com/help/articles/360053335433-Manage-incoming-emails-for-your-workspace-or-organization>`_.

#. In the Aiven Console, go to the project that you want to get notifications for.

#. Follow the instructions to set the Slack email address as a :ref:`project contact <set-project-contacts>` or :ref:`service contact <set-service-contacts>`.

Alternatively, you can `set up a Slackbot forwarding address <https://slack.com/help/articles/206819278-Send-emails-to-Slack#h_01F4WE06MBF06BBHQNZ1G0H2K5>`_ and use that to automatically forward Aiven's email notifications from your email client.