Tutorial: Add caching to your PostgreSQL® app using Redis®*
===========================================================

Proposed outline (from earlier)
-------------------------------

.. note:: *This outline will go away when the document is written!*

We want a simple webapp fronting PG

* Use either Flask or FastAPI (the latter is more fashionable?)
* Show how to start up PG on Aiven, and how to populate it with some interesting data
* Show how to write a simple frontend that provides a GET request for data

  Can we come up with a use case that actually shows the speedup from caching?

  (perhaps do a ``count`` of records matching some criterion!)

* Explain why caching is a good idea in general
* Point out that a service doesn’t retain data between requests, and that a real backend may well be running multiple copies of a service, so there’s no way to share data in the application itself
* Explain that Redis is very easy to use, a good match for typical programming language datastructures, and popular for this sort of task
* Show how to start up a Redis service on Aiven
* First approach: cache explicitly by writing simple code in the request method
* Point out that we may have multiple hashes/dictionaries/maps in Redis for different purposes, and how Redis supports that
* Explain cache invalidation - both explicit when we POST data that changes
  the cached value, and implicit with TTL, which Redis supplies

  * Create a simple POST that adds a record which will invalidate the count
  * Show how if we don't make it so, the cached value will continue to be
    returned, even though if we use the PG CLI and SQL we can get back a
    different value
  * Show the TTL approach - the problem is that assumes we don't update too
    often!
  * Code the POST method invalidating the cache (removing the entry from
    Redis), do another POST (to make the invalidation happen), and show that
    the GET now gets an updated value

* Explain how explicit code per method doesn’t work very well if there are
  multiple GET requests, and introduce a simple Python decorator
* I don’t *think* we have scope to get into HTTP headers, ETAGs and other
  things…

Maybe mention that many web frameworks come with hooks for this sort of thing,
and point to the blog post(s) on Aiven and Django, if both of them are out. If
not, add such a link later on when they are both out.

---------

Learning objectives
-------------------

* ...
* ...

Overview
--------

...

Prerequisites
-------------

...
