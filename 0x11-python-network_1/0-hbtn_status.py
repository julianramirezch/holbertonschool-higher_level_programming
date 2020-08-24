#!/usr/bin/python3
''' Python script that fetches https://intranet.hbtn.io/status '''
import urllib.request as ur


def fetch_url(url):
    ''' Function fetch url '''
    with ur.urlopen(url) as response:
        html = response.read()

    return html


if __name__ == "__main__":
    html = fetch_url('https://intranet.hbtn.io/status')
    print('Body response:')
    print('    - type: {}'.format(html))
    print('    - content: {}'.format(html))
    print('    - utf8 content: {}'.format(html.decode('utf-8')))