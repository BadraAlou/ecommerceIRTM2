# Utilisation de l'image officielle de Python
FROM python:3.10

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers du projet
COPY requirements.txt .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY . .

# Exposition du port de Django
EXPOSE 8000

# Commande de lancement du serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
