#!/usr/bin/python3
'''  Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)'''

import urllib.request
import urllib.parse
from sys import argv


def fetch_url(url, email):
    ''' Fetch url '''
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf8')

    return html


if __name__ == "__main__":
    html = fetch_url(argv[1], argv[2])
    print(html)
