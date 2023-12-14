import requests
import webbrowser
url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(url)
# data opvragen (kan handig zijn om de data eerst even te printen)
data = response.json()
foto = data['message']
print(foto)
webbrowser.open(foto)
afbeelding = requests.get(foto)
with open(r"C:\Users\Davy\Python\API\fotohondje/test.jpg", "wb") as hond:
        hond.write(afbeelding.content)