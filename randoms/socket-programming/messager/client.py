import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    # We need to convert the length of the message to 64 byte
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))


def chat():
    while True:
        msg = input()
        if msg == DISCONNECT_MESSAGE:
            print("You are getting disconnected")
            send(msg)
            break
        else:
            send(msg)
    print("You are disconnected")


if __name__ == "__main__":
    chat()
