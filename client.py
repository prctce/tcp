import socket, threading

TCP_IP = socket.gethostbyname(socket.gethostname())
TCP_PORT = 5006 
ADDR = (TCP_IP, TCP_PORT)
BUFFER_SIZE = 1024
FORMAT = "utf-8"
NICKNAME = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def receive():
    while True:
        try:
            message = client.recv(BUFFER_SIZE).decode(
                FORMAT)
            if message == 'NICKNAME':
                client.send(NICKNAME.encode(FORMAT))
            else:
                print(message)
        except:
            print("[INFO] An error occured!")
            client.close()
            break


def write():
    while True:
        message = '{}: {}'.format(NICKNAME, input(''))
        client.send(message.encode(FORMAT))


receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()