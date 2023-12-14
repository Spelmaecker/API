import requests
import webbrowser
url = "https://moppenbot.nl/api/random/"
response = requests.get(url)
# data opvragen (kan handig zijn om de data eerst even te printen)

data = response.json()
joke = data['joke']['joke']
nsfw = input("Wil je een mopje horen?").lower
if nsfw == "ja":
    print("Dit je mopje:", joke)
else:
    print("Jammer, je krijgt er toch één:", joke)