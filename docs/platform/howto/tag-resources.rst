Tag your Aiven resources
========================

Tags can add metadata to Aiven resources like projects and services. Adding tags can be useful to categorize services, store specific information for your application or business, and group services or bills based on custom logic.

Tag details
-----------

A tag consists of a string **key** and a single **value** and can be attached to any project or service. 

Tag keys must consist of characters ``[A-Za-z0-9_-]``, are case sensitive, and must start with a letter. The maximum length for a key is 64 characters. 
Tag values can be at most 64 UTF-8 characters long.

.. Note::

    Any single Aiven resource can have **at most 10 tags attached**. Within a resource, the tag keys must be unique, meaning that they can't be a duplicated.

You can use either the Aiven Console or Aiven client (or call the tag APIs by some other means) to use tags. Aiven-client version 2.14.0 or later is required for tagging support.

Add tags to resources in the Aiven Console
------------------------------------------

Add tags to projects
"""""""""""""""""""""

You can add billing reference tags or project tags to projects. 

Billing reference tags are returned in the Invoice API. They are also displayed on PDF invoices for the project. Project tags are returned for resources in the API and are also displayed in the list of projects for an account.

To add tags to a project: 

#. In the project, click **Settings**. 
#. Add a key and value in the **Billing Reference Tags** or **Project Tags** and click the add new tag icon.
#. Click **Save changes** to save all of your tags. You can see the tags listed in the table on the **Projects** page.


Add tags to services
"""""""""""""""""""""

To add tags to a service:

#. On the **Current services** page, select the service that you want to tag. 
#. On the **Overview** page for the service in the **Service Tags** section, click **Tag service**. 
#. In the window that opens, add a key and value and click the add new tag icon.
#. After you have added all of the tags, click **Save changes**. You can see the tags listed in the table on the **Projects** page.


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
