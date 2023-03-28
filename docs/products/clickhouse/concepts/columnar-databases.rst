ClickHouse® as a columnar database
==================================

Learn how columnar databases handles data and what benefits this approach has. Check out characteristics and capabilities of ClickHouse® as a columnar database.

Fast data reading
-----------------

Compared to traditional row-oriented solutions, columnar database management systems store data tables by columns to provide better performance and efficiency in certain applications. As a truly columnar database, ClickHouse® also stores the values of the same column physically next to each other. This further increases the speed of retrieving the values of a column. However, it also makes it slower to retrieve complete rows, as the values of a single row are stored across different physical locations.

Enhanced query performance
--------------------------

Storing the data of each column independently minimizes disk access and improves query performance by reading only the data columns that are relevant to a specific query.

Data compression and queries aggregation
----------------------------------------

This storage approach also provides better options for data compression, for example by the ability to better utilize similarities between adjacent data. Columnar databases are also better at aggregating queries that involve large sets of data. 

Massive and complex read operations
-----------------------------------

Columnar databases such as ClickHouse are therefore best suited for analytical applications that require big data processing or data warehousing, as these usually involve fewer write operations but more - or more complex - read operations that focus on subsets of the stored data. However, applications where queries mainly affect entire rows in the data tables are less efficient in columnar databases.
