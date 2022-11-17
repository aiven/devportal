Use Aggregations with OpenSearch® and NodeJS
============================================

Learn how to aggregate data using OpenSearch and its NodeJS client. In this tutorial we'll look at different types of aggregations, write and execute requests to learn more about the data in our dataset.

.. note::
    If you're new to OpenSearch® and its JavaScript client you might want to check :doc:`how to write search queries with OpenSearch with NodeJS <opensearch-and-nodejs>` first.

Prepare the playground
**********************

You can create an OpenSearch cluster either with the visual interface or with the command line. Depending on your preference follow the instructions for :doc:`getting started with the console for Aiven for Opensearch <../getting-started>` or see :doc:`how to create a service with the help of Aiven command line interface <../../../tools/cli/service>`.

.. note::

    You can also clone the final demo project from `GitHub repository <https://github.com/aiven/demo-open-search-node-js>`_.

File structure and GitHub repository
------------------------------------

To organise our development space we'll use these files:

- ``config.js`` to keep necessary basis to connect to the cluster,
- ``index.js`` to hold methods which manipulate the index,
- ``helpers.js`` to contain utilities for logging responses,
- ``search.js`` and ``aggregation.js`` for methods specific to search and aggregation requests.

We’ll be adding code into these files and running the methods from the command line.

Connect to the cluster and load data
------------------------------------

Follow instructions on how to :doc:`connect to the cluster with a NodeJS client <connect-with-nodejs>` and add the necessary code to ``config.js``. Once you're connected :ref:`load a sample data set <load-data-with-nodejs>` and :ref:`retrieve the data mapping <get-mapping-with-nodejs>` to understand the structure of the created index.

.. note::
    In the code snippets we'll keep error handling somewhat simple and use ``console.log`` to print information into the terminal.

Now you're ready to start aggregating the data.

Aggregations
************

In this tutorial we'll write and run examples for three different types of aggregations: metric, bucket and pipeline. You can read more about aggregations in :doc:`a concept article <../concepts/aggregations>`.

Structure and syntax
--------------------

To calculate an aggregation, create a request and then send it to the ``search()`` endpoint (the same we used for search queries).

The request body should include an object with the key ``aggs`` (or you can use a longer word ``aggregations``). Specify in this object **a name** of your aggregation (we might want to reference each aggregation individually), **an aggregation type** and **a set of properties** specific for the given aggregation type.

.. note::
    In most cases when we deal with aggregations we are not interested in individual hits, that's why it is common to set ``size`` property to zero.

The structure of a simple request looks like this:

.. code-block:: javascript

      client.search(
        {
          index,
          body: {
            aggs: {
              'GIVE-IT-A-NAME': { // aggregation name
                'SPECIFY-TYPE': {  // one of the supported aggregation types
                  ... // list of properties, such as a field on which to perform the aggregation
                },
              },
            },
          },
          size: 0, // we're not interested in `hits`
        }
      );


The best way to learn more about each type of aggregations is to try them out. Therefore, it's time to make our hands dirty and do some coding. Create `aggregate.js` file, this is where we'll be adding our code. At the top of the file import client and index name, we'll need them to send requests to the cluster.

.. code-block:: javascript

    const { client, indexName: index } = require("./config");



Metrics aggregations
********************

Average value
-------------

The simplest form of an aggregation is perhaps a calculation of a single-value metric, such as finding an average across values in a field.
Using the draft structure of an aggregation we can create a method to calculate the average of the recipe ratings:

.. code-block:: javascript

    /**
     * Calculate average rating of all documents
     * run-func aggregate averageRating
     */
    module.exports.averageRating = () => {
      client.search(
        {
          index,
          body: {
            aggs: {
              "average-rating": { // aggregation name
                avg: { // one of the supported aggregation types
                  field: "rating", // list of properties for the aggregation
                },
              },
            },
          },
          size: 0, // ignore `hits`
        },
        (error, result) => { // callback to log the output
          if (error) {
            console.error(error);
          } else {
            console.log(result.body.aggregations["average-rating"]);
          }
        }
      );
    };

Run the method from the command line::

    run-func aggregate averageRating

