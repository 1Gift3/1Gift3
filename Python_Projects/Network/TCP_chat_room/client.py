import socket 
import threading 

nickname = input("Choose your preferred nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True: 
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)

        except: 
            print("An error occured!")
            client.close() 
            break       

def write():
    while True:
        message = f'{nickname}: {input("")}'   
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()            

# Error 1 -  client.connect(('127.0.0.1', 55555)) ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

# When it works i shuld be able to open three terminals to seee the interaction of the new chat open but not on the serve as it monitors only the connections

