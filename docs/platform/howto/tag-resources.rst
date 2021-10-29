Tag your Aiven resources
========================

You can attach metadata to your Aiven resources using tags. They can help you to categorize your services, and store information specific to your application or business.

A tag consist of a string key and value, and you can have at most 10 tags attached to a single resource. Tag keys must be unique for a given resource, and one key can only hold one value. Keys must consist of characters `[A-Za-z0-9_-]` and start with a letter, and they are case sensitive. The maximum length for a key is 64 characters. Tag values can be at most 64 UTF-8 characters long.

Tags are supported for Aiven projects and services. You currently need to either use the Aiven client, or call the tag APIs by some other means, to use tags. Aiven-client version 2.14.0 or later is required for tagging support.

Add and modify service tags with the Aiven client
-------------------------------------------------

1. Select the service you want to tag.

2. Add new tags to the service::

    avn service tags update your-service --add-tag key=value --add-tag another=one

3. Modify or remove tags::

    avn service tags update your-service --add-tag another=two --remove-tag key

4. List the tags::

    avn service tags list your-service
    KEY      VALUE
    =======  =====
    another  two

5. Replace tags with a set of new ones, removing old ones::

    avn service tags replace your-service --tag new_tag=with_value

    avn service tags list your-service
    KEY      VALUE
    =======  ==========
    new_tag  with_value

Add and modify project tags
---------------------------

The commands `update`, `list` and `replace` exist for tagging projects too, and work the same way:

1. Add tags to a project::

    avn project tags update --project your-project --add-tag tag_key=tag_value

2. Replace project tags::

    avn service tags replace --project your-project --tag new_tag=with_value

3. List project tags::

    avn project tags list
    KEY      VALUE
    =======  ==========
    new_tag  with_value
