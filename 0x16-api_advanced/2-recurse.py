#!/usr/bin/python3
'''2. Recurse it!'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit'''

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url = url + '?after={}'.format(after)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64;\
    x64; rv:80.0) Gecko/20100101 Firefox/80.0'
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return None

    after = r.json().get('data').get('after')

    for i in r.json().get('data').get('children'):
        hot_list.append(i.get('data').get('title'))

    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
