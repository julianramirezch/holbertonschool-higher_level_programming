#!/usr/bin/python3
''' Python script that fetches https://intranet.hbtn.io/status '''
import urllib.request as ur

url = 'https://intranet.hbtn.io/status'
with ur.urlopen(url) as response:
    html = response.read()
    print('Body response:')
    print('    - type: {}'.format(type(response.read())))
    print('    - content: {}'.format(html))
    print('    - utf8 content: {}'.format(html.decode('utf-8')))
