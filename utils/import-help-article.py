import argparse
import os
import requests
import sys
from urllib.parse import urlparse

import pypandoc
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description="Convert an existing help file")
parser.add_argument('url', help="The URL of the source file")
args = parser.parse_args()

page_url = args.url
print(page_url)

# tangent: grab a filename
url_pieces = urlparse(page_url)
path_pieces = os.path.split(url_pieces.path)
filename, ext = os.path.splitext(path_pieces[1])

# fetch web page
html_text = requests.get(page_url).text
soup = BeautifulSoup(html_text, 'html.parser')

attrs = {
    'class': 'article'
}
content = soup.find('div', attrs=attrs)
heading = content.find('h1')

# get the text, some tidying up needed
article = content.find('article')

# remove containers
for container in article.findAll('div', {'class': 'intercom-container'}):
    container.unwrap()

# download and replace images
image_counter = 1
for image in article.findAll('img'):
    src = image['src']

    img_path = urlparse(src)
    imgfile, ext = os.path.splitext(img_path.path)
    new_img_filename = filename + "_image" + str(image_counter) + ext

    img_data = requests.get(src).content
    with open(new_img_filename, 'wb') as handler:
        handler.write(img_data)

    image['src'] = new_img_filename
    image_counter = image_counter + 1

# output pretend HTML page
with open(filename + '.html', 'w+') as f:
    f.write(str(heading) + str(article))

f.close()

# have pandoc convert
output = pypandoc.convert_file(filename + '.html', 'rst', outputfile=filename + '.rst')
