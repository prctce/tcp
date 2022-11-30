import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    msg = input("Enter message: ")
    s.send(msg.encode())

    data = s.recv(BUFFER_SIZE)
    sent = data.decode()
    print("Data sent:", sent)

s.close()
print(data)