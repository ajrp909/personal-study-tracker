def csv_formatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

def new_csv(filepath, number_of_questions):
    with open(filepath, "w", encoding='utf-8') as file:
        file.write("question_id, difficulty, correct, date\n")
        for i in range(1, number_of_questions):
            line = f"{i},0,None,None\n"
            file.write(line)
        file.write(f"{number_of_questions},0,None,None")
