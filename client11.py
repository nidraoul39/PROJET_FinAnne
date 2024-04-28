from tkinter import *
from connexion import Client # mon module connexion.py
import webbrowser
import time

# Classe Interface pour gérer l'interface graphique du jeu
class Interface:   
    def __init__(self):
        self.client = Client()
        self.joueur = None
        self.boutons = [[] for _ in range(6)]
        self.turn = "X"
        self.tourfenetre = None

    # Méthode pour établir la connexion avec le serveur
    def connexion(self):
        self.client.connexion()
        self.verifier_donnees_recues()
        time.sleep(1)

    # Méthode pour vérifier si le joueur est signé
    def verif_sign(self):
        if self.joueur == None :
            self.afficher_erreur("ERREUR SIGNE NON RECU")
            return 0
        else:
            return 1
    
    # Méthode pour créer la fenêtre du jeu
    def faire_fenetre(self):
        self.fenetre = Tk()
        self.fenetre.title("puissance 4")
        self.fenetre.geometry("900x800") 
        self.fenetre.resizable(False, False)
        for x in range(6):
            for y in range(7):
                self.boutons[x].append(Button(self.fenetre, command=lambda y=y, x=x: self.jouer_coup(x,y), width=5, height=2, font=("Arial", 20, "bold")))  
                self.boutons[x][y].grid(row=x, column=y)

        self.tourfenetre = Label(self.fenetre, text=f"Tour du joueur: {self.turn}", font=("Arial", 15, "bold"))
        self.tourfenetre.grid(row=9, column=9)
        self.joueurfentre = Label(self.fenetre, text=f"Vous êtes le joueur: {self.joueur}", font=("Arial", 15, "bold"))
        self.joueurfentre.grid(row=10, column=9)

        if self.joueur == "O":
            self.fenetre.after(1000,self.verifier_donnees_recues)

        self.fenetre.mainloop()

        

    # Méthode pour jouer un coup
    def jouer_coup(self, x, y):
        try:
            if self.turn != self.joueur:
                self.afficher_erreur("Ce n'est pas votre tour")
                return
            coup = "Coup"+ str(self.joueur)
            donnees = {coup : (x, y)}
            self.client.envoie_donnees(donnees)

            self.verifier_donnees_recues() 
            self.verifier_donnees_recues()
        except:
            pass

    def changer_tour(self):
        try: 
            if self.turn == "O":
                self.turn = "X"
            else:
                self.turn = "O"
            self.tourfenetre.config(text=f"Tour du joueur: {self.turn}")
        except:
            pass
        
    # Méthode pour mettre à jour le plateau de jeu
    def maj_plateau(self, plateau : list):
        self.changer_tour()

        for i in range(6):
            for j in range(7):
                if plateau[i][j] == "X":
                    self.boutons[i][j].config(text=plateau[i][j], bg="blue")
                elif plateau[i][j] == "O":
                    self.boutons[i][j].config(text=plateau[i][j], bg="red")
                else :
                    pass
        self.fenetre.update()

    
    # Méthode pour fermer la fenêtre du jeu
    def fermer_fenetre(self):
        self.client.fermer_connexion()
        self.fenetre.destroy()
    
    # Méthode pour afficher le gagnant
    def afficher_gagnant(self, gagnant):
        fenetre = Tk()
        fenetre.geometry("500x100")
        fenetre.title("Gagnant")
        if gagnant == self.joueur:
            label = Label(fenetre, text=f"Le gagnant est: {gagnant} vous avez gagné", font=("Arial", 15, "bold"), fg="green")
        else:
            label = Label(fenetre, text=f"Le gagnant est: {gagnant} vous avez perdu", font=("Arial", 15, "bold"), fg="red")
        label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.fenetre.title(f"puissance 4 - Gagnant: {gagnant}")
        self.blockgame()
        self.fenetre.update()
        
    # Méthode pour afficher une erreur
    def afficher_erreur(self, erreur):
        stop = lambda fenster: fenster.destroy() 
        fenster = Tk()
        fenster.geometry("600x100")  
        fenster.configure(bg="beige") 
        text = Label(fenster, text=f"Erreur: {erreur}", font=("Arial", 15, "bold"), fg="red", bg="beige")
        text.pack()
        button = Button(fenster, text="OK", command=lambda: stop(fenster))
        button.pack()
        fenster.mainloop()

    # Méthode pour obtenir le joueur actuel
    def get_player(self):
        return self.joueur
    
    # Méthode pour bloquer le jeu
    def blockgame(self):
        for i in range(6):
            for j in range(7):
                self.boutons[i][j].config(command=None)

    def unblockgame(self):
        for i in range(6):
            for j in range(7):
                self.boutons[i][j].config(command=lambda i=i, j=j: self.jouer_coup(i,j))

    # Méthode pour vérifier les données reçues du serveur
    def verifier_donnees_recues(self):

        data = self.client.recevoir_donnees()
        print("Données reçues : ", data)  

        if "gagnant" in data.keys():
            self.afficher_gagnant(data["gagnant"])
            time.sleep(7)
            self.fermer_fenetre() 
            self.client.fermer_connexion()


        if "errorX" in data.keys() and self.joueur == "X":
            self.afficher_erreur(data["errorX"])
            return "CI"
        if "errorO" in data.keys() and self.joueur == "O":
            self.afficher_erreur(data["errorO"])
            return "CI"
        if "errorX" in data.keys() and self.joueur != "O":
            pass
        if "errorO" in data.keys() and self.joueur != "X":
            pass
        if "plateau" in data.keys():
            self.maj_plateau(data["plateau"])
        if "erreur" in data.keys():
            self.afficher_erreur(data["erreur"])
        if "sign" in data.keys():
            self.joueur = data["sign"]
        if "tour" in data.keys():
            self.turn = data["tour"] 
            self.fenetre.update()
        


