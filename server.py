import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = '192.168.1.104'
port = 3001

serversocket.bind((host, port))
serversocket.listen(5)

print("Server listening on", host, port)

while True:
    clientsocket, address = serversocket.accept()
    print("received connection from", address)
    clientsocket.send(b"hi")
    clientsocket.close()
