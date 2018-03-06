import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.tvn24.pl/rss.html")
soup = BeautifulSoup(page.text, "html.parser")


rss_link_list = soup.find(class_='podcast')

rss_link_list_items = rss_link_list.find_all(class_='rssLink')

for rss_link in rss_link_list_items:
    print(rss_link)
