import socket, threading

TCP_IP = socket.gethostbyname(socket.gethostname())
TCP_PORT = 5006
ADDR = (TCP_IP, TCP_PORT)
BUFFER_SIZE = 1024
FORMAT = "utf-8"
CLIENTS = []
NICKNAMES = []
print("[INFO] Server is starting...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print("[INFO] Server is started.")


def broadcast(message):
    for client in CLIENTS:
        client.send(message)
    
def handle(client):
    while True:
        try:
            message = client.recv(BUFFER_SIZE)
            broadcast(message)
            print(str(message, FORMAT))
        except:
            index = CLIENTS.index(client)
            CLIENTS.remove(client)
            client.close()
            nickname = NICKNAMES[index]
            broadcast(f"{nickname} left the chat!".encode(FORMAT))
            NICKNAMES.remove(nickname)
            break

def recv():
    while True:
        client, address = server.accept()
        print(f"[INFO] New connection: {str(address)}")
        print(f"[INFO] Active connections: {threading.active_count()}")
        client.send("NICKNAME".encode(FORMAT))
        nickname = client.recv(BUFFER_SIZE).decode(FORMAT)
        NICKNAMES.append(nickname)
        CLIENTS.append(client)
        print(f"[INFO] Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode(FORMAT))
        client.send("Connected to the server!".encode(FORMAT))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
recv()