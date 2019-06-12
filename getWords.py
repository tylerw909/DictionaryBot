import requests
import json

app_id = "c61f86ed"
app_key = "3619c026aab8720030520f80a85191be"
language = "en-gb"



word_id = "example"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
req = requests.get(url, headers={"app_id": "c61f86ed", "app_key": "3619c026aab8720030520f80a85191be"})



