from bs4 import BeautifulSoup
from urllib.parse import urljoin
from elasticsearch import Elasticsearch
import hashlib
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--es-url', help='Elasticsearch URL')


def index_pages(es, index_name, base_url):
    es.delete_by_query(index=index_name,
                       body={'query': {
                           'term': {
                               'source': 'helpcenter'
                           }
                       }})

    pages = []

    response = requests.get(base_url)

    root = BeautifulSoup(response.content, 'html.parser')
    collections = root.find_all('a', {'class': 'paper'})

    for collection in collections:
        collection_url = urljoin(base_url, collection['href'])
        response = requests.get(collection_url)
        collection = BeautifulSoup(response.content, 'html.parser')

        articles = collection.find_all('a', {'class': 'paper'})

        for article in articles:
            article_url = urljoin(base_url, article['href'])
            response = requests.get(article_url)
            article = BeautifulSoup(response.content, 'html.parser')

            title = article.find('h1').text
            description = article.find('div', {'class': 'article__desc'}).text
            content = article.find('article').text

            page = {
                'title': title,
                'description': description,
                'content': content,
                'url': article_url,
                'source': 'helpcenter',
                'sort_priority': 2
            }

            es.index(index=index_name,
                     body=page,
                     id=hashlib.sha256(
                         page['url'].encode("utf-8")).hexdigest())

            print(f"Indexed {page['url']}")

    return pages


if __name__ == '__main__':
    args = parser.parse_args()

    index_name = 'devportal'
    base_url = 'https://help.aiven.io/en'

    es = Elasticsearch([args.es_url])
    index_pages(es, index_name, base_url)
