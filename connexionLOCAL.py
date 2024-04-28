#fichier a renommer connexion.py pour que le jeu fonctionne (lancer seulement client.py)

import socket
import pickle

class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ("127.0.0.1", 5555)
        self.socket.settimeout(3600)

    def envoie_donnees(self, donnees):
        self.socket.send(pickle.dumps(donnees))
    
    def recevoir_donnees(self):
        donnees = self.socket.recv(1024)
        return pickle.loads(donnees)
    
    def connexion(self):
        self.socket.connect(self.host)

    def fermer_connexion(self):
        self.socket.close()

