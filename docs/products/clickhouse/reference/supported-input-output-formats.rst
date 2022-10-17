Formats for ClickHouse®-Kafka® data exchane
======================================================

When connecting ClickHouse® to Kafka® using Aiven integrations, data exchange is possible with the following formats only:

============================     ====================================================================================
Format name                      Example
============================     ====================================================================================
CSV                              ``123,"Hello"``
JSONASString                     ``{"x":123,"y":"hello"``
JSONCompactEachRow               ``[123,"Hello"]``
JSONCompactStringsEachRow        ``["123","Hello"]``
JSONEachRow                      ``{"x":123,"y":"hello"}``
JSONStringsEachRow               ``{"x":"123","y":"hello"}``
MsgPack                          ``{\xc4\x05hello``
TSKV                             ``x=123\ty=hello``
TSV                              ``123\thello``
TabSeparated                     ``123\thello``
============================     ====================================================================================
