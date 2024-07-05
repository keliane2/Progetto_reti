#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#server
import socket
import threading

# IP address del server ricevente
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
# riceve 4096 bytes ogni trance
BUFFER_SIZE = 1024
#numero di connessioni abilitate
NUM = 100

# Lista dei clienti connessi
clients = []

# Funzione per ricevere i messaggi ricevuti dai clients
def handle_client(client_socket):
    while True:
        try:
            #riceve il messaggio dal cliente
            message = client_socket.recv(BUFFER_SIZE).decode('utf-8','ignore')
            if message:
                print(f"Received message: {message}")
                #condivide il messaggio con tutti gli altri client
                broadcast(message, client_socket)
            else:
                remove(client_socket)
        except:
            continue

# Funzione per inviare messaggi a tutti i clienti connessi
def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)

# Funzione per rimuovere un client dalla lista dei clienti connessi
def remove(client):
    if client in clients:
        clients.remove(client)

# main principale per il server
if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_HOST, SERVER_PORT))
    server.listen(NUM)
    print("Server started. Waiting for connections...")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"Connection from {addr} has been established.")

        threading.Thread(target=handle_client, args=(client_socket,)).start()