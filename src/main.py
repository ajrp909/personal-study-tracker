import os

import sys

import psycopg2

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

from datetime import datetime

from dotenv import load_dotenv

from src.utils import create_questions_string

from src.database import create_database, seed_database, drop_database

load_dotenv()

DATABASE_URL = os.environ['DATABASE_URL']

NUMBER_OF_QUESTIONS: int = 500

EXAM_DATE: datetime = datetime.strptime('5 Jun 2025','%d %b %Y')

questions_string = create_questions_string(NUMBER_OF_QUESTIONS)

if "drop" in sys.argv:
    if input("return 'Y' to confirm table deletion: ").lower() == 'y':
        try:
            drop_database(DATABASE_URL)
        except:
            print("exception1")
if "seed" in sys.argv:
    try:
        create_database(DATABASE_URL)
    except:
        print("exception2")
    try:
        seed_database(DATABASE_URL,questions_string)
    except:
        print("exception3")
if len(sys.argv) != 1:
    sys.exit()

class Question(BaseModel):
    question_id: int
    difficulty: int
    correct: bool
    date: datetime

app = FastAPI()

@app.get("/")
async def root():
    return "Short question study tracker.\
    difficulty range: 1 is easy 5 is hard 0 is unattempted"

# @app.get("/questions")
# async def question_summary():
    # questions_remaining = len([question for question in questions if question.split(",")[1] == "0"])
    # time_remaining = EXAM_DATE - datetime.now()
    # days_left = time_remaining.days
    # questions_per_day = questions_remaining//days_left + 1
    # return (f"questions_remaining: {questions_remaining}",
    #         f"days left: {days_left}",
    #         f"questions per day: {questions_per_day}")

# @app.get("/question/{question_id}")
# async def question_id_call(question_id: int):
#     if 0 < question_id < len(questions):
#         return questions[question_id]
#     raise HTTPException(status_code=404, detail="Question {question_id} not found")

# @app.put("/question/{question_id}/{difficulty}/{correct}")
# async def question_update(question_id: int, difficulty: int, correct: bool):
#     if 0 < question_id < len(questions):
#         question_update_string = f"{question_id},{difficulty},{correct},{datetime.now()}"
#         questions[question_id] = question_update_string
#         update_csv(CSV_FILEPATH, questions)
#         return f"Question {question_id} was updated to {question_update_string}"
#     raise HTTPException(status_code=404, detail="Question {question_id} not found")