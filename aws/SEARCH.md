# Aiven Docs custom search

Aiven Docs uses custom OpenSearch based search. The files related to the search are:

- the search results page [\_templates/search.html](_templates/search.html)
- the search form for the sidebar [\_templates/sidebar/search.html](_templates/sidebar/search.html)
- the AWS function that is used by the search results page [aws/src/handlers/search.js](aws/src/handlers/search.js)
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
            "type": "integer"
        }
    }
    }
}
```

| Property      | Description                                                                                                                                           |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| title         | Document title, used as the link text in search results                                                                                               |
| description   | Short document description, used in help center results under the title text                                                                          |
| content       | Main document content                                                                                                                                 |
| source        | Document source, currently either `devportal` or `helpcenter`                                                                                         |
| sort_priority | Document sort priority in search results, smaller priority documents are shown first and same priority documents are sorted by OpenSearch query score |

In addition to these `url` field should be provided with every document but it is not indexed or used in search queries. `url` is used in search result `href`.

## Search function

The OpenSearch® index is used through the AWS Lambda in [aws/src/handlers/search.js](aws/src/handlers/search.js). To call the function, make a GET request to the function URL and append your search term to the `query` parameter, like this: [https://docs.aiven.io/search.html?query=redis](https://docs.aiven.io/search.html?query=redis).

The query uses this overall approach:

- use OR-style query matching `title`, `description` and `content` (with OS `match_phrase_prefix`)
- give higher value to `title`

# Creating the index

The index is created with [scripts/create_index.py](scripts/create_index.py). You can run it with

```
make create-index ES_URL=https://opensearch-url/here
```

This can be run multiple times and has to be run at least once before the other commands that add documents to the index.

The index name in OpenSearch® is `devportal`.

# Docs page indexing

Pages are indexed with [scripts/index_developer_portal_pages.py](scripts/index_developer_portal_pages.py).
The script parses built HTML files using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
and extracts document title from `title` element and document content from `main` element child that has a `content` class (CSS selector `main .content`).

Pages that we do not want to be indexed can be added to `INDEX_BLACKLIST` list in [scripts/index_developer_portal_pages.py](scripts/index_developer_portal_pages.py).

You can run the script with

```
make index-devportal ES_URL=https://opensearch.url/here
```

# Help Center page indexing

Intercom pages are indexed with [scripts/index_help_center_pages.py](scripts/index_help_center_pages.py).
The script fetches HTTP pages from [https://help.aiven.io/](https://help.aiven.io/) and parses them using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

You can run the script with

```
make index-helpcenter ES_URL=https://opensearch.url/here
```

## Adding documents to the index using Python

Using `opensearchpy` library:

```python
import hashlib
from opensearchpy import OpenSearch

# Create the client instance
os_client = OpenSearch(['https://opensearch.url/here'], use_ssl=True)

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
os_client.index(index='devportal',
         body=document,
         id=hashlib.sha256(page['url'].encode("utf-8")).hexdigest())
```

You might also need to take care of removing documents that no longer exist.

# Synonyms

If you want to alias one search term to another, then you can update the file `scripts/synonyms.json` with comma-separated lists of aliases. For example:

```
[
     "postgresql, postgres, pg",
     "kafka, kafak, kfaka"
]
```

Note the lack of a trailing comma on the final term; this file must be valid JSON.

The aliases are used at index-creation time, so if this file changes then the index needs to be re-created before it will take effect.

# Testing changes to search functionality

## Preparations

1. Create an OpenSearch® service on Aiven, copy the URL and then set it as the environment `ES_URL` in `aws/env.local.json`
2. Run `make create-index` and then `make index-helpcenter` and `make index-devportal` to populate the OpenSearch® data (you can go browse with OpenSearch® dashboards at this point if you're interested)
3. Follow the workflow as noted in [here](https://github.com/aiven/devportal/tree/feature/use-aws/devportal-aws#workflow) to test further after making changes.

## Development

### One time testing

Following the instructions [here](https://github.com/aiven/devportal/tree/feature/use-aws/aws#development) one should have a `event.SearchFunction.local.json` after running `npm run generate-event GET SearchFunction`. It looks like this

```
{
	  "body": "eyJ0ZXN0IjoiYm9keSJ9",
      "resource": "/{proxy+}",
      "path": "/path/to/resource",
      "httpMethod": "GET",
      "isBase64Encoded": true,
      "queryStringParameters": {
        "foo": "bar"
      },
}
```

To invoke this API with valid parameters, one should edit the `queryStringParameters` to contain a valid parameter for the API e.g `"query": "kafka"`

### Continuous testing

Another way for continuous testing is to have a `env.local.json` with `ES_URL` filled. Then one can run `npm run watch` and `npm run start` (in different terminals) and test it with Postman or other API testing tools.

## Gotchas

- I ran `npm run generate-event GET SearchFunction` and `npm run invoke SearchFunction`. Terminal gave an error saying something about `ERROR ResponseError: x_content_parse_exception`?
  - It's likely you haven't modified the `event.SearchFunction.local.json`to give a proper parameter to the API. In the field `queryStringParameters` there, try supplying some valid parameter like `"query": "kafka"`
