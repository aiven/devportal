from bs4 import BeautifulSoup

with open('./_build/html/sitemap.xml', 'r') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'xml')

urls = soup.find_all('url')

for url in urls:
    loc = url.find('loc')
    text = loc.string
    # Remove the 'gen' and '404' pages
    if '404' in text:
        url.decompose()
        continue
    if text.endswith('/genindex.html'):
        loc.string = text[:-5]  # removes the ".html"
    elif text.endswith('/index.html'):
        loc.string = text[:-10]  # removes the "index.html"
    elif text.endswith('.html'):
        loc.string = text[:-5]  # removes the ".html"

with open('./_build/html/sitemap.xml', 'w') as f:
    f.write(str(soup))
