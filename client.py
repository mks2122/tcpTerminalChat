import socket
import threading
import select
import sys

c = socket.socket()

c.connect(('localhost',9999))
name=input("Enter your name: ")
c.send(bytes(name,'utf-8'))

def create():
    
    roomName=input("Enter the chat room name to create:")
    c.send(bytes(str(roomName),'utf8'))
    print(c.recv(1024).decode())
    

def join():
    i=c.recv(1024).decode()

    if int(i)==1:
        print(c.recv(1024).decode())
        room()
    else:
        print("Room Number \t:\tRoom Number\t")
        rooms=list(map(str,(c.recv(1024).decode()).split("-")))
        for i in range(len(rooms)): 
                print(f"{i+1}\t:\t{rooms[i]}")
        r=int(input("Enter the room number: "))
        if r-1<=len(rooms):
            c.send(bytes(str(r),'utf-8'))
        else:
            c.send(bytes("1111","utf-8"))
            print("Wrong input! Try again")
            join()

 
def room():
    print("1. create new chat room\n2. join existing chatroom\n3. show existing chatroom")
    ui=int(input("Enter an option: "))
    c.send(bytes(str(ui),'utf-8'))
    if ui==3:
        for i in list(map(str,c.recv(1024).decode().split("-"))):
            print(i,end="\n")
        room()
    elif ui==2:
        join()
    elif ui==1:
        create()

    



def recieve():
    msg=c.recv(1024).decode()
    print(msg)

def sendmsg(name):

        msg = sys.stdin.readline()
        if msg!='':
            msg1=f'\n{name}>> '+str(msg)
            c.send(bytes(msg1,'utf-8'))



room()


while True:
    snd=threading.Thread(target=sendmsg(name))
    snd.start()


    rec=threading.Thread(target=recieve)
    rec.start()
    snd.join()

    



c.close()



