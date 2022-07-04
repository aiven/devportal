Connect with Python
-------------------

This example connects to Redis®* service from Python, making use of the ``redis-py`` library.

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

==================      =============================================================
Variable                Description
==================      =============================================================
``REDIS_URI``           URL for the Redis connection, from the service overview page
==================      =============================================================

Pre-requisites
''''''''''''''

Install the ``redis-py`` library::

    pip install redis

Code
''''
Create a new file named ``main.py``, add the following content and replace the placeholder with the Redis URI:

.. literalinclude:: /code/products/redis/connect.py
   :language: python

This code creates a key named ``key`` with the value ``hello world`` and no expiration time. Then, it gets the key back from Redis and prints its value.

Run the code::

    python main.py

.. note::

    Note that on some systems you will need to use `python3` to get Python3 rather than the previous Python2

If the script runs successfully, the outputs should be::

    The value of key is: hello world
