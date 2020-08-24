#!/usr/bin/python3
''' Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8). '''

import urllib.request
from sys import argv


def fetch_url(url):
    ''' Function fetch url '''
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
            print('Error code: {}'.format(error.code))


if __name__ == "__main__":
    fetch_url(argv[1])
