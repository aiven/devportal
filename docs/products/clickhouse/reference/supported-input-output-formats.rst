Supported data formats for input and output
============================================

============================     ====================================================================================
Format name                      Example
============================     ====================================================================================
CSV                              ``123,"Hello"``
JSONCompactEachRow               ``[123,"Hello"]``
JSONCompactStringsEachRow        ``["123","Hello"]``
JSONEachRow                      ``{"x":123,"y":"hello"}``
JSONStringsEachRow               ``{"x":"123","y":"hello"}``
MsgPack                          ``{\xc4\x05hello``
TSKV                             ``x=123\ty=hello``
TSV                              ``123\thello``
TabSeparated                     ``123\thello``
============================     ====================================================================================
