# Socket-programming-in-python

server.py -> server for assigning task to clients.
clien1.py, cliemt2.py, client3.py are clients as truck1, truck2 and truck 3

First run server.py. Now, server will wait for truck 1 to connect, immediately as truck 1 connects to server, it will wait for truck 2 to connect and so on.
After getting "Successfully connected to all three trucks!!", enter number of locations(n).
Enter locations and time required to deliver package(space seprated) in n lines.
Server will assign tasks to trucks based on their availability. If all are free then, Truck1>Truck2>Truck3.
