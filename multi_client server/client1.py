import socket
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.connect((socket.gethostname(),2002))

# msg1=""

while True:
    while True:
        if len(s1.recv(10))==0:
            break
        r=str(s1.recv(1024).decode('ascii'))
    print(r)
