Connect with NodeJS
=====================

This example demonstrates how to connect to Dragonfly from NodeJS using the `ioredis` library, which is officially supported and compatible with Dragonfly. For more information, see `Dragonfly SDKs <https://www.dragonflydb.io/docs/development/sdks>`_.

Variables
----------

Replace the following placeholders in the code sample with the appropriate values:

==================      =============================================================
Variable                Description
==================      =============================================================
``DRAGONFLY_URI``       URL for the Dragonfly connection
==================      =============================================================

Pre-requisites
---------------

Install the `ioredis` library:

.. code::

   npm install --save ioredis

Code
-----

Create a new file named `index.js`, add the following content and replace the ``DRAGONFLY_URI`` placeholder with your Dragonfly instance's connection URI:

.. code::

   const Redis = require('ioredis');

   const redis = new Redis('DRAGONFLY_URI'); // Replace with your Dragonfly URI

   redis.set('key', 'hello world').then(() => {
        return redis.get('key');
   }).then((value) => {
        console.log('The value of key is:', value);
        process.exit();
   }).catch((err) => {
        console.error('Error:', err);
        process.exit(1);
   });

This code connects to Dragonfly, sets a key named `key` with the value `hello world` (without expiration), then retrieves and prints the value of this key.

Run the Code
--------------

To execute the code, use the following command in your terminal:

.. code::

   node index.js

If everything is set up correctly, the output should be:

.. code::

   The value of key is: hello world
