from elasticsearch import Elasticsearch
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--es-url', help='Elasticsearch URL')


def create_index(es, index_name):
    # If needed uncomment next line to start over
    # es.indices.delete(index=index_name)
    es.indices.create(index=index_name, ignore=400)
    es.indices.put_mapping(index=index_name,
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
                                   }
                               }
                           })


if __name__ == '__main__':
    args = parser.parse_args()

    index_name = 'devportal'

    es = Elasticsearch([args.es_url])
    create_index(es, index_name)