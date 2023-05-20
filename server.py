import socket
import _thread

s = socket.socket()

s.bind(('localhost',9999))

s.listen(100)
print('Waiting for connections')

usr={}

def client(name,rn):
 
    while True:
            try:
                message = c.recv(2048).decode()
                print ('\n' + message)
                msg_send(message,c,rn)
            except Exception:
                    print("The user is removed")
                    remove(c)
                    break

def msg_send(msg, c,roomName):
    print(usr)
    for i in usr.keys():
        if usr[i] == roomName:
            try:
                i.send(bytes(msg, 'utf-8'))
            except Exception:
                print("The user removed")
                i.close()
                remove(i)
            

def remove(c):
    if c  in usr.keys():
        del usr[c]

rooms=[]
def create_room(name):
    roomName=c.recv(1024).decode()
    rooms.append(roomName)
    usr[c]=roomName
    c.send(bytes("Welcome to the chat room",'utf-8'))
    _thread.start_new_thread(client, (name,roomName)) 

def join_room(name):
    if len(rooms)==0:
        c.send(bytes("1",'utf-8'))
        room(name)
    else:
        c.send(bytes("0",'utf-8'))
        roomList="-".join(rooms)
        c.send(bytes(roomList,"utf-8"))
        r=int(c.recv(1024).decode())
        if r==1111:
            print("wrong room")
            join_room(name)
        usr[c]=rooms[r-1]
        c.send(bytes("Welcome to the chat room",'utf-8'))
        _thread.start_new_thread(client, (name,usr[c]))

        
        
   
def show_room(name):
    if len(rooms) != 0:
        roomList="-".join(rooms)
        c.send(bytes(roomList,"utf-8"))
    room(name)


def room(name):

    ui=int(c.recv(1024).decode())
    if ui==1:
        create_room(name)
    elif ui==2:
        join_room(name)
    else:
        show_room(name)

while True:

    c, addr = s.accept()
    name=c.recv(1024).decode()
    usr[c]=""
    print("connections accepted ")
    room(name)

    
c.close()
s.close()

