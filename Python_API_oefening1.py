import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()

data = response.json()
title = data['title']
print(title)

completed = data['completed']

if completed == True:
    print("Goed gedaan")
else:
    print("Er moet nog gewerkt worden")
