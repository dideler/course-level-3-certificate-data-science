from db.connection import get_connection


def create_schema(conn):
    try:
        cur = conn.cursor()
        cur.execute("CREATE SCHEMA IF NOT EXISTS prod;")
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
        create_schema(conn)
    finally:
        conn.close()
