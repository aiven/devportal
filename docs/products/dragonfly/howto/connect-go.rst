Connect with Go
================

This example demonstrates how to connect to Dragonfly using Go, using the ``go-redis/redis`` library, which is officially supported with Dragonfly. For more information, see `Dragonfly SDKs <https://www.dragonflydb.io/docs/development/sdks>`_.

Variables
----------

These are the placeholders you will need to replace in the code sample:

==================      =============================================================
Variable                Description
==================      =============================================================
``DRAGONFLY_URI``       URL for the Dragonfly connection
==================      =============================================================

Pre-requisites
---------------

First, install the ``go-redis/redis`` library:

.. code::

    go get github.com/go-redis/redis/v8

Code
-------
Create a new file named ``main.go`` and add the following content, replacing the ``DRAGONFLY_URI`` placeholder with your Dragonfly instance's connection URI:

.. code:: go

    package main

    import (
        "context"
        "fmt"
        "github.com/go-redis/redis/v8"
    )

    var ctx = context.Background()

    func main() {
        dragonflyURI := "DRAGONFLY_URI"

        opts, err := redis.ParseURL(dragonflyURI)
        if err != nil {
            panic(err)
        }

        rdb := redis.NewClient(opts)

        err = rdb.Set(ctx, "key", "hello world", 0).Err()
        if err != nil {
            panic(err)
        }

        val, err := rdb.Get(ctx, "key").Result()
        if err != nil {
            panic(err)
        }
        fmt.Println("The value of key is:", val)
    }

This code connects to Dragonfly, sets a key named ``key`` with the value ``hello world`` (with no expiration), and then retrieves and prints the value of this key.

Run the code
--------------

To run the code, use the following command in your terminal:

.. code::

   go run main.go

If everything is set up correctly, the output should be:

.. code::

   The value of key is: hello world
