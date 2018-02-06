import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,
                 site):
        self.site = site

    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        parser = "html.parser"
        soup_parser = BeautifulSoup(html, parser)
        for tag in soup_parser.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

news = "https://news.google.com/"
Scraper(news).scrape()
