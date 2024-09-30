# Utiliser une image Python 3.9
FROM python:3.9-slim

# Installer Kedro et autres dépendances
RUN pip install kedro==0.18.1

# Définir le répertoire de travail
WORKDIR /usr/src/app

# Copier le projet
COPY . .

# Installer les dépendances du projet
RUN pip install -r requirements.txt

# Commande pour exécuter Kedro
CMD ["kedro", "run"]