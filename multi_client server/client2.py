import socket
s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s2.connect((socket.gethostname(),5001))
msg=""
print("*****************TRUCK 2 ACTIVE*************")
while True:
    k=s2.recv(10).decode('ascii')
    if(len(k)>0):
        msg=msg+k
    else:
        break

print(msg)
s2.close()
    
        
        
        

    
 
