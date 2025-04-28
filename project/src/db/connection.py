import os
import psycopg2


def get_connection():
    try:
        return psycopg2.connect(
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASS"],
            host=os.environ["POSTGRES_HOST"],
            port=os.environ["POSTGRES_PORT"],
        )
    except KeyError as e:
        raise KeyError(f"Missing required environment variable: {e}")
    except psycopg2.Error as e:
        raise Exception(f"Failed to connect to the database: {e}")
