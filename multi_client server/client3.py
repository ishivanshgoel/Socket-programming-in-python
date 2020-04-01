import socket
s3=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s3.connect((socket.gethostname(),2004))


while True:
    while True:
        if len(s3.recv(1024))==0:
            break
        r=s3.recv(1024).decode('ascii')
    print(r)

    
