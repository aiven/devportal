Connect with Python
====================

This example demonstrates how to connect to Dragonfly® using Python, using the ``redis-py`` library, which is officially supported by Dragonfly. For more information, see `Dragonfly SDKs <https://www.dragonflydb.io/docs/development/sdks>`_.

Variables
-----------

Replace the following placeholders in the code sample with the appropriate values:

==================      =============================================================
Variable                Description
==================      =============================================================
``DRAGONFLY_URI``       URL for the Dragonfly connection
==================      =============================================================

Pre-requisites
----------------

Install the ``redis-py`` library:

.. code::

   pip install redis

Code
-----

Create a new file named ``main.py``, add the following content and replace the ``DRAGONFLY_URI`` placeholder with your Dragonfly instance's connection URI:

.. code:: 

   import redis

   # Replace with your Dragonfly URI
   r = redis.Redis.from_url('DRAGONFLY_URI')

   r.set('key', 'hello world')
   value = r.get('key')
   print(f'The value of key is: {value.decode()}')

This code connects to Dragonfly, sets a key named ``key`` with the value ``hello world`` (without expiration), and then retrieves and prints the value of this key.

Run the code
--------------

To execute the code, use the following command in your terminal:

.. code::

   python main.py

.. note::

   On some systems, you may need to use ``python3`` instead of ``python`` to invoke ``Python 3``.

If everything is set up correctly, the output should be:

.. code::

   The value of key is: hello world
