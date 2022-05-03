import socket
from _thread import *
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "172.22.203.111"
port = 2800

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")
pos = [0,0]
pos1 = [pos,pos]
currentId = "0"
def threaded_client(conn,pos):
    global currentId
    conn.send(pickle.dumps(currentId))
    currentId = "1"
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            print(data)
            pos1[pos] = data
            if not data:
                print("discconect")
                break
            else:
                if pos == 1:
                    reply = pos1[0]
                else:
                    reply = pos1[1]

                print("Received: ", data)
                print("Sending : ", reply)
                
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Connection Closed")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1