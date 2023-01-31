Integrate ClickHouse®  with an open source BI tool
==================================================

Data analysis is a critical component of modern business operations. As organizations generate more and more data, it becomes increasingly difficult to extract meaningful insights from the raw information. That's where Business Intelligence (BI) tools can help us. BI tools allow organisations transform their data into visual, actionable insights that support informed decision-making.

In this tutorial, you'll learn how you can integrate ClickHouse database with an open source BI tool `Metabase <https://www.metabase.com/start/oss/>`_ to visualise the data stored in your databases. After completing this tutorial you'll have a dashboard in Metabase with insights from the data you have in ClickHouse.

After all, a picture is worth a thousand words.

Preparing ClickHouse cluster and data
--------------------------------------

We'll start on the ClickHouse side. In this section we'll set up the cluster and load the data that we can use for analysis.

Setting up Aiven for ClickHouse
+++++++++++++++++++++++++++++++

We recommend you use `Aiven for ClickHouse <https://aiven.io/clickhouse>`_ when following this tutorial. If you still don't have Aiven's account, `register over here <https://console.aiven.io/signup>`_. You'll get free credits that you can use for this tutorial.

Once you're logged into  Aiven platform, click on **Create service** and follow the wizard to set up the preferences.


We also have `a documentation <https://docs.aiven.io/docs/products/clickhouse/getting-started>`_  for detailed instructions.

Loading data
++++++++++++++
If you already have data in your ClickHouse database for analysis, feel free to skip this step and visualise your data.

Alternatively, you can use `a dataset from New York Public Library "What's on the Menu?" <http://menus.nypl.org/data>`_ as an example. This dataset is easy to setup and it has ample opportunities for exploration. The official documentation of ClickHouse offers `a convenient set of instructions <https://clickhouse.com/docs/en/getting-started/example-datasets/menus/>`_ to create the tables and load the data.

We'll be utilizing the data from the "What's on the Menu?" dataset in the examples below. However, the same techniques are applicable to your data.



Setting up OSS version of Metabase
------------------------------------------

Depending on your operating system and preferences, you can choose among two approaches when `setting up the open source edition of Metabase <https://www.metabase.com/start/oss/>`_: using a Docker image and running Metabase as a jar.

In this tutorial we'll be using `Docker <https://www.docker.com/>`_. However, similar results can be achieved using the ``.jar`` file.

If you don't have a license token for a paid version of Metabase and you don't need a production installation, these steps `for the quick start <https://www.metabase.com/docs/latest/installation-and-operation/running-metabase-on-docker#open-source-quick-start>`_ plus a minor adjustment `to include a ClickHouse driver <https://www.metabase.com/docs/latest/installation-and-operation/running-metabase-on-docker#adding-external-dependencies-or-plugins>`_ is what you need.

When starting your Docker container, make sure that you have access to the mounted folder. We'll need this folder for the next step.



Adding drivers
++++++++++++++
Metabase comes with a predefined set of supported database. ClickHouse is not in `the list of officially supported drivers <https://www.metabase.com/docs/latest/databases/connecting#connecting-to-supported-databases>`_, but we can include it `as a third-party community driver <https://www.metabase.com/docs/latest/developers-guide/partner-and-community-drivers#community-drivers>`_.

You can find ClickHouse driver (and extra documentation, in case you need it) in ClickHouse driver for Metabase `GitHub repository <https://github.com/ClickHouse/metabase-clickhouse-driver>`_.

Load the driver by going `to the latest release <https://github.com/ClickHouse/metabase-clickhouse-driver/releases>`_ and selecting ``clickhouse.metabase-driver.jar`` from the list of assets.



Add this file to the folder that you mounted in the previous step. This will allow Metabase to access ClickHouse driver and therefore work with ClickHouse data.

Starting Metabase
-----------------

Time to start Metabase! If you used the default ports when running the container, go to ``http://localhost:3000``, if you used a different port, adjust it accordingly.

The first time you open Metabase, it will ask you several questions. Remember the email and password you enter, they are needed for logins. Skip adding data, we'll do it separately in the next step




Connecting to ClickHouse
----------------------------------

In order to connect to ClickHouse server you need to add a database to Metabase and provide all necessary credentials for access. To add a database, click on **Add your own data**, this will navigate you to *Add Database* form.

If all went well installing a driver, you'll see **ClickHouse** in the list of available types of databases. If you don't see ClickHouse there, try restarting the container.

The connection between Metabase and ClickHouse happens over HTTPS. You can take all necessary properties (such as host, port and user credentials) from your *Aiven for ClickHouse* page in the section **ClickHouse HTTPS & JDBC**.




Visualising the data
----------------------------------

Now we can run analysis and visualise the data. To start with something simple, check for most popular currencies used across the menus in the dataset we have.

Click on the **New** button and select **SQL Query** from the list. Next, choose the database for your query (``AivenForClickHouse`` in our case) and you'll land onto the SQL query editor. You can use the same syntax here as running your usual ClickHouse queries.

.. code:: sql

    SELECT menu_currency_symbol, count() FROM menu_item_denorm
    GROUP BY menu_currency

The results will appear below the query editor. To visualise the findings, click on the button **Visualisation**. This will show you a set of possible options that fit your data. For this specific example, for example you can use a pie chart.

Once you're happy with the visualisation, save it. Metabase will also suggest adding the visualisation to a dashboard. If you don't want to do it yet, you can add it later.


Conclusions
------------
In this tutorial we described how to use ClickHouse together with an open source BI tool, Metabase. We used open source edition of Metabase and a community-developer driver for ClickHouse.

You can find more information about Aiven for ClickHouse in `our documentation <https://docs.aiven.io/>`_.