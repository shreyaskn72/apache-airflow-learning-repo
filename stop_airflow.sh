#!/bin/bash

set -e

echo ""
echo "Stopping Airflow containers..."
echo ""

# Stop all containers
docker compose down
docker compose down flower
echo ""
echo "✅ All Airflow containers have been stopped."
echo ""

# Optional: Remove volumes
read -p "Do you want to remove volumes and clean up? (y/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
  echo "Removing volumes..."
  docker compose down -v
  echo "✅ Volumes removed. Airflow setup is cleaned up."
else
  echo "✅ Containers stopped. Data preserved for next startup."
fi

echo ""