You'll see a calculated numeric value, the average of all values from the rating field across the documents.

::

    { value: 3.7130597014925373 }

``avg`` is one of many metric aggregation functions offered by OpenSearch. We can also use ``max``, ``min``, ``sum`` and others.

To have a possibility to easily change aggregation function and aggregation field we can do couple of simplifications in the method we created:

* move the aggregation type and aggregation field to the method parameters, so that different values can be passed as arguments
* generate name dynamically based on field name
* separate the callback function and use the dynamically generated name to print out the result


With these changes our method looks like this:

.. code-block:: javascript

    const logAggs = (field, error, result) => {
      if (error) {
        console.error(error);
      } else {
        console.log(result.body.aggregations[field]);
      }
    };

    /**
     * Get metric aggregations for the field
     * Examples: avg, min, max, stats, extended_stats, percentiles, terms
     * run-func aggregate metric avg rating
     */
    module.exports.metric = (metric, field) => {
      const body = {
        aggs: {
          [`aggs-for-${field}`]: { // aggregation name, which you choose
            [metric]: { // one of the supported aggregation types
              field,
            },
          },
        },
      };
      client.search(
        {
          index,
          body,
          size: 0, // ignore `hits`
        },
        logAggs.bind(this, `aggs-for-${field}`) // callback to log the aggregation output
      );
    };

Run the method to make sure that we still can calculate the average rating ::

    run-func aggregate metric avg rating

And because we like clean code, move and export the ``logAggs`` function from ``helpers.js`` and reference it in ``aggregate.js``.

.. code-block:: javascript

    const { logAggs } = require("./helpers");

Other simple metrics
--------------------

We can use the method we created to run other types of metric aggregations, for example, to find what the minimum sodium value is, in any of the recipes:

::

    run-func aggregate metric min sodium

Try out other fields and simple functions such as ``min``, ``max``, ``avg``, ``sum``, ``count``, ``value_count`` and see what results you will get.

Cardinality
------------

Another interesting single-value metric is ``cardinality``. Cardinality is an estimated number of distinct values found in a field of a document.

For example, by calculating the cardinality of the rating field, you will learn that there are only eight distinct rating values over all 20k recipes. Which makes me suspect that the rating data was added artificially later into the data set. The cardinality of `calories`, `sodium` and `fat` field contain more realistic diversity:

::

    run-func aggregate metric cardinality rating

::

    { value: 8 }

Calculating cardinality for sodium and other fields and see what conclusions you can make!

Field statistics
----------------

A multi-value aggregation returns an object rather than a single value. An example of such aggregation are statistics and we can continue using the method we created to explore different types of computed statistics.

Get a set of metrics (``avg``, ``count``, ``max``, ``min`` and ``sum``) by using ``stats`` aggregation type:

::

    run-func aggregate metric stats rating

::

    { count: 20100, min: 0, max: 5, avg: 3.7130597014925373, sum: 74632.5 }

To get additional information, such as standard deviation, variance and bounds, use ``extended_stats``:

::

    run-func aggregate metric extended_stats rating

::

    {
      count: 20100,
      min: 0,
      max: 5,
      avg: 3.7130597014925373,
      sum: 74632.5,
      sum_of_squares: 313374.21875,
      variance: 1.803944804893444,
      variance_population: 1.803944804893444,
      variance_sampling: 1.8040345578565216,
      std_deviation: 1.3431101238891188,
      std_deviation_population: 1.3431101238891188,
      std_deviation_sampling: 1.3431435358354376,
      std_deviation_bounds: {
        upper: 6.399279949270775,
        lower: 1.0268394537142997,
        upper_population: 6.399279949270775,
        lower_population: 1.0268394537142997,
        upper_sampling: 6.399346773163412,
        lower_sampling: 1.0267726298216622
      }
    }

Percentiles
-----------

Another example of a multi-value aggregation are ``percentiles``. Percentiles are used to interpret and understand data indicating how a given data point compares to other values in a data set. For example, if you take a test and score on the 80th percentile, it means that you did better than 80% of participants. Similarly, when a provider measures internet usage and peaks, the 90th percentile indicates that 90% of time the usage falls below that amount.

