import socket

HOST = "127.0.0.1"
PORT = 50001
ADDR = (HOST, PORT)
FORMAT = 'utf8'


def sendList(Client, list):

    for item in list:
        Client.sendto(item.encode(FORMAT))
        # cho phan hoi
        Client.recv(1024)

    data = "end"
    Client.sendto(data.encode(FORMAT), addr)


def recvList(Client):
    list = []

    item = Client.recv(1024).decode(FORMAT)

    while (item != "end"):

        list.append(item)
        # response
        Client.sendto(item.encode(FORMAT), addr)
        item = Client.recv(1024).decode(FORMAT)
    return list


Client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
list = ["HO CHI MINH CITY", "VIETNAM", "ASIA"]
print("Client is connected to server")
Client.sendto("Hello".encode(FORMAT), ADDR)
Client.recv(1024)
message = ""
while True:
    data = input("Enter your message: ")    
    
    if data =="list":
        while message != "end":
            message = message.encode(FORMAT)
            Client.sendto("list".encode(FORMAT), ADDR)
            message = Client.recv(1024)
            print(message.decode(FORMAT))
            message = message.decode(FORMAT)

    message = ""    
    Client.sendto(data.encode(FORMAT), ADDR)
    
    if data == "exit":
        break
    else:
        data = Client.recv(1024).decode(FORMAT)
        print(data)


Client.close()
print("Client is disconnected from server")