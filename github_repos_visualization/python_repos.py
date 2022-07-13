# python_repos.py

import sys

import requests

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
	"""
	Replacing of the problematic characters with the replacement 
	characters.
	"""
	enc = file.encoding
	if enc == 'UTF-8':
		print(*objects, sep=sep, end=end, file=file)
	else:
		f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
		print(*map(f, objects), sep=sep, end=end, file=file)

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

print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
	print(f"\nName: {repo_dict['name']}")
	print(f"Owner: {repo_dict['owner']['login']}")
	print(f"Stargazers: {repo_dict['stargazers_count']}")
	print(f"Repository: {repo_dict['html_url']}")
	uprint(f"Description: {repo_dict['description']}")