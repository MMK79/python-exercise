import requests
import os
from dotenv import load_dotenv

load_dotenv()

api = os.getenv("avalai")
authorization = "Bearer " + api

url = "https://api.avalai.ir/user/credit"
headers = {"Content-Type": "application/json", "Authorization": authorization}
response = requests.get(url, headers=headers)
print(response.json())
