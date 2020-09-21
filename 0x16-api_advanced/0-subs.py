#!/usr/bin/python3
'''0. How many subs?'''
import requests


def number_of_subscribers(subreddit):
    '''queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0)\
    Gecko/20100101 Firefox/80.0'
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        jsoned_r = r.json()
        return jsoned_r.get('data').get('subscribers')
    else:
        return 0