Calculate percentiles for `calories`:

::

    run-func aggregate metric percentiles calories

::

    {
      values: {
        '1.0': 17.503999999999998,
        '5.0': 62,
        '25.0': 197.65254901960782,
        '50.0': 331.2031703590527,
        '75.0': 585.5843561472852,
        '95.0': 1317.4926233766223,
        '99.0': 3256.4999999999945
      }
    }

From the returned result you can see that 50% of recipes have less than 331 calories. Interestingly, only one percent of the meals is more than 3256 calories. You must be curious what falls within that last percentile ;) Now that we know the value to look for, we can use `a range query <https://docs.aiven.io/docs/products/opensearch/howto/opensearch-and-nodejs.html#find-fields-with-a-value-within-a-range>`_ to find the recipes. Set the minimum value, but keep the maximum empty to allow no bounds:

::

    run-func search range calories 3256

::

    [
      'Ginger Crunch Cake with Strawberry Sauce ',
      'Apple, Pear, and Cranberry Coffee Cake ',
      'Roast Lobster with Pink Butter Sauce ',
      'Birthday Party Paella ',
      'Clementine-Salted Turkey with Redeye Gravy ',
      'Roast Goose with Garlic, Onion and Sage Stuffing ',
      'Chocolate Plum Cake ',
      'Carrot Cake with Cream Cheese-Lemon Zest Frosting ',
      'Lemon Cream Pie ',
      'Rice Pilaf with Lamb, Carrots, and Raisins '
    ]

Ah, I knew it! A chocolate plum cake 🎂

Bucket aggregations
*******************

Buckets based on ranges
-----------------------
You can aggregate data by dividing it into a set of buckets. We can either predefine these buckets, or create them dynamically to fit the data.

To understand how this works, we'll create a method to aggregate recipes into buckets based on sodium ranges.

We use ``range`` aggregation and add a property ``ranges`` to describe how we want to split the data across buckets:

.. code-block:: javascript

    /**
     * Group recipes into bucket based on sodium levels
     * run-func aggregate sodiumRange
     */
    module.exports.sodiumRange = () => {
      client.search(
        {
          index,
          body: {
            aggs: {
              "sodium-ranges": { // aggregation name
                range: { // range aggregation
                  field: "sodium", // field to use for the aggregation
                  ranges: [ // the buckets we want
                    { to: 500.0 },
                    { from: 500.0, to: 1000.0 },
                    { from: 1000.0 },
                  ],
                },
              },
            },
          },
          size: 0,
        },
        (error, result) => { // callback to output the result
          if (error) {
            console.error(error);
          } else {
            console.log(result.body.aggregations["sodium-ranges"]);
          }
        }
      );
    };

Run it with ::

    run-func aggregate sodiumRange

And then check the results::

    {
      buckets: [
        { key: '*-500.0', to: 500, doc_count: 10411 },
        { key: '500.0-1000.0', from: 500, to: 1000, doc_count: 2938 },
        { key: '1000.0-*', from: 1000, doc_count: 2625 }
      ]
    }

By looking at ``doc_count`` we can say how many recipes fall into each of the buckets.

However, our method is narrowed down to a specific scenario. We want to refactor it a bit to use for other fields and different sets of ranges. To achieve this we'll:

* move aggregation field and bucket ranges to the list of method parameters
* use the rest parameter syntax to collect range values
* transform the list of range values into ``ranges`` object in a format `from X` / `to Y` expected by OpenSearch API
* use logAggs function, which we already created, to log the results
* separate ``body`` into a variable for better readability


.. code-block:: javascript

    /**
     * Group recipes into bucket based on the provided field and set of ranges
     * run-func aggregate range sodium 500 1000
     */
    module.exports.range = (field, ...values) => { // map values to list of ranges
                                                   // in format 'from X'/'to Y'
      const ranges = values.map((value, index) => ({
        from: values[index - 1],
        to: value,
      }));
      // account for the last item 'from X to infinity'
      ranges.push({
        from: values[values.length - 1],
      });

      const body = {
        aggs: {
          [`range-aggs-for-${field}`]: {
            range: {
              field,
              ranges,
            },
          },
        },
      };
      client.search(
        {
          index,
          body,
          size: 0,
        },
        logAggs.bind(this, `range-aggs-for-${field}`)
      );
    };

