from bs4 import BeautifulSoup
from requests_html import HTMLSession 


def scrape(scheme='https', delimiter='://', site=None, path=None, url=None):
    url = url or f'{scheme}{delimiter}{site}{path}'
    print(url)
    session = HTMLSession()
    r = session.get(url)
    [scrape(url=link) for link in sorted(r.html.absolute_links) if url in link and link != url]

if __name__ =="__main__":
    scheme = 'https'
    delimiter = '://'
    site = 'davidwatson.org'
    path = '/'
    scrape(scheme, delimiter, site, path)
