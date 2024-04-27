import socket
import pickle

class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ("82.67.59.220", 5555)

    def envoie_donnees(self, donnees):
        self.socket.send(pickle.dumps(donnees))
    
    def recevoir_donnees(self):
        self.socket.settimeout(30)
        donnees = self.socket.recv(1024)
        return pickle.loads(donnees)
    
    def connexion(self):
        self.socket.connect(self.host)

    def fermer_connexion(self):
        self.socket.close()
