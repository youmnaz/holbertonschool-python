#!/usr/bin/python3
"""
    10-my_github.py
"""

import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passw = argv[2]
    r = requests.get('https://api.github.com/user', auth=(user, passw))
    print(r.json().get("id"))
