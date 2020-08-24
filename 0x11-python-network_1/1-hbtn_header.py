#!/usr/bin/python3
''' Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.'''

import urllib.request as ur
from sys import argv


def fetch_url(url):
    ''' Function fetch url'''
    with ur.urlopen(url) as response:
        html = response.info()

    return html


if __name__ == "__main__":
    html = fetch_url(argv[1])
    print(html.get('X-Request-Id'))
