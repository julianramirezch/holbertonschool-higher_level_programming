#!/usr/bin/python3
''' Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.'''

import requests
from sys import argv


def request_url(url, letter):
    ''' Function request url '''
    data = {'q': letter}
    request = requests.post(url, data=data)

    try:
        if len(request.json()) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(request.json().get('id'),
                                   request.json().get('name')))
    except Exception:
        print('Not a valid JSON')

if __name__ == "__main__":
    q = ''
    if len(argv) == 2:
        q = argv[1]
    response = request_url('http://0.0.0.0:5000/search_user', q)