To make sure that the upgraded function works just like the one one, run::

    run-func aggregate range sodium 500 1000

Now you can run the method with other fields and custom ranges, for example, split recipes into buckets based on values in the field `fat`::

    run-func aggregate range fat 1 5 10 30 50 100


The returned buckets are::

    {
      buckets: [
        { key: '*-1.0', to: 1, doc_count: 1230 },
        { key: '1.0-5.0', from: 1, to: 5, doc_count: 1609 },
        { key: '5.0-10.0', from: 5, to: 10, doc_count: 1916 },
        { key: '10.0-30.0', from: 10, to: 30, doc_count: 6526 },
        { key: '30.0-50.0', from: 30, to: 50, doc_count: 2404 },
        { key: '50.0-100.0', from: 50, to: 100, doc_count: 1648 },
        { key: '100.0-*', from: 100, doc_count: 575 }
      ]
    }

Why not experiment more with the range aggregation? We still have `protein` values, and can also play with the values for the ranges to learn more about recipes from our dataset.

Buckets for every unique value
------------------------------

Sometimes we want to divide the data into buckets, where each bucket corresponds to a unique value present in a field.
This type of aggregations is called ``terms`` aggregation and is helpful when we need to have more granular understanding of a dataset. For example, we can learn how many recipes belong to each category.

The structure of the method for `terms aggregation` will be similar to what we wrote for the ranges, with a couple of differences:

* use aggregation type ``terms``
* use an optional property ``size``, which specifies the upper limit of the buckets we want to create.

.. code-block:: javascript

    /**
     * Group recipes into buckets for every unique value
     * `run-func aggregate terms categories.keyword 20`
     */
    module.exports.terms = (field, size) => {
      const body = {
        aggs: {
          [`terms-aggs-for-${field}`]: {
            terms: { // aggregate data by unique terms
              field,
              size, // max number of buckets generated, default value is 10
            },
          },
        },
      };
      client.search(
        {
          index,
          body,
          size: 0,
        },
        logAggs.bind(this, `terms-aggs-for-${field}`)
      );
    };

To get the buckets created for different categories run::

    run-func aggregate terms categories.keyword

Here are the resulting delicious categories::

    {
      doc_count_error_upper_bound: 0,
      sum_other_doc_count: 175719,
      buckets: [
        { key: 'Bon Appétit', doc_count: 9355 },
        { key: 'Peanut Free', doc_count: 8390 },
        { key: 'Soy Free', doc_count: 8088 },
        { key: 'Tree Nut Free', doc_count: 7044 },
        { key: 'Vegetarian', doc_count: 6846 },
        { key: 'Gourmet', doc_count: 6648 },
        { key: 'Kosher', doc_count: 6175 },
        { key: 'Pescatarian', doc_count: 6042 },
        { key: 'Quick & Easy', doc_count: 5372 },
        { key: 'Wheat/Gluten-Free', doc_count: 4906 }
      ]
    }

We can see a couple of interesting things in the response. First, there were just 10 buckets created, each of which contains ``doc_count`` indicating number of recipes within particular category. Second, ``sum_other_doc_count`` is the sum of documents which are left out of response, this number is high because almost every recipe is assigned to more than one category.

We can increase the number of created buckets by using the ``size`` property::

    run-func aggregate terms categories.keyword 30

Now the list of buckets contains 30 items.

Find least frequent items
-------------------------

Did you notice that the buckets created with the help of ``terms`` aggregation are sorted by their size in descending order? You might wonder how you can find the least frequent items?

You can use the ``rare_terms`` aggregation! This creates a set of buckets sorted by number of documents in ascending order. As a result, the most rarely used items will be at the top of the response.

``rare_terms`` request is very similar to ``terms``, however, instead of `size` property which defines total number of created buckets, ``rare_terms`` relies on ``max_doc_count``, which sets upper limit for number of documents per bucket.

