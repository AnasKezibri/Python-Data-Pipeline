FROM apache/airflow:2.10.2
ADD requirements.txt .
RUN pip install apache-airflow==${AIRFLOW_VERSION} -r requirements.txt

# Définir le répertoire de travail
WORKDIR /usr/src/app

# Copier le projet
COPY . .

# Commande pour exécuter Kedro
CMD ["kedro", "run"]