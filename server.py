from threading import Thread
import socket
import threading

host = '127.0.0.1'
port = 9999

server = socket.socket()

server.bind((host, port))

server.listen()

clients = []

aliases = []

# function used to broadcast specific message.


def broadcast(message):

    for client in clients:

        client.send(message)

# function used to handle the clients.
# it tells us if the client joined the chatroom or left the chatroom.


def handle_client(client):

    while True:

        try:

            message = client.recv(1024)
            broadcast(message)

        except:

            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(
                f'{alias} has recently left the chat room.'.encode('utf-8'))
            aliases.remove(alias)
            break


def receive():

    while True:

        print("Server is ready and running now ........")
        client, address = server.accept()
        print(f'Connection is successfully established with {str(address)}')
        client.send('your alias?..'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} joined the chatroom'.encode('utf-8'))
        client.send("you are connected".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":

    receive()
