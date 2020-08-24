#!/usr/bin/python3
'''  Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header '''

import requests
from sys import argv


def request_url(url):
    ''' Request url'''
    request = requests.get(url)
    return request.headers

if __name__ == "__main__":
    header = request_url(argv[1])
    print(header.get('X-Request-Id'))
