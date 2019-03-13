import socket
import sys

#Creates a basic Socket
def createSocket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error() as msg:
        print("ERROR CREATING SOCKET : " + str(msg))

#Binding the port to socket
def bindSocket():
    #try:
    global port
    global host
    global s
    print("Binding socket to port " + str(port))

    s.bind((host,port))
    s.listen(5)

    #except socket.error() as msg:
     #   print("ERROR BINDING SOCKET " + str(msg) + " Retrying...")
      #  bindSocket()

#Establish Connection with client and socket must be listening
def socketAccept():
    conn, add = s.accept()
    print("Connection successfull : " + " ip:" + add[0] + " port:" + str(add[1]))
    chat(conn)
    conn.close()


#function for chatting
def chat(conn):
    running = True
    while running:
        print("\n$")
        sendMessage = input()
        if sendMessage == "quit":
            running = False
        else:
            conn.send(str.encode(sendMessage))
            clientResponse = str(conn.recv(1024),"utf-8")
            print(clientResponse, end = "")



createSocket()
bindSocket()
socketAccept()
 