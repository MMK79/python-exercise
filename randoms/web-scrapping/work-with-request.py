import requests

# r = requests.get("https://xkcd.com/353/")
# print(r)
# functions = dir(r)
# print the html of the site
# print(r.text)

# r = requests.get("https://imgs.xkcd.com/comics/python.png")

# print bytes of the image
# print(r.content)

# wb = write byte
# with open("comic.png", "wb") as f:
#     f.write(r.content)

# check the status code
# print(r.status_code)
# return True for response less than 400
# print(r.ok)
# information about site
# print(r.headers)

# payload = {"page": 2, "count": 25}
# r = requests.get("https://httpbin.org/get", params=payload)

# print(r.text)
# print(r.url)

# post data
# check the html structure so you understand form and see what that site accept
# payload = {"username": "masuod", "password": "test"}
# r = requests.post("https://httpbin.org/post", data=payload)

# print(r.text)
# Create python dictionary of json response
# r_dict = r.json()
# print(r.json())

# Basic Auth
# r = requests.get("https://httpbin.org/basic-auth/masuod/test", auth=("masuod", "test"))
# print(r)
# print(r.text)
# r = requests.get(
#     "https://httpbin.org/basic-auth/masuod/test", auth=("masuod", "testing")
# )
# print(r)
# print(r.text)

# Test delay
# try:
#     r = requests.get("https://httpbin.org/delay/4", timeout=3)
#     print(r)
# except requests.ReadTimeout as e:
#     print("Time out error")
