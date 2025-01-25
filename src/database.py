import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

from datetime import datetime

load_dotenv()

TABLE_NAME = "question"
DATABASE_URL = os.environ['DATABASE_URL']
DB_CONN = f"{DATABASE_URL}"

def sql_create_table():
    """Connects to a database and tries to create a table using the table_name parameter.
    Returns a string letting the user know if successful or unsuccessful.
    """
    try:
        table_name = TABLE_NAME
        query = "create table {} (question_id integer primary key, difficulty integer not null default 0, correct boolean, date date);"
        conn = psycopg2.connect(DB_CONN)
        cur = conn.cursor()
        cur.execute(sql.SQL(query).format(sql.Identifier(table_name)))
        conn.commit()
        cur.close()
        conn.close()
        print(f"{table_name} table created successfully.")
    except Exception:
        print(f"{table_name} table already exists.")

def sql_seed_table(questions):
    """Seeds a new table with expected data to be later updated by the user.
    """
    try:
        table_name = TABLE_NAME
        query = "insert into {} values (%s)"
        placeholder_list = [(i,) for i in range(1, questions + 1)]
        conn = psycopg2.connect(DB_CONN)
        cur = conn.cursor()
        cur.executemany(sql.SQL(query).format(sql.Identifier(table_name)), placeholder_list)
        conn.commit()
        cur.close()
        conn.close()
        print(f"{table_name} table seeded successfully, {placeholder_list[-1][0]} records inserted.")
    except Exception:
        print(f"seeding of {table_name} unsuccessful.")

    
def sql_delete_table():
    """drops table
    """
    try:
        query = "drop table {};"
        table_name = TABLE_NAME
        conn = psycopg2.connect(DB_CONN)
        cur = conn.cursor()
        cur.execute(sql.SQL(query).format(sql.Identifier(table_name)))
        conn.commit()
        cur.close()
        conn.close()
        print(f"{table_name} table deleted.")
    except Exception:
        print(f"{table_name} did not exist.")

def sql_count_total():
    try:
        query = "select count(*) from {};"
        table_name = TABLE_NAME
        conn = psycopg2.connect(DB_CONN)
        cur = conn.cursor()
        cur.execute(sql.SQL(query).format(sql.Identifier(table_name)))
        result = cur.fetchone()
        cur.close()
        conn.close()
        print("count successful.")
        return result
    except Exception:
        print("count unsuccessful.")

def sql_count_remaining():
    try:
        query = "select count(*) from {} where difficulty = 0;"
        table_name = TABLE_NAME
        conn = psycopg2.connect(DB_CONN)
        cur = conn.cursor()
        cur.execute(sql.SQL(query).format(sql.Identifier(table_name)))
        result = cur.fetchone()
        cur.close()
        conn.close()
        print("count successful.")
        return result
    except Exception:
        print("count unsuccessful.")

def sql_get_row(row_id):
    try:
        query = "select * from {} where question_id = %s;"
        placeholder = (row_id,)
        table_name = TABLE_NAME
        conn = psycopg2.connect(DB_CONN)
        cur = conn.cursor()
        cur.execute(sql.SQL(query).format(sql.Identifier(table_name)), placeholder)
        result = cur.fetchone()
        cur.close()
        conn.close()
        print("row retireved.")
        return result
    except Exception:
        print("row retrival unsuccessful.")

def sql_update(row_id, difficulty, correct):
    try:
        query = "update {} set difficulty = %s, correct = %s, date = %s where question_id = %s;"
        table_name = TABLE_NAME
        placeholder = (difficulty, correct, datetime.now(), row_id)
        conn = psycopg2.connect(DB_CONN)
        cur = conn.cursor()
        cur.execute(sql.SQL(query).format(sql.Identifier(table_name)), placeholder)
        conn.commit()
        cur.close()
        conn.close()
        print("record updated.")
    except Exception:
        print("update unsuccessful.")