.. code-block:: javascript

    /**
     * Group recipes into buckets to find the most rare items
     * `run-func aggregate rareTerms categories.keyword 3`
     */
    module.exports.rareTerms = (field, max) => {
      const body = {
        aggs: {
          [`rare-terms-aggs-for-${field}`]: {
            rare_terms: {
              field,
              max_doc_count: max, // get buckets that contain no more than max items
            },
          },
        },
      };
      client.search(
        {
          index,
          body,
          size: 0,
        },
        logAggs.bind(this, `rare-terms-aggs-for-${field}`)
      );
    };


::

    run-func aggregate rareTerms categories.keyword 3

The result will return us all the categories with at most three documents each. Frankly, I believe the waffle category deserves more recipes! 🧇

Histograms
----------

The story of bucket aggregations won't be complete without speaking about histograms. Histograms aggregate date based on provided interval. And since we have a `date` property, we'll build a date histogram.

The format of the histogram aggregation is similar to what we saw so far, so we can create a new method almost identical to previous ones:

.. code-block:: javascript

    /**
     * Date histogram with a time interval
     * `run-func aggregate dateHistogram date year`
     */
    module.exports.dateHistogram = (field, interval) => {
      const body = {
        aggs: {
          [`histogram-for-${field}`]: {
            date_histogram: { // aggregation type
              field,
              interval, // such as minute, hour, day, month or year
            },
          },
        },
      };
      client.search(
        {
          index,
          body,
          size: 0,
        },
        logAggs.bind(this, `histogram-for-${field}`)
      );
    };

Values for the interval field can be from `minute` up to a `year`.

::

    run-func aggregate dateHistogram date year

The results when we use a year::

    {
      buckets: [
        {
          key_as_string: '1996-01-01T00:00:00.000Z',
          key: 820454400000,
          doc_count: 1
        },
        ...
        {
          key_as_string: '2004-01-01T00:00:00.000Z',
          key: 1072915200000,
          doc_count: 11576
        },
        ...
      ]
    }

You should see a list of buckets, one per each year starting at 1996 and up to 2016, with ``doc_count`` indicating how many recipes belong to each year. Most of the data items are marked by year 2004.

Now that we have seen examples of metric and bucket aggregations, it is time to learn some more advanced concepts of pipeline aggregations.

Pipeline aggregations
*********************

Calculate moving average
------------------------

When working with continuously incoming data we might want to understand the trends and changes in the figures. This is convenient in many situations, such as helping to see the changes in sales over a given time, noticing the divergence in the activity of users or learn about other trends.

OpenSearch allows "piping" the results of one aggregation into the different one to achieve more granular analysis through an intermediate step.

To demonstrate an example of pipeline aggregations, we'll look at the moving average of number of recipes added throughout the years. With the help of what we learned so far and a couple of new tools we can do the following:

1. Create a date histogram to divide documents across years (we name it ``date_histogram``)
2. Create a metric aggregation to count documents added per year (we name it ``new_recipes``)
3. Use a moving function, a pipeline feature, to glue theses aggregations together
4. Use a built-in function ``unweightedAvg`` to calculate average value within a window
5. Use ``shift`` property to move window one step forward and include the current year (by default the current data position is excluded from the calculated year)
6. Set ``window`` property to define the size of moving window

When put these pieces together we can write this method:

.. code-block:: javascript

    /**
     * Calculating the moving average of number of added recipes across years
     * `run-func aggregate movingAverage`
     */
    module.exports.movingAverage = () => {
      const body = {
        aggs: {
          recipes_per_year: { // 1. date histogram
            date_histogram: {
              field: "date",
              interval: "year",
            },
            aggs: {
              recipes_count: { // 2. metric aggregation to count new recipes
                value_count: { // aggregate by number of documents with field 'date'
                  field: "date"
                },
              },
              moving_average: {
                moving_fn: { // 3. glue the aggregations
                  script: "MovingFunctions.unweightedAvg(values)", // 4. a built-in function
                  shift: 1, // 5. take into account the existing year as part of the window
                  window: 3, // 6. set size of the moving window
                  buckets_path: "recipes_count",
                  gap_policy: "insert_zeros", // account for years where no recipes were
                                              // added and replace null value with zeros
                },
              },
            },
          },
        },
      };
      client.search(
        {
          index,
          body,
          size: 0,
        },
        (error, result) => {
          if (error) {
            console.error(error);
          } else {
            console.log(result.body.aggregations["recipes_per_year"].buckets);
          }
        }
      );
    };

