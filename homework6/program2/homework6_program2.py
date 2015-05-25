from random import randrange


def learnIntegerDivision(dividentRange, divisorRange):
    a = randrange(dividentRange)
    b = randrange(1, divisorRange)
    try:
        ans = input("{} / {} = ".format(a, b))
        if int(ans) == (a // b):
            print("CORRECT!")
        else:
            print("INCORRECT!")
    except ValueError:
        print("Please enter Integers Only!")
    except Exception as e:
        print(type(e))
        print(e.args)
        print(e)


print("INTEGER DIVISIONS")
dividentRange = input("Please input the area of divident(0-?): ")
divisorRange = input("Please input the area of divisor(1-?): ")
questionNumber = input("How many question do you want to test: ")

for i in range(int(questionNumber)):
    learnIntegerDivision(int(dividentRange), int(divisorRange))
