from tkinter import *
from tkinter import messagebox
import sqlite3



color = "#CCFFCC"


def submitTest():
    score = 0
    if userName.get() == "" or len(answerList) != len(questionList):
        messagebox.showinfo(
            "Alert", "Check you have input name and you have completed all question")
    else:
        for i in range(len(questionList)):
            if answerList[i].upper() == questionList[i][6].upper():
                score += 1
        conn = sqlite3.connect("examsystem.sqlite")
        cursor = conn.cursor()
        # inset a row into the userscore table
        cursor.execute("insert into userscore(userName, score)\
            values(?,?)", (userName.get(), score))
        conn.commit()
        conn.close()
        messagebox.showinfo("Your Score: ", str(score))

answerList = []


def nextQuestion():
    global currentQuestionIndex
    if answer.get() == "":
        messagebox.showinfo(
            "Alert", "please input answer")
    else:
        answerList.append(answer.get())
        currentQuestionIndex += 1
        if currentQuestionIndex <= len(questionList):
            labelQuestion.config(text="Question " + str(currentQuestionIndex) + "/" + str(
                len(questionList)) + ": " + questionList[currentQuestionIndex - 1][1])
            labelA.config(
                text="A: " + questionList[currentQuestionIndex - 1][2])
            labelB.config(
                text="B: " + questionList[currentQuestionIndex - 1][3])
            labelC.config(
                text="C: " + questionList[currentQuestionIndex - 1][4])
            labelD.config(
                text="D: " + questionList[currentQuestionIndex - 1][5])
        else:
            messagebox.showinfo("Alert", "This is the last question")
        answer.delete(0, END)


conn = sqlite3.connect("examsystem.sqlite")
cursor = conn.cursor()
result = cursor.execute("select * from testquestion")
questionList = result.fetchall()
conn.commit()
conn.close()

base = Tk()
base.title("Job interview examization")
#base["bg"] = color
base.geometry("500x500")

frame = Frame(base)
frame.pack()
labelName = Label(frame, text="Name: ")
userName = Entry(frame)
labelName.pack(side=LEFT)
userName.pack(side=LEFT)


currentQuestionIndex = 1
labelQuestion = Label(
    base, text="Question " + str(currentQuestionIndex) + "/" + str(len(questionList)) + ": " + questionList[currentQuestionIndex - 1][1])
labelQuestion.pack(anchor=W)

labelA = Label(base, text="A: " + questionList[currentQuestionIndex - 1][2])
labelA.pack(anchor=W)
labelB = Label(base, text="B: " + questionList[currentQuestionIndex - 1][3])
labelB.pack(anchor=W)
labelC = Label(base, text="C: " + questionList[currentQuestionIndex - 1][4])
labelC.pack(anchor=W)
labelD = Label(base, text="D: " + questionList[currentQuestionIndex - 1][5])
labelD.pack(anchor=W)

frame1 = Frame(base)
frame1.pack()
labelAnswer = Label(frame1, text="Answer(A to D): ")
answer = Entry(frame1)
labelAnswer.pack(side=LEFT)
answer.pack(side=LEFT)

nextQuestion = Button(base, text="Next", command=nextQuestion)
submit = Button(base, text="submit", command=submitTest)
nextQuestion.pack()
submit.pack()

#button = Button(base, text="submit", command=submitTest,highlightbackground=color)
# button.pack()
base.mainloop()
