#!/usr/bin/python3
''' Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8). '''

import urllib.request
from sys import argv


def fetch_url(url):
    ''' Function fetch url '''
    with urllib.request.urlopen(url) as response:
        html = response.read()

    return html


if __name__ == "__main__":
    html = fetch_url(argv[1])
    print(html)