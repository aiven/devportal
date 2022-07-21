import glob
from os import path
from bs4 import BeautifulSoup
from opensearchpy import OpenSearch
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--es-url', help='OpenSearch URL')
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
            elements = doc.select('div.article-container')[0]

            # remove tables of contents
            for toc in elements.select('div.toctree-wrapper'):
                toc.decompose()

            # remove header links
            for headerlink in elements.select('a.headerlink'):
                headerlink.decompose()

            # remove preamble links etc
            for backtotop in elements.select('a.back-to-top'):
                backtotop.decompose()

            for icons in elements.select('div.content-icon-container'):
                icons.decompose()

            content = elements.text
            pages.append({
                'title': title,
                'content': content.strip(),
                'url': relative_path,
                'source': 'devportal',
                'sort_priority': 1
            })

            print(f"Parsed {filepath}")

    return pages


def index_pages(os_client, index_name, pages):
    os_client.delete_by_query(index=index_name,
                       body={'query': {
                           'term': {
                               'source': 'devportal'
                           }
                       }})

    for page in pages:
        os_client.index(index=index_name,
                 body=page,
                 id=hashlib.sha256(page['url'].encode("utf-8")).hexdigest())
        print(f"Indexed {page['url']}")


if __name__ == '__main__':
    args = parser.parse_args()

    index_name = 'devportal'

    os_client = OpenSearch([args.es_url], use_ssl=True)
    pages = parse_pages(args.html_build_dir)
    index_pages(os_client, index_name, pages)