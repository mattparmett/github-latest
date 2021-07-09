import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    events = requests.get("https://api.github.com/users/{}/events".format(username)).json()
    print("First event for user {} created at {}".format(username, events[0]['created_at']))