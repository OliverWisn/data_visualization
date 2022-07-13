# python_repos.py

import requests

# Make the API call and save the response received.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'aplication/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')
print(url)

# Putting the API response in a variable
response_dict = r.json()

# Processing the results.
print(response_dict.keys())