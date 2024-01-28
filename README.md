# Projet-Devops-CI-CD

Groupe : CAILLOT Adrien / KABACHE Zakaria

Choix de Projet - Mettre en place une CI/CD permettant de gérer le cycle vie d'une application WEB : des lancements des tests au déploiement

Tests unitaires :

- Création d'un fichier web.py qui contient un serveur Flask basique
- Création d'un fichier test-unitaire.py qui contient un code permettant de tester si le code de la page renvoyait bien 200 (site fonctionnel), le test regarde aussi si l'intitulé de la page est bien celui inscrit dans le code ( dans notre cas, le message est 'This is my web server')

Mise à jour sur une VM de prod :

- Création d'une VM Azure pour pouvoir réaliser nos tests et voir si le workflow fonctionne bien, configuration classique avec un environnement Ubuntu, connexion SSH / HTTPS / HTTP autorisée.
- Création de secrets sur Github pour la confidentialité des données + assurer connectivité avec la VM avec adresse IP / Hostname / Password / PrivateKey
- Ytilisation de Ansible pour gérer le déploiement, le fichier inventory.ini permet de mettre les informations de la VM Azure, le fichier deploy.yaml est un script permettant d'envoyer le fichier web.py sur notre VM et ainsi de mettre à jour notre VM.

Déploiement de l'application via Docker :

- Utilisation de Docker pour créer une image, créer un repository et l'envoyer sur notre DockerHub
- Déploiement de l'image sur notre VM Azure 

Technologies utilisées :
Ansible / Docker / Azure Virtual Machine / Pytest / GitHub 


