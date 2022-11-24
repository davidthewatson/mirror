from requests_html import HTMLSession 


def scrape( url=None):
    print(url)
    session = HTMLSession()
    r = session.get(url)
    [scrape(url=link) for link in sorted(r.html.absolute_links) if url in link and link != url]

if __name__ =="__main__":
    scrape('https://davidwatson.org/')