# Fonction pour ouvrir le site web
def ouvrir_site_web():
    webbrowser.open("https://nidraoul.me")

# Fonction pour ouvrir Instagram
def ouvrir_instagram():
    webbrowser.open("https://www.instagram.com/nidal_d25")

# Fonction pour ouvrir Discord
def ouvrir_discord():
    webbrowser.open("https://discord.gg/deNudFYSnU")

# Fonction pour afficher le menu principal
def menu_principal():
    global root_menu
    root_menu = Tk()
    root_menu.title("Puissance 4")
    root_menu.title("Game")
    root_menu.configure(background="beige")
    root_menu.geometry("1920x1080")
    root_menu.attributes("-fullscreen", True)

    bouton_quitter = Button(root_menu, text="X", command=root_menu.destroy, font=("Arial", 20), bg="red", fg="white")
    bouton_quitter.pack(side=TOP, anchor=NE, padx=10, pady=10)

    etiquette_bienvenue = Label(root_menu, text="Bienvenue sur le Puissance 4 \n n'hésitez pas à aller visiter notre site", bg="beige", fg="black", font=("Arial", 30))
    etiquette_bienvenue.pack(side=TOP, fill=X, padx=10, pady=10)

    bouton_connexion = Button(root_menu, text="Se connecter", width=25, height=3, bg="#2ecc71", fg="white", font=("Arial", 20), command=lambda: main(root_menu))
    bouton_connexion.pack(side=TOP, padx=10, pady=10)

    bouton_site_web = Button(root_menu, text="NOTRE SITE", width=25, height=3, bg="#2ecc71", fg="white", font=("Arial", 20), command=ouvrir_site_web)
    bouton_site_web.pack(side=TOP, padx=10, pady=10)

    bouton_instagram = Button(root_menu, text="Mon Insta", width=25, height=3, bg="#2ecc71", fg="white", font=("Arial", 20), command=ouvrir_instagram)
    bouton_instagram.pack(side=TOP, padx=10, pady=10)

    bouton_discord = Button(root_menu, text="SERVEUR DISCORD", width=25, height=3, bg="#2ecc71", fg="white", font=("Arial", 20), command=ouvrir_discord)
    bouton_discord.pack(side=TOP, padx=10, pady=10)

    root_menu.mainloop()

# Fonction principale pour lancer le jeu
def main(fenster):
    fenster.destroy()
    game = Interface()
    try:
        game.connexion()
        game.faire_fenetre()
    except:
        game.afficher_erreur("Erreur de connexion")
        menu_principal()

# Lancement du menu principal
menu_principal()
