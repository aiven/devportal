# Aiven Developer Portal custom search

Aiven Developer Portal uses custom Elasticsearch based search. The files related to the search are:

- the search results page [\_templates/search.html](_templates/search.html)
- the search form for the sidebar [\_templates/sidebar/search.html](_templates/sidebar/search.html)
- the Netlify function that is used by the search results page [netlify/functions/search/search.js](netlify/functions/search/search.js)
- the python script that creates the index and index mapping [scripts/create_index.py](scripts/create_index.py)
- the python script that parses and adds the Developer Portal pages to the index [scripts/index_developer_portal_pages.py](scripts/index_developer_portal_pages.py)
- the python script that fetches, parses and adds the Help Center pages to the index [scripts/index_help_center_pages.py](scripts/index_help_center_pages.py)

## Index mapping

The index is described with the following JSON:

```json
{
    "dynamic": false,
    "properties": {
        "title": {
            "type": "text"
        },
        "description": {
            "type": "text"
        },
        "content": {
            "type": "text"
        },
        "source": {
            "type": "keyword"
        },
        "sort_priority": {
            "type": "interger"
        }
    }
    }
}
```

| Property      | Description                                                                                                                                              |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| title         | Document title, used as the link text in search results                                                                                                  |
| description   | Short document description, used in help center results under the title text                                                                             |
| content       | Main document content                                                                                                                                    |
| source        | Document source, currently either `devportal` or `helpcenter`                                                                                            |
| sort_priority | Document sort priority in search results, smaller priority documents are shown first and same priority documents are sorted by Elasticsearch query score |

In addition to these `url` field should be provided with every document but it is not indexed or used in search queries. `url` is used in search result `href`.

## Search query

The Elasticsearch index is used through the Netlify function in [netlify/functions/search/search.js](netlify/functions/search/search.js). The exact query can be found in the file but the idea is:

- use OR-style query matching `title`, `description` and `content` (with ES `match_phrase_prefix`)
- give higher value to `title`

# Creating the index

The index is created with [scripts/create_index.py](scripts/create_index.py). You can run it with

```
make create-index ES_URL=https://es.url/here
```

This can be run multiple times and has to be run at least once before the other commands that add documents to the index.

The index name in Elasticsearch is `devportal`.

# Developer Portal page indexing

Developer Portal pages are indexed with [scripts/index_developer_portal_pages.py](scripts/index_developer_portal_pages.py).
The script parses built HTML files using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
and extracts document title from `title` element and document content from `main` element child that has a `content` class (CSS selector `main .content`).

Pages that we do not want to be indexed can be added to `INDEX_BLACKLIST` list in [scripts/index_developer_portal_pages.py](scripts/index_developer_portal_pages.py).

You can run the script with

```
make index-devportal ES_URL=https://es.url/here
```

# Help Center page indexing

Developer Portal pages are indexed with [scripts/index_help_center_pages.py](scripts/index_help_center_pages.py).
The script fetches HTTP pages from [https://help.aiven.io/](https://help.aiven.io/) and parses them using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

You can run the script with

```
make index-helpcenter ES_URL=https://es.url/here
```

## Adding documents to the index using Python

Using `elasticsearch` library:

```python
import hashlib
from elasticsearch import Elasticsearch

# Create the client instance
es = Elasticsearch(['https://elasticsearch.url/here'])

# Loop:

# Form the document that you want to index
document = {
    'title': 'How to use Kafka',
    'description': 'This guide will get you started with Kafka',
    'content': 'Long document...',
    'url': 'https://aiven.io/contact',
    'source': 'helpcenter',
    'sort_priority': 2,
}

# Send the document to the index
es.index(index='devportal',
         body=document,
         id=hashlib.sha256(page['url'].encode("utf-8")).hexdigest())
```

You might also need to take care of removing documents that no longer exist.