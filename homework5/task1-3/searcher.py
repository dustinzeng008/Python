from datetime import datetime
import shelve


def search(shelve_file):
    s = shelve.open(shelve_file)
    data_dict = s["data_dict"]
    s.close()
    name = input("Hi, What's your name? ")
    print("Hello, " + name + "! Welcome to the search engine!")
    print("Please enter multiple keywords and boolean operators!")
    searchMore = "yes"  # check if search more

    while(searchMore == "yes"):
        queryString = input("query:")
        splitData = set(queryString.split())
        # record it is (and operation) or (or operation)
        andOrOperation = -1

        # get search keyword
        if (("or" in splitData) and ("and" not in splitData)):
            splitData.remove("or")
            print("Performing OR search for: " + str(splitData) + "\n")
            andOrOperation = 0
        elif (("or" in splitData) and ("and" in splitData)):
            splitData.remove("or")
            splitData.remove("and")
            print("Performing AND search for: " + str(splitData) + "\n")
            andOrOperatoutputSet = [] = 1
        elif (("or" not in splitData) and ("and" in splitData)):
            splitData.remove("and")
            print("Performing AND search for: " + str(splitData) + "\n")
            andOrOperation = 1
        else:
            print("Performing AND search for: " + str(splitData) + "\n")
            andOrOperation = 1

        splitData = list(splitData)
        outputSet = []

        # search keyword
        dt1 = datetime.now()
        if (andOrOperation == 0):  # if it is (or operation)
            for n in range(len(splitData)):
                if splitData[n] in data_dict.keys():
                    outputSet = list(
                        set(outputSet).union(set(data_dict[splitData[n]])))
        else:  # if it is (and operation)
            if splitData[0] in data_dict.keys():
                outputSet = data_dict[splitData[0]]
                for n in range(1, len(splitData)):
                    if splitData[n] in data_dict.keys():
                        outputSet = list(
                            set(outputSet).intersection(set(data_dict[splitData[n]])))
            else:
                print("Found Nothing!")
        dt2 = datetime.now()

        for value in outputSet:
            print("Found at " + str(value) + "\n")
        print("Execution time:", dt2.microsecond - dt1.microsecond)

        searchMore = input("\nDo you want to search more (yes or no)? ")
        while(searchMore != "yes" and searchMore != "no"):
            searchMore = input("\nDo you want to search more (yes or no)? ")
    print("Bye-bye")
