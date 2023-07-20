Tag your Aiven resources
========================

Tags can add metadata to Aiven resources like projects and services. Adding tags can be useful to categorize services, store specific information for your application or business, and group services or bills based on custom logic.

Tag details
-----------

A tag can be attached to any project or service and consists of the following:

* String **key**, which is case-sensitive and must consists of characters ``[A-Za-z0-9_-]`` and start with a letter. The maximum length for a key is 64 characters.
* Single **value**, which can be at most 64 UTF-8-character-long.

.. Note::

    Any single Aiven resource can have at most 10 tags attached. Within a resource, the tag keys must be unique, meaning that they can't be a duplicated.

To work with tags, you can use the following:

* `Aiven Console <https://console.aiven.io/>`_
* Aiven client: Aiven-client version 2.14.0 or later is required for tagging support.
* APIs (for example, `ProjectUpdate <https://api.aiven.io/doc/#tag/Project/operation/ProjectUpdate>`_)

Add tags to resources in Aiven Console
--------------------------------------

Add tags to projects
""""""""""""""""""""

You can add the following types of tags to projects:

* Billing reference tags - returned in the Invoice API and displayed on PDF invoices for the project
* Project tags - returned for resources in the API and displayed in the list of projects

To add tags to a project, take the following steps:

#. Log in to `Aiven Console <https://console.aiven.io/>`_ and select your organization and your project from the top navigation bar.
#. On the project's page, select **Settings** from the sidebar.
#. On the **Settings** page, add a key and its value in the **Billing Reference Tags** or **Project Tags** fields, and select the **+** icon to add more tags in the same manner.
#. Select **Save changes** to save all of your tags.

.. topic:: Result
    
    You can see the tags listed in the table on the **Projects** page.

Add tags to services
""""""""""""""""""""

To add tags to a service, take the following steps:

#. Log in to `Aiven Console <https://console.aiven.io/>`_ and select your organization and your project from the top navigation bar.
#. On the **Services** page of your project, select the service that you want to tag. 
#. On the **Overview** page of the service, go to **Service Tags** > **Tag service**.
#. In the **Tag this service** window, add a key and its value in the **Service Tags** fields, and select the **+** icon to add more tags in the same manner.
#. Select **Save changes** to save all of your tags.

.. topic:: Result

   You can see the tags listed in the table on the **Projects** page.


Add and modify resource tags with the Aiven client
--------------------------------------------------

Add and modify service tags 
""""""""""""""""""""""""""""

* Add new tags to a service::

    avn service tags update your-service --add-tag business_unit=sales --add-tag env=smoke_test

* Modify or remove tags::

    avn service tags update your-service --add-tag env=production --remove-tag business_unit

* List service tags::

    avn service tags list your-service
    KEY  VALUE
    ===  ==========
    env  production

* Replace tags with a set of new ones, removing the old ones::

    avn service tags replace your-service --tag cost_center=U1345

    avn service tags list your-service
    KEY          VALUE
    ===========  =====
    cost_center  U1345

Add and modify project tags
""""""""""""""""""""""""""""

The commands ``update``, ``list`` and ``replace`` exist for tagging projects too, and work the same way:

* Add tags to a project::

    avn project tags update --project your-project --add-tag business_unit=sales

* Replace project tags::

    avn project tags replace --project your-project --tag env=smoke_test

* List project tags::

    avn project tags list
    KEY  VALUE
    ===  ==========
    env  smoke_test
