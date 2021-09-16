Connect with Python
-------------------

This example connects to Redis service from Python, making use of the ``redis-py`` library.

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

1. Create a new directory and access it::

    mkdir redis-python
    cd redis-python

2. Initialize a new virtual environment::

    python -m venv venv
    source venv/bin/activate

3. Install the ``redis-py`` library::

    pip install redis

Code
''''
Create a new file named ``main.py``, add the following content and replace the placeholder with the Redis URI:

.. literalinclude:: /code/products/redis/connect.py

This code creates a key named ``key`` with the value ``hello world`` and no expiration time. Then, it gets the key back from Redis and prints its value.

Run the code::

    python main.py

If the script runs successfully, the outputs should be::

    The value of key is: hello world
