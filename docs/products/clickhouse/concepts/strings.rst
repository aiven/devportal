String data type in Aiven for ClickHouse®
=========================================

Aiven for ClickHouse® uses ClickHouse® databases, which can store diverse types of data, such as decimals, boolean data type, or arrays. This article focuses on strings and its usage in ClickHouse. Discover key functions and data type conversions required for working efficiently with strings in ClickHouse.

About strings in ClickHouse
---------------------------

ClickHouse allows strings of any length. Strings can contain an arbitrary amount of bytes, which are stored and output as-is. The string type replaces the types VARCHAR, BLOB, CLOB, and others from other database management systems (DBMS). When creating tables, numeric parameters for string fields can be set (for example, TEXT(140)) but are ignored.

ClickHouse supports the following aliases for strings: LONGTEXT, MEDIUMTEXT, TINYTEXT, TEXT, LONGBLOB, MEDIUMBLOB, TINYBLOB, BLOB, VARCHAR, CHAR.

String-handling functions
-------------------------

* `Functions for working with strings <https://clickhouse.com/docs/en/sql-reference/functions/string-functions/>`_

* `Functions for searching in strings <https://clickhouse.com/docs/en/sql-reference/functions/string-search-functions>`_

  .. note::
    
    By default, the search is case-sensitive in these functions, but case-insensitive search variants are also available.

* `Functions for searching and replacing in strings <https://clickhouse.com/docs/en/sql-reference/functions/string-replace-functions>`_

* `Functions for splitting and merging strings and arrays <https://clickhouse.com/docs/en/sql-reference/functions/splitting-merging-functions>`_

String conversions
------------------

Any plain string type can be cast to a different type using functions in `Type Conversion Functions <https://clickhouse.com/docs/en/sql-reference/functions/type-conversion-functions>`_.

Strings and JSON
----------------

ClickHouse supports a wide range of functions for working with JSON. With specific functions, you can use strings for extracting JSON.

.. seealso::
    
    Learn more on `JSON functions in ClickHouse <https://clickhouse.com/docs/en/sql-reference/functions/json-functions/>`_.

.. topic:: Examples

    ``visitParamExtractString(params, name)``
      Parse the string in double quotes.

    ``JSONExtractString(json[, indices_or_keys]…)``
      Parse a JSON and extract a string.

    ``toJSONString``
      Convert a value of any data type to its JSON representation.
