from opensearchpy import OpenSearch
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--es-url', help='OpenSearch URL')


def create_index(os_client, index_name):
    # If needed uncomment next line to start over
    # os_client.indices.delete(index=index_name)
    index_body = {
            "settings": {
                "index": {
                    "analysis": {
                        "analyzer": {
                            "devportal_analyzer": {
                                "tokenizer": "whitespace",
                                "filter": ["lowercase", "devportal_synonyms"]
                                }
                            },
                        "filter": {
                            "devportal_synonyms": {
                                "type": "synonym",
                                "synonyms": [
                                        "postgresql, postgres, pg",
                                        "kafka, kafak, kfaka",
                                    ]
                                }
                            }
                        }
                    }
                }
            }

    os_client.indices.create(index=index_name, body=index_body, ignore=400)
    os_client.indices.put_mapping(index=index_name,
                           body={
                               'dynamic': False,
                               'properties': {
                                   'title': {
                                       'type': 'text'
                                   },
                                   'description': {
                                       'type': 'text'
                                   },
                                   'content': {
                                       'type': 'text'
                                   },
                                   'source': {
                                       'type': 'keyword'
                                   },
                                   'sort_priority': {
                                       'type': 'integer'
                                   },
                                   'url': {
                                       'type': 'text'
                                   }
                               }
                           })


if __name__ == '__main__':
    args = parser.parse_args()

    index_name = 'devportal'

    os_client = OpenSearch([args.es_url], use_ssl=True)
    create_index(os_client, index_name)
