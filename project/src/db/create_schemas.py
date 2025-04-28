from db.connection import get_connection


def create_schemas(conn):
    try:
        cur = conn.cursor()
        cur.execute("CREATE SCHEMA IF NOT EXISTS raw;")
        cur.execute("CREATE SCHEMA IF NOT EXISTS processed;")
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    conn = get_connection()
    try:
        create_schemas(conn)
    finally:
        conn.close()
