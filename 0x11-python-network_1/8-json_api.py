#!/usr/bin/python3
''' Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.'''

import requests
from sys import argv


def request_url(url, letter):
    ''' Function request url '''
    request = requests.get(url, data={'q': letter})

    return request.content

if __name__ == "__main__":
    q = ''
    if argv[1]:
        q = argv[1]
    response = request_url('http://0.0.0.0:5000/search_user', q)
    print(response)
