import requests
import webbrowser
input = input("Waarover wilt u iets vernemen?")
api_key = "53e41654f1f348859869b078c1ec4e8c"
url = f"https://newsapi.org/v2/everything?q={input.lower()}&apiKey={api_key}"
response = requests.get(url)
# data opvragen (kan handig zijn om de data eerst even te printen)
data = response.json()
artikels = data['articles']
# om de titels af te drukken
for article in artikels:
    print(article['title'])
