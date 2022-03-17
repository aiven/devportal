from bs4 import BeautifulSoup
from urllib.parse import urljoin
from opensearchpy import OpenSearch
import hashlib
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--es-url", help="OpenSearch URL")


def index_pages(os_client, index_name, base_url):
    successes = []
    skips = []
    deletes = []
    fails = []

    response = requests.get(base_url)
    root = BeautifulSoup(response.content, "html.parser")
    collections = root.find_all("a", {"class": "paper"})

    for collection in collections:
        collection_url = urljoin(base_url, collection["href"])
        response = requests.get(collection_url)
        collection = BeautifulSoup(response.content, "html.parser")
        articles = collection.find_all("a", {"class": "paper"})

        for article in articles:
            article_url = urljoin(base_url, article["href"])
            try:
                response = requests.get(article_url)

                if not response.url.startswith(base_url):
                    skips.append((article_url, response.url))
                    continue

                article = BeautifulSoup(response.content, "html.parser")
                title = article.find("h1").text
                description = article.find("div", {"class": "article__desc"}).text
                content = article.find("article").text

                page = {
                    "title": title,
                    "description": description,
                    "content": content,
                    "url": article_url,
                    "source": "helpcenter",
                    "sort_priority": 2,
                }

                os_client.index(
                    index=index_name,
                    body=page,
                    id=hashlib.sha256(page["url"].encode("utf-8")).hexdigest(),
                )

                successes.append(article_url)
            except Exception as e:
                fails.append((article_url, e))

    search_result = os_client.search(
        index=index_name,
        body={"query": {"term": {"source": "helpcenter"}}},
        _source=["url"],
        size=10000,
    )
    indexed_pages = search_result["hits"]["hits"]
    all_current_urls = successes + fails

    for page in indexed_pages:
        page_id = page["_id"]
        page_url = page["_source"]["url"]
        if page_url not in all_current_urls:
            os_client.delete(index=index_name, id=page_id)
            deletes.append(page_url)

    print("# INDEXED")
    print("\n".join(successes))
    print("# SKIPPED (REDIRECTS)")
    print("\n".join([f"{url} -> {redirect_url}" for (url, redirect_url) in skips]))
    print("# DELETED FROM INDEX")
    print("\n".join(deletes))
    print("# FAILED TO INDEX")
    print("\n".join([f"{url} | {repr(error)}" for (url, error) in fails]))


if __name__ == "__main__":
    args = parser.parse_args()

    index_name = "devportal"
    base_url = "https://help.aiven.io/en"

    os_client = OpenSearch([args.es_url], use_ssl=True)
    index_pages(os_client, index_name, base_url)
