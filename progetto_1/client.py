#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#client 

import socket
import threading

# IP address del server ricevente
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001
# riceve 4096 bytes
BUFFER_SIZE = 1024

# funzione per ricezione di messaggi dal server
def receive_messages(client_socket):
    while True:
        # legge 1024 bytes dal socket
        try:
            message = client_socket.recv(BUFFER_SIZE).decode('utf-8','ignore')
            if message:
                print(message)
        except:
            print("There is an error!")
            client_socket.close()
            break

# Funzione principale per il client
if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input('')
        client_socket.send(message.encode('utf-8'))
