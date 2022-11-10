from usp.tree import sitemap_tree_for_homepage
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import requests


def index_pages(es, base_url):
    successes = []
    skips = []
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

                successes.append(article_url)
            except Exception as e:
                fails.append((article_url, e))

    if (os.getenv('INDEX_DEBUG')):
        print("# INDEXED")
        print("\n".join(successes))
        print("# SKIPPED (REDIRECTS)")
        print("\n".join([f"{url} -> {redirect_url}" for (url, redirect_url) in skips]))
        print("# FAILED TO INDEX")
        print("\n".join([f"{url} | {repr(error)}" for (url, error) in fails]))

    all_pages = successes + skips
    print("HELP Summary: {:d} help pages found, {:d} redirects, {:d} total".format(
        len(successes), len(skips), len(all_pages)))


if __name__ == "__main__":
    tree = sitemap_tree_for_homepage('https://docs.aiven.io')
    devportal_pages = sum(1 for _ in tree.all_pages())
    print("Aiven Developer sitemap page count: {:d}".format(devportal_pages))

    base_url = "https://help.aiven.io/en"
    es = ""

    index_pages(es, base_url)

