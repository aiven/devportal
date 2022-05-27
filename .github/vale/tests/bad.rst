.. This file should give (at least?) one Vale error or warning per line.
   (``vale --output=line`` is assumed)
   Lines should correspond to those in good.txt
   At some point this will probably be split into multiple files

clickhouse                              -- capitalisation
Clickhouse                              -- capitalisation

flick                                   -- spelling
influx                                  -- common replacement
influxdb                                -- spelling
kakfa                                   -- spelling
kafka                                   -- case
multicloud                              -- hyphenation
postgesql                               -- spelling
postgres                                -- full name
postgreSql                              -- case
timeseries                              -- should be two words

Apache Nonesuch                         -- wants ® first word -- NOT DETECTED YET
Apache Flink                            -- wants ® after second word

MirrorMaker2                           -- ``MirrorMaker 2`` with a space

--------

``literal-text`` MirrorMaker2             -- this is NOT found

``literal text`` MirrorMaker2             -- this IS found
