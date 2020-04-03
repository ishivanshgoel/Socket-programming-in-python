import socket
""" Connect to clients one by one as instructed by program"""

client=[]
s=['s1','s2','s3']
task=0
loc_dur=[]


## connect to users and stores all clients to a list
def accept_connections():
    global client ## list of clients
    global s  ## a list of sockets
    for i in range(3):
        s[i]=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s[i].bind((socket.gethostname(),2000+i))
        s[i].listen(5)
        print(f"Waiting for Truck {i+1} to connect......")
        clt,address1=s[i].accept()

        ''' .accept() functions waits for clients to connect'''

        client.append(clt)
        print(f"Connected to Truck {i+1}")
    print("Successfully Connected to all 3 trucks!!")


## append delivery information to a output file
def write_output():
    global f
    f = open("myfile.txt", "a+")

## takes delivery locations information from user 
def take_input():
    global loc_dur
    global n
    n=int(input("Enter Number of locations:"))
    for i in range(n):
        loc_dur.append(input().split(" "))


""" assigns task to trucks based on their availability
    availability order if all are free Truck1 > Truck2 > Truck3 """


''' 
logic for assigning task

## run a loop till all tasks are finished
## n is number of tasks

## list of locations with time

while(task!=n):
	if(time1==0):  ## truck1 is free
		##assgn location present at index 0 in list
		##  time1= time required for particular location 
		task=task+1 ## a task is completed
		## remove location present on index 0 from the list

	if(time2==0):
	   ## truck2 is free
	   ## assign a location
	   ## time 2 = time required for partcular location
	   task=task+1
	   ## one more task completed

	if(time3==0):
		## truck3 is free
		## assign a location
		## time3 =time required for particular location
		task=task+1
		## one more task completed


	time1=time1-1   ## decrease time by -1 in every itteration
	time2=time2-1
	time3=time3-1

'''


def assigning_task():
    global task
    global loc_dur
    global client
    time1=0
    time2=0
    time3=0
    while(task!=n):
        if(time1==0):
            print(f"Location {loc_dur[0][0]} Assigned to Truck 1")
            time1=int(loc_dur[0][1])
            client[0].sendall(bytes(str(loc_dur[0][0]+" Truck 1\n"),"ascii"))
            f.write(str(loc_dur[0][0]+" Truck 1\n"))
            loc_dur=loc_dur[1:]
            task+=1

        if(time2==0):
            print(f"Location {loc_dur[0][0]} Assigned to Truck 2")
            time2=int(loc_dur[0][1])
            client[1].sendall(bytes(str(loc_dur[0][0]+" Truck 2\n"),"ascii"))
            f.write(str(loc_dur[0][0]+" Truck 2\n"))
            loc_dur=loc_dur[1:]
            task+=1

        if(time3==0):
            print(f"Location {loc_dur[0][0]} Assigned to Truck 3")
            time3=int(loc_dur[0][1])
            client[2].sendall(bytes(str(loc_dur[0][0]+" Truck 3\n"),"ascii"))
            f.write(str(loc_dur[0][0]+" Truck 3\n"))
            loc_dur=loc_dur[1:]
            task+=1

        time1-=1
        time2-=1
        time3-=1
    


def main():
    ## function to accept all the connections from clients
    accept_connections()
    ## takes input of delivery location
    take_input()
    ## write assigned task information to output file
    write_output()
    ## assign task to trucks based on availability
    assigning_task()


if __name__=="__main__":
    main()
