import socket
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.connect((socket.gethostname(),1024))


s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s2.connect((socket.gethostname(),1025))


s3=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s3.connect((socket.gethostname(),1026))
while True:
	msg1=s1.recv(1024)                 
	print(msg1.decode("utf-8")) 

	msg2=s2.recv(1024)                 
	print(msg2.decode("utf-8")) 

	msg3=s3.recv(1024)                 
	print(msg3.decode("utf-8")) 


