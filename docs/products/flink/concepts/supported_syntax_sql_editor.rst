Supported syntax in the Aiven SQL editor
========================================

The SQL editor that is available in the Aiven web console has certain limitations regarding the syntax that it supports. This article highlights what you should take into consideration when you use the editor.

The SQL editor in the Aiven web console highlights the content that you enter according to standard SQL syntax validation. However, it does not indicate syntax that the Aiven backend systems do not currently support. This means that the operation may fail when you submit the content, even though what you see in the editor is technically valid SQL syntax.

At the moment, Aiven for Apache Flink services do not support the following SQL syntax:

* SQL comments
* empty lines
* line changes
* tabs
* whitespace characters (except for single spaces in command lines)
* special characters

All other valid SQL syntax is supported.

Examples
--------

The following is an example of content that is not supported in the SQL editor:

.. code-block:: sql

    /* Add events with high CPU load */
    
    INSERT INTO KAlert SELECT * FROM KCpuIn WHERE 'cpu' > 70
    
    -- change CPU load if necessary
	

And the following is a supported example:

.. code-block:: sql

    INSERT INTO KAlert SELECT * FROM KCpuIn WHERE 'cpu' > 70

