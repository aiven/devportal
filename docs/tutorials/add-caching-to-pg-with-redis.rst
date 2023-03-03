Tutorial: Add caching to your PostgreSQL® app using Redis®*
===========================================================

With any sufficiently complex application, performance becomes a primary concern to optimize for. One of the key metrics for measuring performance of any software is speed of reading and writing from a database. 

Most applications repeatedly store (write) and retrieve (read) some kind of input from the user or other systems. In most cases, the amount of reads far exceeds the amount of writes. 

Imagine, for example, a creating a customer profile for a store from a web form: the customer fills out their name, phone number, and address once and clicks submit. This creates one write to the database. However, during the checkout process, the application potentially reads that data many times: once to calculate shipping costs based on the customer's address, another time to pre-fill the payment details, and a third time to prompt the customer to receive SMS updates on their shipment. That's 3x the read operations, even in a simple example!

As a result of this, improving read performance gives us a far greater increase in overall performance for our work. The tried and tested way to do this is through using a cache. This becomes especially relevant when we start developing applications in the cloud. When we start making our applications highly available – that is, duplicating various services, like our databases in multiple regions globally to manage speed, and within regions themselves, to manage traffic spikes – we suddenly have data that needs to be read and written to internally, by the application itself, to maintain data integrity, in addition to externally, to be served to our users so they can do things.

Caching is the act of writing to a block of memory specifically designed for quick retrievals (reads) of common requests. In traditional hardware terms, the cache is typically a memory chip with particularly fast read and write access, like RAM. The computer uses a cache it kind of like a whiteboard: when it needs to, it writes a small amount of information to the cache quickly for a specific set of task, like retrieving a customer profiles. This lets the application access the customer's profile quickly for the many times it's needed during checkout, while only making the expensive and potentially slow call to the database once. The differences are mere milliseconds, but on the scale of global computing, those add up quickly!

However, we're developing applications for the cloud, not directly onto our computer. This adds a few layers of complexity, but opens up some interesting opportunities to optimize our performance further. Instead of using a block of memory (and the unbounded, chaotic nature that entails), we can use two databases instead! We can use one database as a data store, and one as a cache. This lets us optimize our data store for things like concurrency control and our cache for speedy reads and writes, while still taking advantage of everything the cloud offers us in terms of scalability. 

Setting up databases in the cloud is hard, so we'll use [Aiven for PostgreSQL®](https://aiven.io/postgresql) and [Aiven for Redis®](https://aiven.io/redis) in this tutorial. You can [sign up for our free trial](https://console.aiven.io/signup) to follow along!

An application can cache both read operations and write operations. This tutorial will go through caching read operations, but we'll talk about the advantages of caching writes at the end as well. 

What we'll learn
-----------------

* Creating a simple Python web application that accesses data in a PostgreSQL database
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

We're going to be writing a web application in Python, and you'll need at
least Python 3.7

.. note:: [[note while editing]]``psycopg2`` and ``redis-py`` currently still
          support 3.6, but ``fastapi`` requires at least 3.7, and honestly
          that's already quite an old version of Python!

