# Utilisez une image officielle Python comme base
FROM python:3.11-alpine

WORKDIR backend
# Copiez le reste des fichiers de l'application dans le répertoire de travail
COPY . .

# Copiez le fichier des dépendances dans le répertoire de travail
COPY requirements.txt .

# Installez les dépendances de l'application
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000
# Commande pour démarrer l'application
CMD ["uvicorn", "app_ui:app", "--host", "0.0.0.0", "--port", "8000"]
