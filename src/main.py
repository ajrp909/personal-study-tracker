from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

from datetime import datetime

from src.utils import new_csv, csv_formatter, update_csv

CSV_FILEPATH = "src/questions.csv"

NUMBER_OF_QUESTIONS = 500

EXAM_DATE = datetime.strptime('5 Jun 2025','%d %b %Y')

class Question(BaseModel):
    question_id: int
    difficulty: int
    correct: bool
    date: datetime

questions = csv_formatter(CSV_FILEPATH)

if not questions:
    new_csv(CSV_FILEPATH, NUMBER_OF_QUESTIONS)
    questions = csv_formatter(CSV_FILEPATH)

app = FastAPI()

@app.get("/")
async def root():
    return "Short question study tracker.\
    difficulty range: 1 is easy 5 is hard 0 is unattempted"

@app.get("/questions")
async def question_summary():
    questions_remaining = len([question for question in questions if question.split(",")[1] == "0"])
    time_remaining = EXAM_DATE - datetime.now()
    days_left = time_remaining.days
    questions_per_day = questions_remaining//days_left + 1
    return (f"questions_remaining: {questions_remaining}",
            f"days left: {days_left}",
            f"questions per day: {questions_per_day}")

@app.get("/question/{question_id}")
async def question_id_call(question_id: int):
    if 0 < question_id < len(questions):
        return questions[question_id]
    raise HTTPException(status_code=404, detail="Question {question_id} not found")

@app.put("/question/{question_id}/{difficulty}/{correct}")
async def question_update(question_id: int, difficulty: int, correct: bool):
    if 0 < question_id < len(questions):
        question_update_string = f"{question_id},{difficulty},{correct},{datetime.now()}"
        questions[question_id] = question_update_string
        update_csv(CSV_FILEPATH, questions)
        return f"Question {question_id} was updated to {question_update_string}"
    raise HTTPException(status_code=404, detail="Question {question_id} not found")