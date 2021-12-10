import socket

def recvList(server):
    list = []

    item = server.recv(1024).decode(FORMAT)

    while (item != "end"):

        list.append(item)
        #response
        server.sendto(item.encode(FORMAT),address)
        item = server.recv(1024).decode(FORMAT)
    

    return list

def sendList(server, list, address):

    for item in list:
        server.sendto(item.encode(FORMAT),address)
        #cho phan hoi
        server .recv(1024)
    
    message = "end"
    server.sendto(message.encode(FORMAT), address)


HOST = "127.0.0.1"
# SERVER_NAME = socket.gethostname()
# SERVER = socket.gethostbyname(SERVER_NAME)
global PORT
PORT = 50001
ADDR = (HOST, PORT)
FORMAT = 'utf8'
server = socket.socket(socket.AF_INET, socket. SOCK_DGRAM)
list1 = ["HA NOI", "VIETNAM" , "ASIA"]
server.bind(ADDR)  # tạo server tại ADDR này
print("Done")
# s.recvfrom(1024) # so luong byte nhan duoc
message, address = server.recvfrom(1024)
print(message.decode(FORMAT))
message = message.decode(FORMAT)  # cho quay ve kieu ky tu
server.sendto(message.encode(FORMAT), address)  # gửi lại cho client
while message != "exit":
    message, address = server.recvfrom(1024)
    print("client: ", message.decode(FORMAT))
    message = message.decode(FORMAT)
    if message == "exit":
        break
    elif message == "list":
        sendList(server, list1, address)
    else:
        message = "NULL"   
        server.sendto(message.encode(FORMAT), address)
server.close()
print("server dong")