Formats for ClickHouse®-Kafka® data exchange
======================================================

When connecting ClickHouse® to Kafka® using Aiven integrations, data exchange is possible with the following formats only:

============================     ====================================================================================
Format name                      Notes
============================     ====================================================================================
Avro                             Only supports binary Avro format with embedded schema.

                                 Libraries and documentation: https://avro.apache.org/
CSV                              Example: ``123,"Hello"``
JSONASString                     Example: ``{"x":123,"y":"hello"}``
JSONCompactEachRow               Example: ``[123,"Hello"]``
JSONCompactStringsEachRow        Example: ``["123","Hello"]``
JSONEachRow                      Example: ``{"x":123,"y":"hello"}``
JSONStringsEachRow               Example: ``{"x":"123","y":"hello"}``
MsgPack                          Example: ``{\xc4\x05hello``

                                 Libraries and documentation: https://msgpack.org/
TSKV                             Example: ``x=123\ty=hello``
TSV                              Example: ``123\thello``
TabSeparated                     Example: ``123\thello``
============================     ====================================================================================
