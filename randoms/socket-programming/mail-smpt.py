from dotenv import load_dotenv
import os

# SMPT protocol
import smtplib

# Socket Programming
import socket

from urllib.request import urlopen

# regax
import re as r

load_dotenv()
GMAIL_USERNAME = os.getenv("GMAIL_USERNAME")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")

print(GMAIL_USERNAME)
print(GMAIL_PASSWORD)

s = socket.getaddrinfo(socket.gethostname(), None)

hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)

print("Your Computer Name is:", hostname)
print("Your Computer IP Address is:", ip_addr)

# ipconfig for linux, mac = ifconfig
# Extra 0 is the exit status of command when it completes successfully
# print(os.system("ifconfig"))

# Request external webservice to retrieve public ip address
# data = str(urlopen("http://checkip.dyndns.com/").read())
# ip = r.compile(r"Address: (\d+\.\d+\.\d+\.\d+)").search(data).group(1)
#
# print("Your Public IP Address is:", ip)
# print(os.system("curl -s ifconfig.me"))
# print(os.system("curl -s ipinfo.io/ip"))

# os won't capture stdout or stderr, if you want to capture them use subprocess
import subprocess

output = subprocess.check_output(["ifconfig"])
output = subprocess.check_output(["curl", "-s", "ifconfig.me"])
# b = sequence of bytes
output = output.decode().strip()
print(output)
# shell=True unsafe if part of command comes from user input
output = subprocess.check_output("curl -s ifconfig.me", shell=True)
output = output.decode().strip()
print(output)

# 587 = TLS Provider, 465 = SSL Provider
# server = smtplib.SMTP("smtp.gmail.com", 587)

# Start the service
# server.ehlo()
# gmaile tls
# server.starttls()

# if (GMAIL_USERNAME is not None) and (GMAIL_PASSWORD is not None):
#     server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
#     print("We're in Baby")
