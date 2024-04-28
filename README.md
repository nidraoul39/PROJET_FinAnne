## README.md

# Projet Puissance 4 en Ligne

Bienvenue dans mon projet de fin d'année : un jeu de Puissance 4 en ligne !

## Installation et exécution

### Client

Pour jouer, suivez ces étapes :

1. Exécutez `client.py`.
2. Pour vous connecter à votre propre serveur, utilisez `connexion.py`.
3. Si vous préférez tester en local, utilisez `connexionLOCAL.py`. **Attention** : Renommez ce fichier en `connexion.py` avant de l'exécuter, car le client en dépend.

### Serveur

**Linux**

1. Exécutez `serverLinux.py` avec le script `StartServpy`.
2. Dans le terminal du serveur, saisissez :

```bash
nohup ./StartServpy &
```

Cela lancera le serveur et créera un fichier de log dans le même dossier.

**Windows**

1. Exécutez `serverWindows.py` avec Python :

```bash
python serverWindows.py
```

## Problèmes connus

- **Bug de réception des messages (local uniquement):** À la fin de la partie, un seul message de victoire est reçu au lieu de deux. Cela se produit uniquement en mode local car le serveur n'envoie qu'un seul message par adresse.
- **Bug de fin de partie:** À la fin de la partie, le deuxième joueur doit cliquer comme s'il jouait pour recevoir la notification de fin de partie du serveur. Ce bug est dû au fait que le serveur gère la partie et que le client 2 doit envoyer une requête pour attendre la réponse du serveur.

Ces problèmes sont répertoriés pour améliorer votre expérience de jeu.

## Remarques

* Ce projet est réalisé en Python.
* Assurez-vous d'avoir Python installé sur votre système avant de lancer les scripts.
* Vous pouvez modifier le code selon vos besoins et préférences (comme l'addresse ip du server pour un server personnel).

## Amusez-vous bien !
