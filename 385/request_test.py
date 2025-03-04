import sys

import requests
import bs4

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get("https://usm.maine.edu", headers=headers)
print(response.header.get("location"))



soup = bs4.BeautifulSoup(response.text, "html.parser")

divs = soup.select("div")