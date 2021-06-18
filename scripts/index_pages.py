import glob
from os import path
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from elasticsearch import Elasticsearch
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--es-url', help='Elasticsearch URL')
parser.add_argument('--html-build-dir', help='Sphinx HTML build directory')

# Path relative to build dir
INDEX_BLACKLIST = ["search.html", "genindex.html"]


def parse_pages(html_build_dir):
    pages = []

    for filepath in glob.iglob(path.join(html_build_dir, '**/*.html'),
                               recursive=True):

        relative_path = path.relpath(filepath, html_build_dir)

        if relative_path in INDEX_BLACKLIST:
            print(f"Skipping {filepath}")
            continue

        with open(filepath) as file:
            doc = BeautifulSoup(file.read(), 'html.parser')

            title = doc.title.text
            content = doc.select('main .content')[0].text

            pages.append({
                'title': title,
                'content': content.replace("¶", ""),
                'url': relative_path,
                'source': 'devportal'
            })

            print(f"Parsed {filepath}")

    return pages


def create_es_base(es, index_name):
    # If needed uncomment next line to start over
    # es.indices.delete(index=index_name)
    es.indices.create(index=index_name, ignore=400)
    es.indices.put_mapping(index=index_name,
                           body={
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
                                   'url': {
                                       'type': 'keyword'
                                   },
                                   'source': {
                                       'type': 'keyword'
                                   }
                               }
                           })


def index_pages(es, index_name, pages):
    es.delete_by_query(index=index_name,
                       body={'query': {
                           'term': {
                               'source': 'devportal'
                           }
                       }})

    for page in pages:
        es.index(index=index_name,
                 body=page,
                 id=hashlib.sha256(page['url'].encode("utf-8")).hexdigest())
        print(f"Indexed {page['url']}")


if __name__ == '__main__':
    args = parser.parse_args()

    index_name = 'devportal'

    es = Elasticsearch([args.es_url])
    create_es_base(es, index_name)
    pages = parse_pages(args.html_build_dir)
    index_pages(es, index_name, pages)