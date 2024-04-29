import socket
import pickle

class Client:
    def __init__(self,ip:str,port:int):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = (ip, port)
        self.socket.settimeout(3600)

    def envoie_donnees(self, donnees):
        self.socket.send(pickle.dumps(donnees))
    
    def recevoir_donnees(self):
        self.socket.settimeout(3600)
        donnees = self.socket.recv(1024)
        return pickle.loads(donnees)
    
    def connexion(self):
        self.socket.connect(self.host)

    def fermer_connexion(self):
        self.socket.close()

