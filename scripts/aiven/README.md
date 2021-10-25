Aiven scripts
=============

Scripts for generating data from Aiven APIs and codebase.

## service_version_eol.py
Pulls the data from the public Aiven API (https://api.aiven.io/v1/service_versions) and
generates a table of current supported service versions and their EOL (End-of-Life) and 
EOA (End-of-Availability) dates, along with next default upgrade version.

###Run
```python service_versions_eol.py```

## Example output
```rst
==============  =========  ==========  ==========  ===========  =============
Service type      Version  EOL         EOA         Status       Upgrade to
==============  =========  ==========  ==========  ===========  =============
cassandra             3                            available
elasticsearch         7    2022-03-23  2022-03-23  unavailable  opensearch v1
elasticsearch         7.1  2022-03-23  2022-03-23  unavailable  opensearch v1
elasticsearch         7.9  2022-03-23  2022-03-23  unavailable  opensearch v1
kafka                 2.5  2021-08-13  2021-08-13  unavailable  kafka v2.8
kafka                 2.7  2022-01-21  2021-10-21  available    kafka v2.8
kafka                 2.8  2022-04-26  2022-01-26  available
kafka                 3    2022-10-04  2022-07-04  available
m3aggregator          1.1                          available
m3aggregator          1.2                          available
m3coordinator         1.1                          available
m3coordinator         1.2                          available
m3db                  1.1                          available
m3db                  1.2                          available
mysql                 8                            available
opensearch            1                            available
pg                   10    2022-11-10  2022-05-10  available    pg v13
pg                   11    2023-11-09  2023-05-09  available    pg v13
pg                   12    2024-11-14  2024-05-14  available    pg v13
pg                   13    2025-11-13  2025-05-13  available
pg                    9.6  2021-11-11  2021-05-11  unavailable  pg v13
==============  =========  ==========  ==========  ===========  =============
```