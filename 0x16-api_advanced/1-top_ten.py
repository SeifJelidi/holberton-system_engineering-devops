#!/usr/bin/python3
'''1. Top Ten'''
import requests


def top_ten(subreddit):
    '''queries the Reddit API and returns the top 10
    hot posts listed for a given subreddit'''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64;\
    x64; rv:80.0) Gecko/20100101 Firefox/80.0'
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        jsoned_r = r.json()
        if jsoned_r.get('data').get('children') is None:
            print(None)
        for i in range(0, 10):
            print(jsoned_r.get('data').get('children')[i]
                          .get('data').get('title'))
    else:
        print(None)
