from flask import Flask
from flask import request
import sqlite3
import plotly.plotly as py
from plotly.graph_objs import *

app = Flask(__name__)


@app.route('/create_question_database')
def create_question_database():
    # create connection to examsystem.sqlite database, creates the database if
    # it doesn't already exist
    conn = sqlite3.connect("examsystem.sqlite")

    # provides are cursor to the above connection (the means of executing the
    # SQL queries)
    cursor = conn.cursor()

    # execute the create table query
    cursor.execute("create table testquestion (id integer primary key autoincrement,\
        question text, answerA text, answerB text,answerC text,\
        answerD text, correctanswer text)")

    # inset a row into the testquestion table
    cursor.execute(
        "insert into testquestion(id, question, answerA, answerB, answerC, answerD, correctanswer)\
        values(null,'The study of similarities and differences in the behavior of different species is called','biology','comparative psychology',\
            'environmental psychology','differential psychology','C')")

    conn.commit()  # commit changes to the database
    conn.close()  # close the connection
    return ""


@app.route('/create_User_Score_table')
def create_User_Score_table():
    # create connection to examsystem.sqlite database, creates the database if
    # it doesn't already exist
    conn = sqlite3.connect("examsystem.sqlite")

    # provides are cursor to the above connection (the means of executing the
    # SQL queries)
    cursor = conn.cursor()

    # execute the create table query
    cursor.execute("create table userscore (userName text, score text)")
    conn.commit()  # commit changes to the database
    conn.close()  # close the connection
    return ""


@app.route('/handle_form_data_submit_question', methods=['POST'])
def handle_form_data_submit_question():
    question = request.form["question"]
    answerA = request.form["answerA"]
    answerB = request.form["answerB"]
    answerC = request.form["answerC"]
    answerD = request.form["answerD"]
    correctanswer = request.form["correctanswer"]

    conn = sqlite3.connect("examsystem.sqlite")
    cursor = conn.cursor()
    # inset a row into the testquestion table
    cursor.execute("insert into testquestion(id, question, answerA, answerB, answerC, answerD, correctanswer)\
        values(null,?,?,?,?,?,?)", (question, answerA, answerB, answerC, answerD, correctanswer))
    conn.commit()
    conn.close()
    return ""


@app.route('/input_question')
def input_question():
    message = ""
    message += "<h1 align='center'>Please input question & answer:</h1>"
    message += "<form action='handle_form_data_submit_question' align='center' method='POST'><br>"
    message += "<table align='center'>"
    message += "<tr><td align='right'>Question: </td><td><textarea cols='40' rows='4'\
     name='question'></textarea></td></tr>"
    message += "<tr><td align='right'>A: </td><td ><input size='40' type=text name='answerA'></td></tr>"
    message += "<tr><td align='right'>B: </td><td ><input size='40' type=text name='answerB'></td></tr>"
    message += "<tr><td align='right'>C: </td><td ><input size='40' type=text name='answerC'></td></tr>"
    message += "<tr><td align='right'>D: </td><td ><input size='40' type=text name='answerD'></td></tr>"
    message += "<tr><td align='right'>Correct Answer(A-D): </td><td><input size='40' type=text name='correctanswer'></td></tr>"
    message += "<tr><td colspan=2 align='center'><input type=submit name='submit'></td></tr>"
    message += "</table>"
    message += "</form>"
    return message


@app.route('/do_exam')
def do_exam():
    return ""


@app.route('/show_grade')
def show_grade():
    conn = sqlite3.connect("examsystem.sqlite")
    cursor = conn.cursor()
    result = cursor.execute("select * from userscore")
    gradeList = result.fetchall()
    conn.commit()
    conn.close()

    theNames = []
    theScores = []
    totalScore = 0
    message = ""
    message += "<h1 align='center'>Interviewee's Grade</h1>"
    message += "<table align='center'>"
    message += "<tr><th width='100'>Name</th><th width='100'>Grade</th></tr>"
    for i in range(len(gradeList)):
        theNames.append(gradeList[i][0])
        theScores.append(int(gradeList[i][1]))
        totalScore += int(gradeList[i][1])
        message += "<tr><td width='100' align='center'><font size='4'>" + gradeList[i][0] +\
            "</td><td width='100' align='center'><font size='4'>" + \
            gradeList[i][1] + "</td></tr>"
    theScores.sort()
    message += "<tr><td colspan=2 align='center'>Max:" + \
        str(theScores[len(theScores) - 1]) + "</td></tr>"
    message += "<tr><td colspan=2 align='center'>Min:" + \
        str(theScores[0]) + "</td></tr>"
    message += "<tr><td colspan=2 align='center'>Average:" + \
        str(totalScore / len(theScores)) + "</td></tr>"
    message += "</table>"

    data = Data([
        Bar(
        x=theNames,
        y=theScores
        )])
    plot_url = py.plot(data, filename='Interviewee Grade')



    return message

app.run(debug=True)
