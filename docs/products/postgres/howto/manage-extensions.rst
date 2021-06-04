How to Install or Update an Extension
=====================================

Aiven PostgreSQL allows a series of pre-approved extensions to be installed.

Install an Extension
--------------------

Any available can be installed by the ``avnadmin`` user with the following ``CREATE EXTENSION`` command::

  CREATE EXTENSION <EXTENSION_NAME> CASCADE;


Update an Extension
-------------------

To upgrade an already-installed extension to the latest version available, run as the ``avnadmin`` user::

  ALTER EXTENSION <EXTENSION_NAME> UPDATE;

If you want to experiment with upgrading, remember that you can fork your existing database to try this operation on a copy rather than your live database.

.. warning:: When a service is updated via a maintenance update, this does not update the extension versions that are used automatically. The reason for this is that user schemas and functions can (and do often) rely on specific versions of an extension being used, so we can't assume that all extensions are safe to upgrade.

Request a New Extension
-----------------------

We are always open to suggestions of additional extensions that could be useful to many of our customers, and there are a few that can be enabled on request if you need them. For any extensions not on the :doc:`../reference/list-of-extensions` approved list, please open a support ticket and let us know:

 * which extension is requested
 * which database service and user database should have them

.. warning::
    "Untrusted" language extensions such as ``plpythonu`` cannot be supported as they would compromise our ability to guarantee the highest possible service level.

