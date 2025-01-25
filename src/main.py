from src.database import sql_count_total, sql_count_remaining, sql_update, sql_get_row, sql_create_table, sql_delete_table, sql_seed_table
from datetime import datetime
from fastapi import FastAPI

import sys

NUMBER_OF_QUESTIONS: int = 500

EXAM_DATE: datetime = datetime.strptime('5 Jun 2025','%d %b %Y')

if "drop" in sys.argv:
    sql_delete_table()
if "seed" in sys.argv:
    sql_create_table()
    sql_seed_table(NUMBER_OF_QUESTIONS)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/dashboard")
async def dashboard():
    questions_remaining, total_questions = sql_count_remaining()[0], sql_count_total()[0]
    time_remaining = EXAM_DATE - datetime.now()
    days_left = time_remaining.days
    questions_per_day = questions_remaining//days_left + 1
    return (f"questions attempted: {total_questions-questions_remaining}",
            f"questions remaining: {questions_remaining}",
            f"days left until exam: {days_left}",
            f"questions per day: {questions_per_day}"
            )

@app.get("/row/{row_id}")
async def get_row_by_id(row_id):
    result = sql_get_row(row_id)
    return result

@app.put("/update/{row_id}/{difficulty}/{correct}")
async def update_row(row_id, difficulty, correct):
    sql_update(row_id, difficulty, correct)
    return 200