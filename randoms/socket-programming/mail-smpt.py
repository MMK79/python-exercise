# need to be installed
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


def get_ip_with_socket():
    s = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)
    print(s[4][0])

    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)

    print("Your Computer Name is:", hostname)
    print("Your Local Computer IPv4 Address is:", ip_addr)
    print("Your Local Computer IPv6 Address is:", ip_addr)


def get_ip_with_os():
    # ipconfig for linux, mac = ifconfig
    # Extra 0 is the exit status of command when it completes successfully
    print(os.system("ifconfig"))


def get_public_ip_external_webservice():
    # Request external webservice to retrieve public ip address
    data = str(urlopen("http://checkip.dyndns.com/").read())
    ip = r.compile(r"Address: (\d+\.\d+\.\d+\.\d+)").search(data).group(1)  # pyright: ignore

    print("Your Public IP Address is:", ip)
    # 403 for Iran
    print(os.system("curl -s ifconfig.me"))
    # work for Iran
    print(os.system("curl -s ipinfo.io/ip"))


def capture_cli_result():
    # os won't capture stdout or stderr, if you want to capture them use subprocess
    import subprocess

    output = subprocess.check_output(["ifconfig"])
    output = subprocess.check_output(["curl", "-s", "ifconfig.me"])
    output = subprocess.check_output(["curl", "-s", "ipinfo.io/ip"])
    # b = sequence of bytes
    output = output.decode().strip()
    print(output)
    # shell=True unsafe if part of command comes from user input
    output = subprocess.check_output("curl -s ifconfig.me", shell=True)
    output = output.decode().strip()
    print(output)


def monitor_ip():
    import time
    import subprocess

    # Monitoring IP with and without vpn
    while True:
        output = subprocess.check_output(["curl", "-s", "ipinfo.io/ip"])
        output = output.decode().strip()
        print(f"ipinfo.io result: {output}")
        output = subprocess.check_output(["curl", "-s", "ifconfig.me"])
        output = output.decode().strip()
        print(f"ifconfig.me result: {output}")
        time.sleep(1)


def get_wireless_ip():
    # need to be installed
    import netifaces

    # Lits all available network interfaces
    for iface in netifaces.interfaces():
        if "wi-fi" in iface.lower() or "wlan" in iface.lower():
            addrs = netifaces.ifaddresses(iface).get(netifaces.AF_INET)
            if addrs:
                print("Your Wireless NIC IP Address is:", addrs[0]["addr"])
                break
        else:
            print("Wireless IP not found.")


def gmail_smtp():
    # 587 = TLS Provider, 465 = SSL Provider
    server = smtplib.SMTP("smtp.gmail.com", 587)

    # Start the service
    server.ehlo()
    # gmaile tls
    server.starttls()

    if (GMAIL_USERNAME is not None) and (GMAIL_PASSWORD is not None):
        server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        print("We're in Baby")


if __name__ == "__main__":
    get_ip_with_socket()