Run it on the command line::

    run-func aggregate movingAverage

The returned  data for every year including a value ``moving_average``::

    [
      {
        key_as_string: '1996-01-01T00:00:00.000Z',
        key: 820454400000,
        doc_count: 1,
        count: { value: 1 },
        moving_average: { value: 1 }
      },
      {
        key_as_string: '1997-01-01T00:00:00.000Z',
        key: 852076800000,
        doc_count: 0,
        count: { value: 0 },
        moving_average: { value: 0.5 }
      },
      {
        key_as_string: '1998-01-01T00:00:00.000Z',
        key: 883612800000,
        doc_count: 3,
        count: { value: 3 },
        moving_average: { value: 1.3333333333333333 }
      },
      {
        key_as_string: '1999-01-01T00:00:00.000Z',
        key: 915148800000,
        doc_count: 4,
        count: { value: 4 },
        moving_average: { value: 2.3333333333333335 }
      },
    ...
    ]

Pay attention to the values of ``count`` and ``moving_average``. To understand better how those numbers were calculated, we can compute first several values on our own:

.. list-table:: Making sense of moving_average result
   :header-rows: 1

   * - Year
     - Added documents
     - Moving average
   * - 1996
     - 1
     - 1 (no previous years to make a comparison)
   * - 1997
     - 0
     - (1 + 0) / 2 = 0.5 (we had only two years)
   * - 1998
     - 3
     - (1 + 0 + 3) / 3 = 1.3(3)
   * - 1999
     - 4
     - (0 + 3 + 4) / 3 = 2.3(3)
   * - 2000
     - 0
     - (3 + 4 + 0) / 3 = 2.3(3)
   * - ...
     - ...
     - and so on


For every data point (a year in our case) we take the count of added recipes, add number of recipes added over last two years and divide the result by three (according to the size of our window). For the first and second year we divide by the number of available years (1 and 2 respectively). And this is how moving average is calculated. If you compare numbers from the table with the numbers returned in the ``moving_average`` field of the response body, you can see they are same.

Other moving functions
----------------------

We used one of existing built-in functions ``MovingFunctions.unweightedAvg(values)``, which as its name says calculates unweighted average. Unweighted in this context means that the function does not perform any time-dependent weighting.

You can also use other functions such as max(), min(), stdDev() and sum(). Additionally, you can write your own functions, such as

::

    moving_fn: {
        script: "return values.length === 1 ? 1 : 0"
    }

Try replacing the script with ``MovingFunctions.min(values)``, ``MovingFunctions.max(values)`` or custom scripts, changing the window size and shift, and see how thus affects the outcome!


What's next
***********

This was a long ride, hopefully you have a better understanding now how to use aggregations with OpenSearch and its NodeJS client. The best way to deepen the knowledge on these concepts is to play and experiment with different types of aggregations.

We covered some of the examples, but `OpenSearch documentation <https://opensearch.org/docs/latest/opensearch/aggregations/>`_ contains many more. Check OpenSearch docs, as well as other resources listed below to learn more.


Resources
*********

* `Demo GitHub repository <https://github.com/aiven/demo-open-search-node-js>`_ - where all the examples we run in this tutorial can be found
* :doc:`Previous chapter of the tutorial <opensearch-and-nodejs>` - learn how to use OpenSearch with NodeJS to make search queries
* :doc:`How to use OpenSearch with curl <opensearch-with-curl>`
* `GitHub repository for OpenSearch JavaScript client  <https://github.com/opensearch-project/opensearch-js>`_
* `Official OpenSearch documentation <https://opensearch.org>`_
    *  `Metric aggregations <https://opensearch.org/docs/latest/opensearch/metric-agg/>`_
    *  `Bucket aggregations <https://opensearch.org/docs/latest/opensearch/bucket-agg/>`_
    *  `Pipeline aggregations <https://opensearch.org/docs/latest/opensearch/pipeline-agg/>`_

