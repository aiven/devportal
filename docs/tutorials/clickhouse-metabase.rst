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

.. image:: /images/tutorials/clickhouse-metabase/small.gif
   :alt: Animated GIF showing pulling latest docker image and running it


Conclusions
------------
In this tutorial we described how to use ClickHouse together with an open source BI tool, Metabase. We used open source edition of Metabase and a community-developer driver for ClickHouse.

You can find more information about Aiven for ClickHouse in `our documentation <https://docs.aiven.io/>`_.