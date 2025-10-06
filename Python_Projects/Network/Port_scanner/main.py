# Port scanning is illegal

# Will use multi thread to make it.
# WHy we port scan - we interested in open ports we are interested in open ports because an open port especially an unnecessarily open port might be a security gap and we always want to find security gaps either in our own networks to make sure that our network is secure enough or if we have bad intentions and we are hacking we want to find open ports in networks of other people

import socket 
import threading
from queue import Queue

target = "127.0.0.1" # This is a local host my machine to scan 
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker() :
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port) 

port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for t in range(100): # We increase to make it faster from 10 to 500 to check
    thread = threading.Thread(target=worker)  #we referring tot he worker functiont without calling it                  
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)            