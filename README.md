#Projet Puissance 4 en Ligne

Bienvenue dans mon projet de fin d'année, un Puissance 4 en ligne. Voici comment il est présenté :
**Installation et exécution
**Client

Pour jouer, commencez par exécuter client.py. Si vous souhaitez vous connecter à votre propre serveur, utilisez connexion.py. Si vous préférez tester localement, utilisez connexionLOCAL.py. Dans ce cas, assurez-vous de renommer ce fichier en connexion.py, car le client en dépend.

**Serveur

**Linux

Pour le serveur Linux, utilisez serverLinux.py et lancez-le avec le script StartServpy. Dans le terminal du serveur, saisissez :
`nohup ./StartServpy &`
Cela lancera le serveur, et un fichier de log sera créé dans le même dossier que le serveur.

**Windows

Pour le serveur Windows, exécutez simplement serverWindows.py avec Python :
`python serverWindows.py`


**Problèmes Connus

-    Bug de Réception des Messages: En local uniquement (sa fonctionne si on utilise 2 pc différent) , lors de la fin d'une partie, seul un message de victoire est reçu au lieu de deux, car le serveur envoie un seul message par adresse.

-    Bug de Fin de Partie: À la fin de la partie, le deuxième joueur doit cliquer comme s'il jouait pour que le serveur lui envoie la fin de la partie. Cela est dû au fait que c'est le serveur qui gère la partie et que le client 2 doit envoyer une requête pour attendre la réponse du serveur, ce qui entraîne ce bug.

Ces problèmes sont répertoriés pour une meilleure expérience de jeu. Amusez-vous bien !
