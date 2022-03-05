import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "oRBqX0o-AcuJCHdx28EySX3tlP-a3UV7ekmMNzxSztCAjiYoHVLhFdD0c-5mHHyp78vnUvpZM656N35XMOhSowikdb7g3HrASHe_gy9YVBFMnjY0Z-YxHQ4tu6AjYnYx"
headers = {
    "Authorization": "Bearer " + api_key
}
params = {
    "term": "Pizza",  # term = Keyword
    "location": "Altamonte Springs, FL"
}
response = requests.get(url, headers=headers, params=params)
print(response.text)
