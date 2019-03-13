import socket

host = "10.2.38.40"
port = 9999

s = socket.socket()

s.connect((host,port))

running = True
while running:
    message = s.recv(1024)
    if message.decode("utf-8") == "quit":
        print("server has exited")
        running = False
    else:
        print(message.decode("utf-8"))
