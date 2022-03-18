Aggregations
============

Alongside the search functionality, OpenSearch® offers a powerful analytics engine able to perform summary calculations of your data, and extract statistics and metrics very rapidly. Results of these "aggregations" can be then visualised with OpenSearch Dashboards.

Aggregations can be divided into three groups:

* **metric aggregation** performs simple calculations on values extracted from the fields of the documents, for example finding minimum or maximum value, calculating average or collecting statistics about field values.

* **bucket aggregation** distributes documents over a set of buckets based on provided criteria. For example, based on predefined ranges of values or based on how often a value is encountered in a field. Bucket aggregation is also used to create histograms.

* **pipeline aggregations** combine several aggregations in a way that allows using a result of one aggregation as an intermediate step to create a refined output. With pipeline aggregations you can build moving averages, cumulative sums and perform a variety of other mathematical calculations over the data in your documents.
