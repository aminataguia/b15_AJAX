# Utilisez une image officielle Python comme base
FROM python:3.11-alpine

# Définissez le répertoire de travail
WORKDIR /frontend

# Assurez-vous que le fichier requirements.txt est dans le répertoire de travail
COPY ./requirements.txt /front/requirements.txt

# Installez les dépendances de l'application
RUN pip install --no-cache-dir -r requirements.txt

# Copiez les fichiers de l'application dans le répertoire de travail
COPY . /frontend

# Exposez le port sur lequel le serveur sera démarré
EXPOSE 8001

# Commande pour démarrer l'application
CMD ["python3", "-m", "http.server", "8001"]
