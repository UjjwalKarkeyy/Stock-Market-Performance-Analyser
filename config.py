import os
import psycopg2 as psql
from dotenv import load_dotenv

load_dotenv()

def create_conn():
    try:
        conn = psql.connect(
            host=os.getenv('HOST'),
            database=os.getenv('DB'),
            user=os.getenv('USER'),
            password=os.getenv('PASS'),
            port=os.getenv('PORT')
        )

        cur = conn.cursor()

        return cur, conn

    except Exception as err:
        raise err