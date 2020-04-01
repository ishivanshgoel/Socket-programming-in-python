import socket
s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s2.connect((socket.gethostname(),2003))


while True:
    while True:
        if len(s2.recv(1024))==0:
            break
        r=s2.recv(1024).decode('ascii')
    print(r)

    
