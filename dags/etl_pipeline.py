from airflow.decorators import dag, task
from datetime import datetime
import requests
import psycopg2

# -------------------------
# CONFIG
# -------------------------
DB_CONFIG = {
    "host": "postgres",
    "database": "airflow",
    "user": "airflow",
    "password": "airflow"
}

# -------------------------
# DAG
# -------------------------
@dag(
    dag_id="etl_pipeline_taskflow",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["etl", "demo"]
)
def etl_pipeline():

    # -------------------------
    # EXTRACT
    # -------------------------
    @task
    def extract():
        url = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url)
        return response.json()

    # -------------------------
    # TRANSFORM
    # -------------------------
    @task
    def transform(raw_data):
        transformed = []
        for user in raw_data:
            transformed.append({
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "city": user["address"]["city"]
            })
        return transformed

    # -------------------------
    # LOAD
    # -------------------------
    @task
    def load(data):
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users_etl (
                id INT PRIMARY KEY,
                name TEXT,
                email TEXT,
                city TEXT
            )
        """)

        for row in data:
            cursor.execute("""
                INSERT INTO users_etl (id, name, email, city)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING
            """, (row['id'], row['name'], row['email'], row['city']))

        conn.commit()
        cursor.close()
        conn.close()

    # -------------------------
    # FLOW
    # -------------------------
    raw = extract()
    clean = transform(raw)
    load(clean)


# Instantiate DAG
etl_pipeline()
