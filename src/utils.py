def create_questions_string(NUMBER_OF_QUESTIONS):
    questions_string = ""
    for i in range(1, NUMBER_OF_QUESTIONS):
        questions_string += f"({i}),"
    questions_string += f"({NUMBER_OF_QUESTIONS})"
    return questions_string

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

def update_csv(filepath, to_update):
    with open(filepath, "w", encoding='utf-8') as file:
        for i, v in enumerate(to_update):
            if i != len(to_update) - 1:
                file.write(v + "\n")
            else:
                file.write(v)