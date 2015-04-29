def count_frequency(wordList):
    dictCounter={}
    for word in wordList:
        if word in dictCounter:         
            dictCounter[word] +=1
        else:
            dictCounter[word] = 1
    return dictCounter

mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
print(count_frequency(mylist))

