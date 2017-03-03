import requests
r = requests.get(url='https://api.github.com/users/Edu-Glez/repos')
print(r.json())
