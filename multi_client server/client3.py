import socket
s3=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s3.connect((socket.gethostname(),5002))
msg=""
print("*****************TRUCK 3 ACTIVE*************")
while True:
    k=s3.recv(10).decode('ascii')
    if(len(k)>0):
        msg=msg+k
    else:
        break

print(msg)
s3.close()
    
        
