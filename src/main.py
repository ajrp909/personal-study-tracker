from fastapi import FastAPI

from src.utils import new_csv, csv_formatter

CSV_FILEPATH = "src/questions.csv"

NUMBER_OF_QUESTIONS = 500

questions = csv_formatter(CSV_FILEPATH)

if not questions:
    new_csv(CSV_FILEPATH, NUMBER_OF_QUESTIONS)
    questions = csv_formatter(CSV_FILEPATH)

app = FastAPI()

@app.get("/")
async def root():
    return "Short question study tracker.\
    difficulty range: 1 is easy 5 is hard 0 is unattempted"
