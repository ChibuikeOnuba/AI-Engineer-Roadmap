"""Please note that this script underwent various edits and my scope of 
practice is not limited to only the most recent changes."""

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

webapage_url = 'https://en.wikipedia.org/wiki/Bill_Gates'

r = requests.get(webapage_url)
soup = BeautifulSoup(r.text, 'html.parser')

# Find the first image in the webpage
img_tag = soup.find('img')

print(img_tag)