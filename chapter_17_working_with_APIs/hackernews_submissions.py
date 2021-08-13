import requests
import json

# get request from hackernews API
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# create python dictionary of response
respose_dict = r.json()
readable_file = 'readable_hackernews_data.json'
with open(readable_file, 'w') as f:
    json.dump(respose_dict, f, indent=4)