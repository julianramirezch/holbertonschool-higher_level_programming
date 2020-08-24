#!/usr/bin/python3
'''  Python script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter, and finally displays
the body of the response. '''

import requests
from sys import argv


def request_url(url, email):
    ''' Request url '''
    data = {'email': email}
    request = requests.post(url, data)

    return(request.content)


if __name__ == "__main__":
    response = request_url(argv[1], argv[2])
    print(response.decode('utf-8'))
