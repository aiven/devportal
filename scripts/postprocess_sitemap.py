from bs4 import BeautifulSoup

with open('./_build/html/sitemap.xml', 'r') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'lxml')

urls = soup.find_all('loc')

for url in urls:
    text = url.string
    # Skip the 404 page and the genindex page
    if '404' in text or 'genindex' in text:
        continue
    if text.endswith('index.html'):
        url.string = text[:-10]  # removes the "index.html"
    elif text.endswith('.html'):
        url.string = text[:-5]  # removes the ".html"

# Remove all URLs that contain '404' or 'genindex'
urls = [url for url in urls if '404' not in url.string and 'genindex' not in url.string]

with open('./_build/html/sitemap.xml', 'w') as f:
    for url in urls:
        f.write(str(url))