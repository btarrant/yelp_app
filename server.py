import requests
import config

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "Pizza",  # term = Keyword
    "location": "Orlando, FL"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
names = [business["name"]
         for business in businesses if business["rating"] > 3.5]
print(names)
