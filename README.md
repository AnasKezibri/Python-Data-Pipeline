# Guide d'Installation et d'Exécution du Data Pipeline

## Prérequis

Avant de commencer, assurez-vous d'avoir les outils suivants installés sur votre machine :

1. **Docker** et **Docker Compose** :
   - [Installer Docker](https://docs.docker.com/get-docker/)
   - [Installer Docker Compose](https://docs.docker.com/compose/install/)

2. **Git** :
   - [Installer Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Étapes à suivre

### 1. Cloner le dépôt Git
Ouvrez un terminal Git Bash, choisissez un emplacement pour mettre le proejt, puis exécutez la commande suivante pour cloner le projet :
```
git clone https://github.com/AnasKezibri/Python-Data-Pipeline.git
```

### 2. Accéder au répertoire Airflow du projet
```
cd  Python-Data-Pipeline/drugs-publiction-graph/airflow/
```

### 3. Construire l'image Docker
```
docker-compose build
```

### 4. Initialiser la base de données Airflow
```
docker-compose up airflow-init
```

### 5. Démarrer les services
```
docker-compose up
```

### 6. Accéder à Airflow
Vous pouvez maintenant accéder à l'interface web d'Airflow à l'adresse suivante : http://localhost:8080 (User : airflow, password : airflow), puis déclencher le DAG kedro_drugs_pipeline_dag.






