name=input("Hi, What's your name? ");
print("Hello "+ name +"! Let's play a game!");
print("Think of random number from 1 to 100,and I'll try to guess it!");
playMoreGame="yes";                       #check if game over
while(playMoreGame=="yes"):
    numberIsCorrect="no";                 #check if you guess a correct number
    maxValue=101;                         #max value the number should be 
    minValue=0;                           #min value the number should be
    times=0;                              #how many time do you guess
    number=(minValue+maxValue)//2;        #the number you guess
    while(numberIsCorrect!="yes"):        #break only when you input no
        times+=1;
        numberIsCorrect=input("Is it "+str(number)+"? (yes/no)");
        while(numberIsCorrect!="yes" and numberIsCorrect!="no"):
            numberIsCorrect=input("Is it "+str(number)+"? (yes/no)");
        if(numberIsCorrect=="no"):
            isLarger=input("Is the number larger than "+ str(number)+"? (yes/no)");
            while(isLarger!="yes" and isLarger!="no"):
                isLarger=input("Is the number larger than "+ str(number)+"? (yes/no)");
            if(isLarger=="yes"):
                minValue=number;
                number=(maxValue+minValue)//2;
            else:
                maxValue=number;
                number=(maxValue+minValue)//2
    print("Yeey! I got it in "+str(times)+" tries!");
    playMoreGame=input("Do you want to play more?")
    while(playMoreGame!="yes" and playMoreGame!="no"):
        playMoreGame=input("Do you want to play more?")
print("Bye-bye");

