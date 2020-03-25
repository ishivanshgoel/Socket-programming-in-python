##server side

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),2002))
s.listen(5)

n=int(input())

loc_dur=[]

for i in range(n):
    loc_dur.append(input().split(" "))

time1=0
time2=0
time3=0
task=0

clt,address=s.accept()

try:
    f = open("myfile.txt", "x")
except:
    f = open("myfile.txt", "w")

while(task!=n):
    if(time1==0):
        time1=int(loc_dur[0][1])
        clt.send(bytes(str(loc_dur[0][0]+" Truck 1\n"),"utf-8"))
        f.write(str(loc_dur[0][0]+" Truck 1\n"))
        loc_dur=loc_dur[1:]
        task+=1
 
    if(time2==0):
        time2=int(loc_dur[0][1])
        clt.send(bytes(str(loc_dur[0][0]+" Truck 2\n"),"utf-8"))
        f.write(str(loc_dur[0][0]+" Truck 2\n"))
        loc_dur=loc_dur[1:]
        task+=1
    
    if(time3==0):
        time3=int(loc_dur[0][1])
        clt.send(bytes(str(loc_dur[0][0]+" Truck 3\n"),"utf-8"))
        f.write(str(loc_dur[0][0]+" Truck 3\n"))
        loc_dur=loc_dur[1:]
        task+=1
    
    time1-=1
    time2-=1
    time3-=1
s.close()
f.close()
