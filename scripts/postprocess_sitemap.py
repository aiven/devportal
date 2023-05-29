from bs4 import BeautifulSoup

with open('./_build/html/sitemap.xml', 'r') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'lxml')

locs = soup.find_all('loc')

for loc in locs:
    text = loc.string
    if text.endswith('index.html'):
        loc.string = text[:-10]  # removes the "index.html"
    elif text.endswith('.html'):
        loc.string = text[:-5]  # removes the ".html"

with open('./_build/html/sitemap.xml', 'w') as f:
    f.write(str(soup))