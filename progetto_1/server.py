#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#server
import socket
from threading import Thread

# IP address del server 
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001
# riceve 1024 bytes
BUFFER_SIZE = 1024
#numero di connessioni abilitate
NUM = 50

# Lista per tener traccia dei client connessi
clients = []

def broadcast(message, client_socket):
    # Invia il messaggio agli altri client
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                #Rimuove il client nel caso l'invio non andasse
                #a buon fine
                remove(client)

# La funzione gestisce la connessione di un singolo client.
def manage_client(client_socket):
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE).decode('utf-8')
            if message:
                print(f"Received message: {message}")
                broadcast(message, client_socket)
            else:
                remove(client_socket)
                break
        except:
            continue

#Per stabilire la connessione client-server
def receive_connections():
    while True:
        client_socket, client_address = server.accept()
        print(f"Connection from {client_address} has been established.")
        #aggiunge il nuovo client che si connette alla lista dei client connessi
        clients.append(client_socket)
        client_socket.send(bytes("Hello, connection to the server ok!","utf-8"))
        #diamo inizio all'attività del Thread - uno per ciascun client
        Thread(target=manage_client, args=(client_socket,)).start()

# Funzione che rimuove un client dalla lista dei 
# client connessi nel caso non fosse più connesso
def remove(client):
    if client in clients:
        clients.remove(client)

if __name__ == "__main__":
    # Creazione del socket per il server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_HOST, SERVER_PORT))
    server.listen(NUM)    
    print("Server waiting for connections...")
    ACCEPT_THREAD = Thread(target=receive_connections()).start()
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    server.close()

