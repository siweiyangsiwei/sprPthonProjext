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

def get_user(id):
    sql_str = "SELECT * from user WHERE id =\'" + id + "\'"
    cur.execute(sql_str)
    data = cur.fetchall()
    return data

def update_user(sec_list):
    # sql_str = "UPDATE user set time_1 =" + sec_list[0] + ",time_2 =" + sec_list[1] + ",time_3 =" + sec_list[2] +",time_4 =" + sec_list[3]+",time_5 =" + sec_list[4]+",time_6 =" + sec_list[5]+",time_7 =" + sec_list[6]+",time_8 =" + sec_list[7]+",time_9 =" + sec_list[8]+",total_time =" + sec_list[9]+"WHERE id=admin"
    sql_str = "UPDATE user SET time_1 =?,time_2 =?,time_3 =?,time_4 =?,time_5 =?,time_6 =?,time_7 =?,time_8 =?,time_9 =?,total_time =? WHERE id=\'admin\'"
    cur.execute(sql_str,sec_list)
    connect.commit()




