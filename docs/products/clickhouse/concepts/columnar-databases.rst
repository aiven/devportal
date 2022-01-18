Columnar databases
===================

Compared to more traditional, row-oriented solutions, columnar database management systems store the data tables by columns to provide better performance and efficiency in certain applications.

Storing the data of each column independently minimizes disk access and improves query performance by reading only the data columns that are relevant to a specific query. This storage approach also provides better options for data compression, for example by the ability to better utilize similarities between adjacent data. Columnar databases are also better at aggregating queries that involve large sets of data. 

Columnar databases such as ClickHouse are therefore best suited for analytical applications that require big data processing or data warehousing, as these usually involve fewer write operations but more - or more complex - read operations that focus on subsets of the stored data. However, applications where queries mainly affect entire rows in the data tables are less efficient in columnar databases.
