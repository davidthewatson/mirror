# Crawl site recursively using requests_html

import os
import re
import argparse

from requests_html import HTMLSession 


def save(site_root, html, fname):
    if fname == '':
        fname = 'index.html'
    if not os.path.exists(site_root):
        os.mkdir(site_root)
    f = open(f'{site_root}/{fname}', 'w')
    f.writelines(html)
    f.close()

def get_fname(r, url):
    fname = ''
    if "Content-Disposition" in r.headers.keys():
        fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
    else:
        fname = url.split("/")[-1]
    return fname

def scrape( url=None):
    site_root = url[url.find('//')+2:url.rfind('/')]
    session = HTMLSession()
    r = session.get(url)
    fname = get_fname(r, url)
    save(site_root, r.html.html, fname)
    [scrape(url=link) for link in sorted(r.html.absolute_links) if url in link and link != url]

if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('site', type=str, help='The site to mirror')
    args = parser.parse_args()
    scrape(args.site)
