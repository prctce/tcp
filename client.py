import socket

TCP_IP = socket.gethostbyname(socket.gethostname())
TCP_PORT = 5005
ADDR = (TCP_IP, TCP_PORT)
BUFFER_SIZE = 1024
FORMAT = "utf-8"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[INFO] Client connected to server at {TCP_IP}:{TCP_PORT}")

    connected = True
    while connected:
        msg = input("> ")

        client.send(msg.encode(FORMAT))

        if msg == "!exit":
            connected = False
        else:
            msg = client.recv(BUFFER_SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")

if __name__ == "__main__":
    main()