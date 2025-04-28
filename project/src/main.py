from dotenv import load_dotenv

from db.connection import get_connection

load_dotenv()

def main():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT 'foo';")
        print(cur.fetchone())
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        raise

if __name__ == "__main__":
    main()
