#!/usr/bin/python3
''' Python script that takes in 3 strings and sends a search request to the
Twitter API '''

import requests
from sys import argv
import base64

if __name__ == "__main__":
    consumer_key = argv[1]
    consumer_secret = argv[2]

    key = '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')
    b64_key = base64.b64encode(key)
    b64_key = b64_key.decode('ascii')

    url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(url)

    headers = {
        'Authorization': 'Basic {}'.format(b64_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }

    data = {
        'grant_type': 'client_credentials'
    }

    r = requests.post(auth_url, headers=headers, data=data)
    print(r.status_code)
    access_token = r.json().get('access_token')

    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    search_params = {
        'q': argv[3],
        'result_type': 'mixed',
        'count': 15
    }

    search_url = 'https://api.twitter.com/1.1/search/tweets.json'
    search_resp = requests.get(search_url, headers=search_headers,
                               params=search_params)
    print(search_resp.status_code)

    tweet_data = search_resp.json()
    statuses = tweet_data.get('statuses')
    count = 5
    for tuit in statuses:
        print('[{}] {} by {}'.format(tuit.get('id'), tuit.get('text'),
              tuit.get('user').get('name')))
        count -= 1
        if count == 0:
            break
