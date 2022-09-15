import sqlite3

connect = sqlite3.connect("test.db")

cur = connect.cursor()


def get_question_by_chapter(chapter):
    sql_str = "SELECT * from main.test WHERE chapter = \'" + chapter + "\'"
    cur.execute(sql_str)
    data = cur.fetchall()
    return data


def get_correct_answer_by_chapter(chapter):
    data = get_question_by_chapter(chapter)
    correct_answer = []
    for question in data:
        correct_answer.append(question[7])
    return correct_answer
