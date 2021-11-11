Tag your Aiven resources
========================

Tags can add metadata to Aiven resources like projects and services. Adding tags can be useful to categorize services, store specific information to your application or business and to group services or bills depending on custom logic.

Tag details
-----------

A tag consists of a string **key** and a single **value** and can be attached to any project or service. 

Tag keys must consist of characters ``[A-Za-z0-9_-]``, are case sensitive, and must **start with a letter**. The maximum length for a key is 64 characters. 
Tag values can be at most 64 UTF-8 characters long.

.. Note::

    Any single Aiven resource can have **at most 10 tags attached**. Within a resource, the tag keys are unique, meaning that there can't be a duplicated key.

Tags are supported for Aiven projects and services. You currently need to either use the Aiven client, or call the tag APIs by some other means, to use tags. Aiven-client version 2.14.0 or later is required for tagging support.

Add and modify service tags with the Aiven client
-------------------------------------------------

1. Select the service you want to tag.

2. Add new tags to the service::

    avn service tags update your-service --add-tag business_unit=sales --add-tag env=smoke_test

3. Modify or remove tags::

    avn service tags update your-service --add-tag env=production --remove-tag business_unit

4. List the tags::

    avn service tags list your-service
    KEY  VALUE
    ===  ==========
    env  production

5. Replace tags with a set of new ones, removing old ones::

    avn service tags replace your-service --tag cost_center=U1345

    avn service tags list your-service
    KEY          VALUE
    ===========  =====
    cost_center  U1345

Add and modify project tags
---------------------------

The commands `update`, `list` and `replace` exist for tagging projects too, and work the same way:

1. Add tags to a project::

    avn project tags update --project your-project --add-tag business_unit=sales

2. Replace project tags::

    avn project tags replace --project your-project --tag env=smoke_test

3. List project tags::

    avn project tags list
    KEY  VALUE
    ===  ==========
    env  smoke_test
