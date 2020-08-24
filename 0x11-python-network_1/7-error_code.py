#!/usr/bin/python3
''' Python script that takes in a URL, sends a request to the URL and displays
the body of the response.'''

import requests
from sys import argv


def request_url(url):
    ''' Request url '''
    request = requests.get(url)
    if request.status_code == 200:
        print(request.content.decode('utf-8'))
    else:
        print('Error code: {}'.format(request.status_code))

if __name__ == "__main__":
    request_url(argv[1])
