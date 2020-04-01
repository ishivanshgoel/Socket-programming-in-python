##server side
import socket
import _thread
import threading 
import select


print_lock = threading.Lock()


s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind((socket.gethostname(),2002))
s1.listen(5)
s1.setblocking(0)

s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s2.bind((socket.gethostname(),2003))
s2.listen(5)
s2.setblocking(0)

s3=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s3.bind((socket.gethostname(),2004))
s3.listen(5)
s3.setblocking(0)

n=int(input())

loc_dur=[]
ans=[]
for i in range(n):
    loc_dur.append(input().split(" "))

time1=0
time2=0
time3=0
task=0


try:
    f = open("myfile.txt", "x")
except:
    f = open("myfile.txt", "w")

while(task!=n):
    if(time1==0):
        print("Connecting to Truck 1")
        time1=int(loc_dur[0][1])
        clt1,address1=s1.accept()
        clt1.send(bytes(str(loc_dur[0][0]+" Truck 1\n"),"ascii"))
        f.write(str(loc_dur[0][0]+" Truck 1\n"))
        loc_dur=loc_dur[1:]
        task+=1

    if(time2==0):
        print("Connecting to Truck 2")
        time2=int(loc_dur[0][1])
        clt2,address2=s2.accept()
        clt2.send(bytes(str(loc_dur[0][0]+" Truck 2\n"),"ascii"))
        f.write(str(loc_dur[0][0]+" Truck 2\n"))
        loc_dur=loc_dur[1:]
        task+=1
    
    if(time3==0):
        print("Connecting to Truck 3")
        time3=int(loc_dur[0][1])
        clt3,address3=s3.accept()
        clt3.send(bytes(str(loc_dur[0][0]+" Truck 3\n"),"ascii"))
        f.write(str(loc_dur[0][0]+" Truck 3\n"))
        loc_dur=loc_dur[1:]
        task+=1
    
    time1-=1
    time2-=1
    time3-=1
s1.close()
s2.close()
s3.close()
f.close()
