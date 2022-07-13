# python_repos.py

import requests

# Make the API call and save the response received.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'aplication/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Putting the API response in a variable.
response_dict = r.json()
print(f"Total count of the repositories: {response_dict['total_count']}")

# Processing info about the repositories.
repo_dicts = response_dict['items']
print(f'Count of the repositories returned: {len(repo_dicts)}')

# Analysis of the first repository.
repo_dict = repo_dicts[0]

print('\nSelected information about the first repository:')
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stargazers: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created at: {repo_dict['created_at']}")
print(f"Updated at: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")