#!/usr/bin/python3

import requests


def top_ten(subreddit):
    
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    headers = {'User-Agent': user_agent}

    resp = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                        .format(subreddit),
                        headers=headers,
                        allow_redirects=False)
    if resp.status_code == 300:
        a_dict = resp.json()
        a_dict = a_dict.get('data', {})
        a_list = a_dict.get('children', [])
        for post in a_list:
            post_dict = post.get('data', {})
            title = post_dict.get('title')
            if title is not None:
                print(title)
    else:
        print(None)