* CLI tooling: The [Redis CLI](https://redis.io/docs/ui/cli/) for Redis and
  [Psql](https://www.geeksforgeeks.org/postgresql-psql-commands/) for
  PostgreSQL are useful to know as they're transferrable anywhere you go. We
  built the [avn CLI](https://docs.aiven.io/docs/tools/cli) to take advantage
  of all the features Aiven offers for its products, and this works too! We'll
  provide examples with both in this tutorial.

If you're following along without using Aiven, we still recommend deploying to
a cloud provider like AWS or Google Cloud. This tutorial assumes the databases
will be configured and deployed for you like Aiven does, and starts at the
point where we connect to a running service.


Set up a Python virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We'll do our development at the command line, in a Python virtual environment.
This will prevent any of the work we're doing in this tutorial from affecting
anything else you might be working on.

We'll also install the [FastAPI framework](https://fastapi.tiangolo.com/) in
this step. We'll use FastAPI to build a quick service hooked up to our
PostgreSQL database.

First, let's set up the Python virtual environment:

.. code:: shell

   python -m venv venv
   source venv/bin/activate

and then install the Python libraries we're going to want to use:

* ``fastapi`` (https://fastapi.tiangolo.com/) for writing our web application,
  and ``uvicorn`` (https://www.uvicorn.org/) to run it:

  .. code:: shell

    pip install fastapi uvicorn

* ``psycopg2`` (https://www.psycopg.org/) for talking to PostgreSQL®

  .. code:: shell

    pip install psycopg2

* and ``redis-py`` (https://github.com/redis/redis-py) for talking to Redis®*
  (we're not going to need that quite yet, but might as well install it now)

  .. code:: shell

    pip install redis[hiredis]

  .. note:: We could just do ``pip install redis``, but the documentation
            suggests installing ``redis[hiredis]`` to gain performance
            improvements. For this tutorial, we probably won't notice any difference.

You can quickly check all of those are installed correctly by starting up
Python:

.. code:: shell

   python

and then at the ``>>>`` prompt doing:

.. code:: python

   import fastapi
   import uvicorn
   import psycopg2
   import redis

If you don't get any errors from those, then you're good to go. Exit the
Python shell by typing:

.. code:: python

   exit()

or (if you're on Unix/Mac) using ``CTRL-D``

Installing command line tools to talk to PostgreSQL and Redis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  **Note** [[editorial]] this is taken from an in-progress blog post talking
  about Django and Redis, so needs extending to talk about PostgreSQL as well.
  Also, the "which to choose" section should make it clearer that we are also
  installing local PG and Redis service support, which can be useful when
  writing tests (this may be something to address at the end of the post).

We will want to be able to "talk" to the PostgreSQL and Redis servers.
We can do that in either of two ways:

1. Using the application specific tools, ``psql`` and ``redis-cli``
2. Using the [Aiven CLI](https://docs.aiven.io/docs/tools/cli)

Let's look at these in turn:

Installing the application specific tools
:::::::::::::::::::::::::::::::::::::::::

PostgreSQL:

https://www.postgresqltutorial.com/postgresql-getting-started/

or

.. code:: shell

   brew install postgresql@14

(for the moment, you have to specify a version of PG to install - use ``brew
search postgresql`` to find out what versions are available)

  **Note** we already know that doing this before doing ``pip install
  psycopg2`` (at least used to) sometimes save problems with that pip
  installation on Mac M1 machines. Is that still true?

Redis:

Using Redis' own tool, `redis-cli`, as described at [connect with redis-cli](https://developer.aiven.io/docs/products/redis/howto/connect-redis-cli.html)

For instance, on on my Mac I can do install Redis locally:

.. code:: shell

  brew install redis

and then run the command using the Redis service's URL from the service overview page:

.. code::

  redis-cli -u <REDIS-URI>

Installing the Aiven CLI
::::::::::::::::::::::::

We can install the [Aiven CLI](https://docs.aiven.io/docs/tools/cli) using
``pip``, still in our virtual environment:

.. code:: shell

  pip install aiven-cli

and then connect to an Aiven for PostgreSQL service using the service name:

.. code:: shell

  avn cli service pg-demo

and to an Aiven for Redis service using *its* service name:

.. code:: shell

  avn cli service redis-demo

These will actually start up either ``psql`` or ``redis-cli`` for you.


Which to choose?
::::::::::::::::

Using `redis-cli` is great if I want a local Redis server, for learning
about Redis, testing, etc., whilst `avn` is great if one is working with
Aiven already. Personally, I have both installed!

Create an Aiven for PostgreSQL® service
---------------------------------------

Next, let's navigate to the [Aiven console](https://console.aiven.io/). Sign up for our free trial if you haven't already, or log in if you have. 

Click **Create service** and create an Aiven for PostgreSQL® service with the following parameters: 

- **Service type:** PostgreSQL®
- **Cloud provider:** Choose the cloud provider of your choice. If you aren't sure what to pick, we suggest DigitalOcean.
- **Service cloud region:** Choose the region closest to you
- **Service plan:** Choose **Hobbyist** or **Startup** 
- **Service name:** Choose something meaningful - we're using `postgres-app-backend`

When you're ready, click **Create service**.

This initializes a PostgreSQL® database for us on the cloud and region you choose, with a small service plan.

If you were building a real application, you'd want to pick a larger plan. 

Make a note of the PostgreSQL connection parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When Aiven is done initializing your PostgreSQL service, it will direct you to the service's Overview page. 



While we're here, note down the following:

- **Service URI**
- **Host** 
- **Port** 
- **User** 
- **Password**

You can return to this page any time using the **Services** menu on the left hand menu and selecting the service you want to view. You can also use the **Quick connect** button to get convenient copy-and-paste commandsd and code snippets in a variety of CLI tools and programming connections! 

   **Note** [[editorial]] for the command line usage, we're going to want to
   put the necessary values into shell variables, so the Python script can
   look them up - this is better practice than embedding them in the script.

   Do we do that here, or later on?

Put some data into the database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  **Note** [[editorial]] the simplest solution is to follow
  https://docs.aiven.io/docs/products/postgresql/getting-started and use
  ``psql`` to load the data. Of course, we can also use ``avn`` to connect.
  This also means we get to install the appropriate command line tools nice
  and early, which is quite good.

  **Installing psql and **




Create a simple web application
-------------------------------

...using FastAPI

...something like the example from the FastAPI documentation, starting with a
file called ``main.py`` that contains:

.. code:: python

  from typing import Union

  from fastapi import FastAPI

  app = FastAPI()


  @app.get("/")
  def read_root():
      return {"Hello": "World"}


  @app.get("/items/{item_id}")
  def read_item(item_id: int, q: Union[str, None] = None):
      return {"item_id": item_id, "q": q}

.. note:: [[editing note]] While I approve of using ``typing``, should we
          remove that for "simplification"? I'm minded not to.

Then run it using the Python built-in web server support (this is definitely
not suitable for use in production, but it's a good way to get started for a
demo or tutorial):

.. code:: shell

   uvicorn main:app --reload

which should say something like::

  INFO:     Will watch for changes in these directories: ['/Users/tony.ibbs/sw/aiven/pg-redis-tutorial']
  INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
  INFO:     Started reloader process [75284] using StatReload
  INFO:     Started server process [75286]
  INFO:     Waiting for application startup.
  INFO:     Application startup complete.

and if you go to ``http://127.0.0.1:8000`` in your web browser, you should
see::

  {"Hello":"World"}

Make it talk to the PostgreSQL database
---------------------------------------

Code it to do a ``count`` on records matching some criterion - this is not
normally regarded as a fast operation, or one to repeat too often.

Use the PG CLI to perform the equivalent SQL and calculate the value.

Show the application in action, returning the same result.


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
