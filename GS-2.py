class Man:
    ID = None
    isFree = True
    preferences = []
    index = 0

    engagedTo = None

    def __init__(self, ID):
        self.ID = ID

    #=== end of class definition

class Woman:
    ID = None
    isFree = True
    preferences = []
    inversePref = []
    engagedTo = None

    def __init__(self, ID):
        self.ID = ID

    #=== end of class


def getCase():
    numOfPref = int(input())
    # arraySize = numOfPref * numOfPref

    men = []
    women = []

    # get mens preferences

    rowCounter = 1
    while (rowCounter < (numOfPref+1)):

        temp = Man(rowCounter)

        rawInput = raw_input()
        rawInput = rawInput.split(" ")

        temp_list = []
        for char in rawInput:
            result = char[1:]
            result = int(result)
            temp_list.append(result)
        temp.preferences = temp_list
        temp.hasProposed = []
        men.append(temp)
        rowCounter += 1

    # get womens preferences

    rowCounter = 1
    while (rowCounter < (numOfPref+1)):

        temp = Woman(rowCounter)
        rawInput = raw_input()
        rawInput = rawInput.split(" ")
        temp_list = []
        temp_list_inverse = [0]*numOfPref
        char_counter = 0
        for char in rawInput:
            result = char[1:]
            result = int(result)
            # print(result-1)
            temp_list_inverse[result-1] = char_counter
            temp_list.append(result)
            char_counter += 1
        temp.preferences = temp_list
        temp.inversePref = temp_list_inverse
        '''
        for i in range(numOfPref):
            temp.inversePref.append(0)
        '''
        women.append(temp)
        rowCounter += 1


    for woman in women:
        '''
        for i in woman.preferences:
            toInsert = woman.preferences.index(i)
            woman.inversePref[i-1] = toInsert
            '''
        # print(woman.preferences)
        # print(woman.inversePref)




    getMatching(men, women)

    #===== end of getCase function


def getMatching(men, women):

    q = []

    for man in men:
        q.append(man)

    # The actual G-S bit
    while q != []:

        # get the next man from queue
        tempMan = q[0]
        del q[0]

        # get his next preference
        tempPref = tempMan.preferences[tempMan.index]

        # find the woman that is represented by the preference
        # tempWoman = None
        for w in women:
            if (tempPref == w.ID):
                tempWoman = w
                break

        # if she is free, assign m and w to be engaged
        if (tempWoman.isFree):
            tempWoman.engagedTo = tempMan
            tempWoman.isFree = False
            tempMan.engagedTo = tempWoman
            tempMan.isFree = False
            tempMan.index += 1

        # if she prefers him to his fiance
        elif (prefers(tempWoman, tempMan)):
            throwAway = tempWoman.engagedTo
            # deal with man
            throwAway.isFree = True
            throwAway.engagedTo = None
            q.insert(0, throwAway)
            # engage the other two
            tempWoman.engagedTo = tempMan
            tempMan.engagedTo = tempWoman
            tempMan.isFree = False
            tempMan.index += 1


        # the woman is rejecting the man
        else:
            tempMan.index += 1
            q.insert(0, tempMan)

    # print the result
    message = ""
    for man in men:
        message = message+"W" + str(man.engagedTo.ID) + " "
    print message

    # --- end of get matching function


# does the woman prefer this man to her current choice ?
def prefers(woman, man):
    currentChoiceIndex = woman.inversePref[woman.engagedTo.ID-1]
    potentialChoiceIndex = woman.inversePref[man.ID-1]
    # print(str(currentChoiceIndex) + " " + str(potentialChoiceIndex))
    if (currentChoiceIndex > potentialChoiceIndex):
        return True
    else:
        return False

    # == end of prefers function


numOfTestCases = int(input())

while (numOfTestCases > 0):
    getCase();
    numOfTestCases -= 1
