#!/usr/bin/python3
'''  Python script that takes 2 arguments and list 10 last commits '''

import requests
from sys import argv


def get_commits(repo, owner):
    ''' Function get commits '''
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, owner)
    r = requests.get(url)
    commits = 10

    for i in r.json():
        print('{}: {}'.format(i.get('sha'), i.get('commit').get('author')
              .get('name')))
        commits -= 1
        if commits == 0:
            break


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    get_commits(repo, owner)
