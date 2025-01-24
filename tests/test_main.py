from src.utils import csv_formatter, new_csv

def test_csv_formatter():
    assert csv_formatter("tests/empty.csv") == []
    test = csv_formatter("tests/test.csv")
    assert len(test) == 6
    assert test[0] == "question_id, difficulty, correct, date"

def test_new_csv():
    new_csv("tests/test2.csv", 5)
    test = csv_formatter("tests/test2.csv")
    assert len(test) == 6
    assert test[0] == "question_id, difficulty, correct, date"