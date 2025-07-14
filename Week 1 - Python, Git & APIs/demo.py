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
print(img_tag['src'])

if img_tag and img_tag.get('src'):
    img_url = urljoin(webapage_url, img_tag['src'])

    # download the image
    img = requests.get(img_url)
    if img.status_code == 200:
        file_path = os.path.join(os.path.dirname(__file__), 'downloaded_image.png')
        with open(file_path, 'wb') as f:
            f.write(img.content)
        print(f"Image downloaded successfully and saved to {file_path}")
    else:
        print(f"Failed to download image, status code: {img.status_code}")
else:
    print("No image found on the webpage.")
