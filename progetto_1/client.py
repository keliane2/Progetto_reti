#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#client 

import socket
from threading import Thread

# IP address del server ricevente
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001
# riceve 4096 bytes
BUFFER_SIZE = 1024


def receive(self):
    # gestisce la ricezione di messaggi
    while True:
        try:
            message = self.client_socket.recv(BUFFER_SIZE).decode('utf-8')
            if message:
                print(message)
        except:
            print("An error occurred!")
            self.client_socket.close()
            break

def send(self):
    # gestisce l'invio dei messaggi
    while True:
        message = input('')
        self.client_socket.send(bytes(message, "utf8"))

if __name__ == "__main__":
    # Creazione del socket del client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))  # Connessione al server

    # Avvio dei thread per ricevere e inviare messaggi
    receive_thread = Thread(target=receive)
    receive_thread.start()

    send_thread = Thread(target=send)
    send_thread.start()
