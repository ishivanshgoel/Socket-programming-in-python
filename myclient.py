import socket
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.connect((socket.gethostname(),2002))
msg1=""
while True:
	v=s1.recv(10)
	if len(v)==0:
		break
	msg1=msg1+v.decode("utf-8")          
print(msg1)
