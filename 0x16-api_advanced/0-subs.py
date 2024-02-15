#!/usr/bin/python3

"""
contains a function that return the number of subcribers from reddit API
"""

import requests

def number_of_subscribers(subreddit):
     
    #read credentials
    file_path = 'credentials.txt'
    credentials = []
    with open(file_path, 'r') as file:
        for line in file:
            username, password = line.strip().split(",")
            credentials.append((username, password))

    
    CLIENT_ID = credentials[0][0]
    SECRET_KEY = credentials[0][1]
    username = credentials[1][0]
    password = credentials[1][1]
    
    headers = {"User-Agent": "0-subs/1.0"}
    
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    data = {
            "grant_type": "password",
            "username": username,
            "password": password,
    }

    res = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)
    Token = res.json()["access_token"]
    headers["Authorization"] = f"bearer {Token}"
    

    response = requests.get(f"https://oauth.reddit.com/r/{subreddit}/about.json", headers=headers)
    if (response.status_code == 200):
        return (response.json()["data"]["subscribers"])
    else:
        return (0)
