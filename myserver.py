##server side

import socket
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind((socket.gethostname(),1026))
s1.listen(5)


s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s2.bind((socket.gethostname(),1025))
s2.listen(5)


s3=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s3.bind((socket.gethostname(),1026))
s3.listen(5)


n=int(input())

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
        time1=int(loc_dur[0][1])
        print("111")
        clt1,address1=s1.accept()
        clt1.send(bytes(str(loc_dur[0][0]+" Truck 1"),"utf-8"))
        clt1.close()
        print(str(loc_dur[0][0]+": Truck1"))
        f.write(str(loc_dur[0][0]+" Truck 1\n"))
        loc_dur=loc_dur[1:]
        task+=1

    if(time2==0):
        time2=int(loc_dur[0][1])
        print("222")
        clt2,address2=s2.accept()
        clt2.send(bytes(str(loc_dur[0][0]+" Truck 2"),"utf-8"))
        clt2.close()
        print(str(loc_dur[0][0]+": Truck 2"))
        f.write(str(loc_dur[0][0]+" Truck 2\n"))
        loc_dur=loc_dur[1:]
        task+=1
    
    if(time3==0):
        time3=int(loc_dur[0][1])
        print("333")
        clt3,address3=s3.accept()
        clt3.send(bytes(str(loc_dur[0][0]+" Truck 3"),"utf-8"))
        clt3.close()
        print(str(loc_dur[0][0]+": Truck 3"))
        f.write(str(loc_dur[0][0]+" Truck 3\n"))
        loc_dur=loc_dur[1:]
        task+=1
    
    time1-=1
    time2-=1
    time3-=1
f.close()
