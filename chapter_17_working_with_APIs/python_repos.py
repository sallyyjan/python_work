import requests

3 # Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# explicitly state to use github's API version 3
headers = {'Accept': 'application/vnd.github.v3+json'}
# making the call to the API using requests module
r = requests.get(url, headers=headers)
# check status code or request (status_code = 200 is successful)
print(f"Status code: {r.status_code}")

# Store response (use .json() to turn returned json into python dict)
response_dict = r.json()

# Process results.
print(response_dict.keys())
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned {len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")

