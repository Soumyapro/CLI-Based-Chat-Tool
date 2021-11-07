import socket
from threading import Thread
import threading

alias = input("Choose your nickname for chatting :   ")

host = '127.0.0.1'
port = 9999
client = socket.socket()
client.connect((host, port))


def client_recieve():

    while True:

        try:

            message = client.recv(1024).decode()

            if message == 'your alias?..':

                client.send(alias.encode('utf-8'))

            else:

                print(message)

        except:

            print("Error!")
            client.close()
            break


def client_send():

    while True:

        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_recieve)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
