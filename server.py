import socket
import threading

TCP_IP = socket.gethostbyname(socket.gethostname())
TCP_PORT = 5005
ADDR = (TCP_IP, TCP_PORT)
BUFFER_SIZE = 1024
FORMAT = "utf-8"

def handle_client(conn, addr):
    print(f"[INFO] New connection: {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(BUFFER_SIZE).decode(FORMAT)
        if msg == "!exit":
            connected = False

        print(f"[{addr}] {msg}")
        msg = f"Msg received: {msg}"
        conn.send(msg.encode(FORMAT))

    conn.close()

def main():
    print("[INFO] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[INFO] Server is listening on {TCP_IP}:{TCP_PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"\n[INFO] Active connections: {threading.active_count() - 1}")
        
if __name__ == "__main__":
    main()