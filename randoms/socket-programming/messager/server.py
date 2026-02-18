import socket

# Creating multiple thread within one python program
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# socket.AF_INET -> we accepting ipv4 addresses for connection
# soket.SOCK_STREAM -> we streaming data
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding a server to an address
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # Blocking line of code -> We will not pass this line of code until we recieve a message
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            # Recieve actual message
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                print(f"[DISCONNECT] {addr} disconnected")
                connected = False
            else:
                print(f"[{addr} {msg}]")
                conn.send("Message Received".encode(FORMAT))
    conn.close()


def start():
    print("[STARTING] Server is starting...")
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        # it blocks -> it will wait until a new connection to the server -> when that happen, we store that connection
        # conn let you send data to the connected device
        conn, addr = server.accept()

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count() - 1}")


if __name__ == "__main__":
    start()
