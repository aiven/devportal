Tutorial: Add caching to your PostgreSQL® app using Redis®*
===========================================================


Learning objectives
-------------------

* Creating a simple Python web application, that accesses data in a PostgreSQL database
* Using ``curl`` at the command line to make GET and POST requests to that web
  application
* Learning why caching the GET response is a good idea, and how to do that
  with Redis®*
* Learning some basics about cache invalidation - making sure the cache
  doesn't get out-of-date

Overview
--------

...

Prerequisites
-------------

* Python

* curl

* Either:

  * redis CLI and PG CLI (more general approach)

  or:

  * ``avn`` CLI (Aiven specific, but easier to use?)

Set up a Python virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   python -m venv venv
   pip install fastapi    # is that correct?

Create an Aiven for PostgreSQL® service
---------------------------------------


Make a note of the PostgreSQL connection parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Put some data into the database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Create a simple web application
-------------------------------

...using FastAPI

Code it to do a ``count`` on records matching some criterion - this is not
normally regarded as a fast operation, or one to repeat too often.

Use the PG CLI to perform the equivalent SQL and calculate the value.

Show the applcation in action, returning the same result.


Why do we want caching?
-----------------------

* Point out that a service doesn’t retain data between requests, and that a
  real backend may well be running multiple copies of a service, so there’s no
  way to share data in the application itself

* Explain that Redis is very easy to use, a good match for typical programming
  language data structures, and popular for this sort of task

Create an Aiven for Redis®* service
-----------------------------------


Make a note of the Redis connection parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Change the web application to cache using Redis
-----------------------------------------------

For the moment, just put the appropriate code into the GET method.

Show that the application continues to work as expected.

For extra points, use the Redis CLI to look at the cache in Redis directly.

But caches get out-of-date
--------------------------

Use the PG CLI to add a new record, changing the count.

Show that the application continues to return the same value.

Which is unhelpful.

Add a POST method to the application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add a POST method which adds a new record to PG, changing the count.

Show calling it, and use the PG CLI to confirm it worked.

Show (again) that the GET doesn't change its result.

Specifying a TTL ("time to live")
---------------------------------

Change the Python code to set a TTL.

(Is it then enough to do the GET again?)

Do a GET, showing the latest count.

Maybe show it in the Redis CLI as well?

Do a POST, an immediate GET (wrong value) and then wait the TTL and another
GET (correct value).

But we can't tell how often someone will do POST


Invalidating the cache
----------------------

Change the POST method to delete the cache entry in Redis.

Show POST, GET, POST, GET and that the correct entry is returned.

Using a Python decorator
------------------------

Explain that as more methods get added to the application, it seems like a
poor idea to just copy the caching code (explain why it's a poor idea).

Show a simple decorator approach.

Further reading
---------------

Point to the Aiven documentation for PG and Redis.

Mention that many web frameworks come with hooks for this sort of thing,

Point to the blog post(s) on Aiven and Django, if both of them are out. If
not, add such a link later on when they are both out.

Maybe point to other useful learning resources on web application caching.

  (Maybe mention there are other things, like ``ETAG``\s, that we're
  deliberately not addressing.)
