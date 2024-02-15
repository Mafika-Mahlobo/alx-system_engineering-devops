#!/usr/bin/python3

"""
returns a list containing the titles of all hot articles for a given subreddit recursively.
"""

import requests
from read_credentials import read_file

def recurse(subreddit, hot_list=None):

    if hot_list is None:
        hot_list = []

    path = "credentials.txt"

    CLIENT_ID = read_file(path)[0][0]
    SECRET_KEY = read_file(path)[0][1]
    username = read_file(path)[1][0]
    password = read_file(path)[1][1]

    headers = {"User-Agent": "1-top_ten/1.0"}

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

    data = {
        "grant_type": "password",
        "username": username,
        "password": password
    }

    res = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)
    Token = res.json()["access_token"]
    headers["Authorization"] = f"bearer {Token}"

    response = requests.get(f"https://oauth.reddit.com/r/{subreddit}/hot", headers=headers)

    if response.status_code == 200:
        data = response.json()["data"]
        children = data.get("children", [])

        for child in children:
            hot_list.append(child["data"]["title"])

        after = data.get("after")
        if after:
            recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None
