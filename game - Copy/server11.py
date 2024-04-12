import pickle
import socket
import time

# Classe représentant une partie de Puissance 4
class Puissance4Partie:
    def __init__(self):
        self.plateau = [["" for _ in range(7)] for _ in range(6)]  # Plateau de jeu
        self.joueur = ['X', 'O']  # Liste des joueurs
        self.joueur_actuel = "X"  # Joueur actuel
        self.gagnant = None  # Joueur gagnant
        self.match_nul = False  # Match nul
        self.terminer = False  # Partie terminée
        self.it1 = 0  # Variable it1
        self.it2 = 0  # Variable it2

    def get_gagnant(self):
        return self.gagnant  # Renvoie le joueur gagnant

    def tour_de_jeu(self):
        return self.joueur_actuel  # Renvoie le joueur dont c'est le tour

    def etatpartie(self):
        return self.terminer  # Renvoie l'état de la partie (terminée ou non)

    def etat_plateau(self):
        return self.plateau  # Renvoie l'état du plateau de jeu

    def changer_joueur(self):
        if self.joueur_actuel == 'X':
            self.joueur_actuel = 'O'
        else:
            self.joueur_actuel = 'X'  # Change le joueur actuel
    
    def faire_mouvement(self, coordonnees: tuple):
        for ligne in range(5, -1, -1):
            if self.plateau[ligne][coordonnees[1]] == "":
                self.plateau[ligne][coordonnees[1]] = self.joueur_actuel  # Place le pion du joueur actuel
                if self.verifier_victoire(ligne, coordonnees[1]):
                    return True  # Vérifie si le joueur actuel a gagné
                else:
                    self.changer_joueur()  # Change de joueur
                    return False
        return False


    def verifier_victoire(self, ligne, colonne):
        if self.verifier_ligne(ligne) or self.verifier_colonne(colonne) or self.verifier_diagonale(ligne, colonne):
            self.gagnant = self.joueur_actuel # Définit le joueur actuel comme gagnant
            self.terminer = True # Termine la partie
            return True
        elif self.verifier_match_nul():
            self.match_nul = True # Déclare un match nul
            self.terminer = True # Termine la partie
            return False
        else:
            return False

    # Vérification de fin de partie

    def verifier_colonne(self, colonne):
        pions_alignes = 0
        for ligne in range(6):
            if self.plateau[ligne][colonne] == self.joueur_actuel:
                pions_alignes += 1
                if pions_alignes == 4:
                    return True
            else:
                pions_alignes = 0  # Réinitialiser le compteur si le pion suivant n'est pas du joueur actuel
        return False

    def verifier_ligne(self, ligne):
        pions_alignes = 0
        for colonne in range(7):
            if self.plateau[ligne][colonne] == self.joueur_actuel:
                pions_alignes += 1
                if pions_alignes == 4:
                    return True
            else:
                pions_alignes = 0  # Réinitialiser le compteur si le pion suivant n'est pas du joueur actuel
        return False

    def verifier_diagonale(self, ligne, colonne):
        pions_alignes = 0
        for i in range(-3, 4):
            if 0 <= ligne + i <= 5 and 0 <= colonne + i <= 6:
                if self.plateau[ligne + i][colonne + i] == self.joueur_actuel:
                    pions_alignes += 1
                    if pions_alignes == 4:
                        return True
                else:
                    pions_alignes = 0  # Réinitialiser le compteur si le pion suivant n'est pas du joueur actuel

        pions_alignes = 0
        for i in range(-3, 4):
            if 0 <= ligne - i <= 5 and 0 <= colonne + i <= 6:
                if self.plateau[ligne - i][colonne + i] == self.joueur_actuel:
                    pions_alignes += 1
                    if pions_alignes == 4:
                        return True
                else:
                    pions_alignes = 0  # Réinitialiser le compteur si le pion suivant n'est pas du joueur actuel

        return False

    def verifier_match_nul(self):
        for ligne in range(6):
            for colonne in range(7):
                if self.plateau[ligne][colonne] == '':
                    return False
        return True

# Classe représentant le serveur du jeu Puissance 4
class puissance4server:
    def __init__(self, destination):
        self.partie = Puissance4Partie() 
        self.clients = []  # Liste des clients connectés
        self.adresses = []  # Liste des adresses des clients
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket du serveur
        self.server.bind(destination) # Lie le socket à l'adresse et au port spécifiés
        self.choice = None

    def attendre_clients(self):
        print("En attente de connexion...")
        self.server.listen(1)  # Écoute au moins une connexion
        while len(self.clients) < 2:
            client, adresse = self.server.accept()  # Accepte la connexion d'un client
            print(f"Connexion établie avec {adresse} , {client}")
            self.clients.append(client)  # Ajoute le client à la liste
            self.adresses.append(adresse)  # Ajoute l'adresse du client à la liste
            self.envoyersigne(client)  # Envoie le signe (X ou O) au client
        time.sleep(1)

    def envoyersigne(self, cl):
        if self.choice == {"sign": "X"}:
            self.choice = {"sign": "O"}
            cl.send(pickle.dumps(self.choice))  # Envoie le signe O au client
        else:
            self.choice = {"sign": "X"}
            cl.send(pickle.dumps(self.choice))  # Envoie le signe X au client

    def envoyer_gagnant(self):
        if self.partie.get_gagnant() == "X":
            data = {"gagnant": "X"}
            self.envoyer_donnees(data)  # Envoie le gagnant X aux clients
        elif self.partie.get_gagnant() == "O":
            data = {"gagnant": "O"}
            self.envoyer_donnees(data)  # Envoie le gagnant O aux clients
        elif self.partie.match_nul == True:
            data = {"gagnant": "match_nul"}
            self.envoyer_donnees(data)  # Envoie match nul aux clients
        else:
            pass

    def envoyer_plateau(self):
        print(self.partie.etat_plateau())
        data = {"plateau": self.partie.etat_plateau()}
        self.envoyer_donnees(data)  # Envoie l'état du plateau aux clients

    def fermer_connexion(self):
        for client in self.clients:
            client.close()  # Ferme la connexion avec les clients
        self.server.close()  # Ferme le socket du serveur
        print("Connexion fermée")

    def envoyer_donnees(self, donnees):
        for client in self.clients:
            client.send(pickle.dumps(donnees))  # Envoie les données aux clients

    def get_clients(self):
        return (self.clients[0], self.clients[1])  # Renvoie les clients connectés

    def verifier_donnees_recues(self, number):
        if number == 0:
            donnees = self.clients[0].recv(1024)
            donnees = pickle.loads(donnees)
        elif number == 1:
            donnees = self.clients[1].recv(1024)
            donnees = pickle.loads(donnees)

        if "CoupX" in donnees.keys():
            
            self.partie.faire_mouvement(tuple(donnees["CoupX"]))
            self.envoyer_plateau()

        if "CoupO" in donnees.keys():

            self.partie.faire_mouvement(tuple(donnees["CoupO"]))
            self.envoyer_plateau()

    def main(self):
        self.attendre_clients() # Attend la connexion des clients

        while True:
            try : 
                if self.partie.etatpartie() == True:
                    self.envoyer_gagnant()  # Vérifie si la partie est terminée et envoie le gagnant aux clients
                    self.fermer_connexion()  # Ferme la connexion avec les clients
                    break
                self.verifier_donnees_recues(0)
                self.verifier_donnees_recues(1)
            except:
                self.fermer_connexion()
                break
        

# Crée une instance de la classe puissance4server et lance la partie
while True:
    server = puissance4server(("127.0.0.1", 5555))
    server.main()
    server = None