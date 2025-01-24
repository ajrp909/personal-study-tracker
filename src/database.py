import psycopg2

def create_database(DATABASE_URL):
    with psycopg2.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute("""create table if not exists public.questions (
                                question_id integer primary key,
                                difficulty integer not null default 0,
                                correct boolean,    
                                date date);
                           """)
            
def seed_database(DATABASE_URL, questions_string):
    with psycopg2.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"""insert into public.questions
                values {questions_string};
                """)
            
def drop_database(DATABASE_URL):
    with psycopg2.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute("""drop table questions;
                           """)