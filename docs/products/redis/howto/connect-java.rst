Connect with Java
-------------------

This example connects to Redis™* service from Java, making use of the ``jredis``.

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

If there is ``maven`` installed then download of ``jredis`` and dependencies and putting it to ``lib`` folder could be done ::

    mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:get -Dartifact=redis.clients:jedis:4.1.1:jar -Ddest=lib/jedis-4.1.1.jar \
    && mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:get -Dartifact=org.apache.commons:commons-pool2:2.11.1:jar -Ddest=lib/commons-pool2-2.11.1.jar \
    && mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:get -Dartifact=org.slf4j:slf4j-api:1.7.35:jar -Ddest=lib/slf4j-api-1.7.35.jar \
    && mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:get -Dartifact=com.google.code.gson:gson:2.8.9:jar -Ddest=lib/gson-2.8.9.jar

If there is no maven then download these dependencies from `Maven Central Repository <https://search.maven.org>`_ and put them to ``lib`` folder

Code
''''
Create a new file named ``RedisExample.java``:

.. literalinclude:: /code/products/redis/connect.java

This code creates a key named ``key`` with the value ``hello world`` and no expiration time. Then, it gets the key back from Redis and prints its value.

Replace the placeholder with the **Redis URI** and compile and run the code::

    javac -cp lib/*:. RedisExample.java && java -cp lib/*:. RedisExample REDIS_URI


If the command runs successfully, the outputs should be::

    The value of key is: hello world
