#!/bin/bash

set -e

# Create directories
mkdir -p dags logs plugins

# Create .env safely
if [ ! -f .env ]; then
  echo "AIRFLOW_UID=$(id -u)" > .env

  echo "Generating Fernet Key..."
  FERNET_KEY=$(python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")

  echo "FERNET_KEY=$FERNET_KEY" >> .env
fi

# Init + start
docker compose up airflow-init
docker compose up -d
docker compose up -d flower

echo ""
echo "🌐 Airflow UI  : http://localhost:8080"
echo "🌸 Flower UI   : http://localhost:5555"
echo "🟥 Redis UI    : http://localhost:5540"
echo "🐘 pgadmin UI  : http://localhost:5050"
