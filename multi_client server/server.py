##server side
import socket
import _thread
import threading
import select

""" Connect to clients one by one as instructed by program"""

s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind((socket.gethostname(),5000))
s1.listen(5)
print("Connect to Truck 1....")
clt1,address1=s1.accept()
print("Successfully Connected to Truck 1")

print("Connect to Truck 2.....")
s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s2.bind((socket.gethostname(),5001))
s2.listen(5)
clt2,address2=s2.accept()
print("Successfully Connected to Truck 2")


print("Connect to Truck 3")
s3=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s3.bind((socket.gethostname(),5002))
s3.listen(5)
clt3,address3=s3.accept()
print("Successfully Connected to Truck 3")

print("Connection Successful with all three Trucks")

n=int(input("Enter Number of locations:"))
print(f"Enter {n} locations and time")
loc_dur=[]
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
        print(f"Location {loc_dur[0][0]} Assigned to Truck 1")
        time1=int(loc_dur[0][1])
        clt1.sendall(bytes(str(loc_dur[0][0]+" Truck 1\n"),"ascii"))
        f.write(str(loc_dur[0][0]+" Truck 1\n"))
        loc_dur=loc_dur[1:]
        task+=1

    if(time2==0):
        print(f"Location {loc_dur[0][0]} Assigned to Truck 2")
        time2=int(loc_dur[0][1])
        clt2.sendall(bytes(str(loc_dur[0][0]+" Truck 2\n"),"ascii"))
        f.write(str(loc_dur[0][0]+" Truck 2\n"))
        loc_dur=loc_dur[1:]
        task+=1

    if(time3==0):
        print(f"Location {loc_dur[0][0]} Assigned to Truck 3")
        time3=int(loc_dur[0][1])
        clt3.sendall(bytes(str(loc_dur[0][0]+" Truck 3\n"),"ascii"))
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
