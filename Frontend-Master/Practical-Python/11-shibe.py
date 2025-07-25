import requests

# api_url = "http://shibe.online/api/shibes?count=1"
#
# response = requests.get(api_url)
#
# print(f"Response status code is {response}")
#
# response_json = response.json()
#
# print(response_json)

api_url = "http://shibe.online/api/shibes"

params = {
   "count": 10
}

# Pass those params in with the request.
api_response = requests.get(api_url, params=params)

print(f"Shibe API Response Status Code is: {api_response.status_code}")  # should be 200 OK

json_data = api_response.json()

print("Here is a list of URLs for dog pictures:")
for url in json_data:
    print(f"\t {url}")
