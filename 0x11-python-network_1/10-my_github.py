#!/usr/bin/python3
''' Python script that takes your Github credentials (username and password)
and uses the Github API to display your id '''

import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def auth_github(user, passwd):
    ''' Function auth in github api '''
    url = 'https://api.github.com/user'
    r = requests.post(url, auth=HTTPBasicAuth(user, passwd))
    print(r.json().get('id'))


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    auth_github(user, passwd)
