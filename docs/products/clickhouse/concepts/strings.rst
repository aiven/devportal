String data type in Aiven for Clickhouse®
=========================================

ClickHouse databases can store diverse types of data, such as decimals, booleans, or arrays. This article focuses on strings and its usage in Aiven for ClickHouse. Discover key functions and data type conversions required for working efficiently with strings in Aiven for ClickHouse.

About strings in ClickHouse
---------------------------

Aiven for ClickHouse allows strings of any length. Strings can contain an arbitrary amount of bytes, which are stored and output as-is. The String type replaces the types VARCHAR, BLOB, CLOB, and others from other DBMSs. When creating tables, numeric parameters for string fields can be set (e.g. TEXT(140)), but are ignored.
Aiven for ClickHouse supports the following aliases for strings: LONGTEXT, MEDIUMTEXT, TINYTEXT, TEXT, LONGBLOB, MEDIUMBLOB, TINYBLOB, BLOB, VARCHAR, CHAR.

String handling functions
-------------------------

* `Functions for Working with Strings <https://clickhouse.com/docs/en/sql-reference/functions/string-functions/>`_

* `Functions for Searching in Strings <https://clickhouse.com/docs/en/sql-reference/functions/string-search-functions>`_
The search is case-sensitive by default in all these functions. There are separate variants for case insensitive search.

* `Functions for Searching and Replacing in Strings <https://clickhouse.com/docs/en/sql-reference/functions/string-replace-functions>`_

* `Functions for Splitting and Merging Strings and Arrays <https://clickhouse.com/docs/en/sql-reference/functions/splitting-merging-functions>`_

String conversions
------------------

Any plain string types can be cast to different types using functions in `Type Conversion Functions <https://clickhouse.com/docs/en/sql-reference/functions/type-conversion-functions>`_.

String and JSON
---------------

ClickHouse supports a wide range of functions for working with JSON. With specific functions, you can use strings for extracting JSON.

.. seealso::
    
    Learn more on `JSON functions in ClickHouse <https://clickhouse.com/docs/en/sql-reference/functions/json-functions/>`_.

.. topic:: Examples

    `visitParamExtractString(params, name)`​
    Parses the string in double quotes.

    `JSONExtractString(json[, indices_or_keys]…)`​
    Parses a JSON and extract a string.

    `toJSONString`
    Convert a value of any data type to its JSON representation.
