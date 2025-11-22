import urllib.request

# this doesn't work, because it is on google drive
mnist_url = "https://drive.google.com/file/d/1eEKzfmEu6WKdRlohBQiqi3PhW_uIVJVP"
urllib.request.urlretrieve(mnist_url, "mnist.zip")
