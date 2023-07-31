from algoliasearch.search_client import SearchClient
import argparse
import glob
from bs4 import BeautifulSoup
import hashlib

parser = argparse.ArgumentParser()
parser.add_argument('--algolia-app-id', help='Algolia Application ID')
parser.add_argument('--algolia-api-key', help='Algolia Admin API Key')
parser.add_argument('--algolia-index-name', help='Algolia Index Name')
parser.add_argument('--html-build-dir', help='Sphinx HTML build directory')

# Path relative to build dir
INDEX_BLACKLIST = ["search.html", "genindex.html"]

def create_index(client, index_name):
    # Initialize your index
    index = client.init_index(index_name)

    # Configure the settings for your index
    settings = {
        'searchableAttributes': ['title', 'body'],
        'attributesForFaceting': ['facetingType'],
        'customRanking': ['desc(popularity)']
    }
    index.set_settings(settings)

def parse_pages(html_build_dir):
    pages = []

    for filepath in glob.iglob(html_build_dir + '/**/*.html', recursive=True):
        relative_path = filepath.replace(html_build_dir, "")
        full_path = ('https://docs.aiven.io' + relative_path).replace(".html", "").replace("/index", "")  # Remove .html and /index.html from the URL

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

            body = elements.text.strip()
            pages.append({
                'title': title,
                'subtitle': body[:160],
                'body': body,
                'slug': full_path,
                'facetingType': 'documentation',
                'popularity': 1,
                '_type': 'documentation',
                '__i18n_lang': 'en',
                'endDate_timestemp': '4845516182350', # 100 years ahead
                'objectID': hashlib.sha256(relative_path.encode("utf-8")).hexdigest()  # Use the URL hash as the objectID
            })

            print(f"Parsed {filepath}")

    return pages

def index_pages(client, index_name, pages):
    index = client.init_index(index_name)

    # Add new objects to the index or update existing ones
    index.save_objects(pages, {'autoGenerateObjectIDIfNotExist': True})

    print(f"Indexed {len(pages)} pages.")

if __name__ == '__main__':
    args = parser.parse_args()

    client = SearchClient.create(args.algolia_app_id, args.algolia_api_key)
    create_index(client, args.algolia_index_name)
    pages = parse_pages(args.html_build_dir)
    index_pages(client, args.algolia_index_name, pages)
