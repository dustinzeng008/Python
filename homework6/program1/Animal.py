class Animal:
    def __init__(self, animalName):
        self.animalName = animalName
        self.hintData = {"elephant": ["I have exceptional memory",
                                      "I am the largest land-living mammal in the world",
                                      "I have long nose"],
                         "tiger": ["I am the biggest cat",
                                   "I come in black and white or orange and black",
                                   "I am apex predators, primarily preying on ungulates such as deer and bovids"],
                         "bat": ["I use echo-location",
                                 "I can fly",
                                 "I see well in dark"]
                         }

    def guess_who_am_i(self):
        print("I will give you 3 hints, guess what animal I am" + "\n")
        guessSuccess = False
        for i in range(3):
            print(self.hintData[self.animalName][i])
            guessName = input("Who am I?: ")
            if guessName == self.animalName:
                print("You got it! I am " + guessName + "\n\n")
                guessSuccess = True
                break
            else:
                print("Nope, try again!" + "\n")
        if not guessSuccess:
            print("I'm out of hints! The answer is: " + self.animalName + "\n\n")
