#!/usr/bin/python3
''' Python script that fetches https://intranet.hbtn.io/status '''

import requests


def requests_url(url):
    ''' Request url '''
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    content = requests_url('https://intranet.hbtn.io/status')
    print('Body response:')
    print('    - type: {}'.format(type(content)))
    print('    - content: {}'.format(content))
