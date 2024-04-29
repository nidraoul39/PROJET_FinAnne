## README.md

# Projet Puissance 4 en Ligne

Bienvenue dans mon projet de fin d'année : un jeu de Puissance 4 en ligne !

## Installation et exécution

### Client

Pour jouer, suivez ces étapes :

1. Exécutez `client.py`.
2. Pour vous connecter à votre propre serveur, utilisez `clientlocal.py`.
3. avec les 2 client on peut se connecter a d'autre server mais dans le premier le server par défaut et mon server et dans le 2 eme le server par défaut est un server local sur l'addresse 127.0.0.1 (local)
4. pour se connecter a un server disponible chez sois qui execute le programme server on peut utiliser l'ip local (addresse ip privé)
### Serveur
**Server local ou distant ?**
1. pour un server local seul l'ip local suffit et le port pour se connecter.
2. pour un server sur une autre box (pas chez sois) une reddirection de port sera nécéssaire si le server.

**Linux**

1. Exécutez `serverLinux.py` avec le script `StartServpy`.
2. Dans le terminal du serveur, saisissez :

```bash
nohup ./StartServpy &
```
avant si se n'est pas déja fait donnez les autorisation d'éxécution avec : 
```bash
chmod +x StartServpy
```

Cela lancera le serveur et créera un fichier de log dans le même dossier de plus on peut relancer une partie au bout d'une minute a peut pres le temps que le port se libère et qu'un autre s'ouvre.

**Windows**

1. Exécutez `serverWindows.py` avec Python :

```bash
python serverWindows.py
```


2. sur windows il y a aussi 3 éxécutable possible le server local, le jeu local, et le jeu pour le server officiel (le mien).

```bash
./executable.exe
```

## Problèmes connus

- **Bug de fin de partie:** À la fin de la partie, le deuxième joueur doit cliquer comme s'il jouait pour recevoir la notification de fin de partie du serveur. Ce bug est dû au fait que le serveur gère la partie et que le client 2 doit envoyer une requête pour attendre la réponse du serveur.

Ces problèmes sont répertoriés pour améliorer votre expérience de jeu.

## Remarques

* Ce projet est réalisé en Python.
* Assurez-vous d'avoir Python installé sur votre système avant de lancer les scripts.
* Vous pouvez modifier le code selon vos besoins et préférences (comme l'addresse ip du server pour un server personnel).

## Amusez-vous bien !
