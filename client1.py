import socket
s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s2.connect((socket.gethostname(),2000))
print("*****************TRUCK 1 ACTIVE***************")
while True:
    k=s2.recv(1024).decode('ascii')
    if(len(k)>0):
        print(k)
    else:
        break
s2.close()
