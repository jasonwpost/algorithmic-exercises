class Man:
    ID = None
    preferences = []
    inversePref = []
    index = 0

    engagedTo = None

    def __init__(self, ID):
        self.ID = ID

    #=== end of class

class Woman:
    ID = None
    preferences = []
    inversePref = []
    engagedTo = None

    def __init__(self, ID):
        self.ID = ID

    #=== end of class

def getCase():
    numOfPref = int(input())
    notEnoughArgs = False

    men = []
    women = []
    matching = []

    # get mens preferences

    rowCounter = 1
    while (rowCounter < (numOfPref+1)):

        temp = Man(rowCounter)
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
        if len(temp.preferences) != numOfPref:
            notEnoughArgs = True

        men.append(temp)
        rowCounter += 1
    #print(men)

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
        if len(temp.preferences) != numOfPref:
            notEnoughArgs = True

        women.append(temp)
        rowCounter += 1

    # get propsed matching
    rawInput = raw_input()
    rawInput = rawInput.split(" ")
    i = 1
    for char in rawInput:
        result = char[1:]
        result = int(result)
        matching.append(result)
        men[i-1].engagedTo = result
        for woman in women:
            if woman.ID == result:
                woman.engagedTo = i
        i += 1

    # print(men)
    # print(women)
    # print(matching)

    #for p in men:
    #    print(p.engagedTo)
    #for w in women:
    #   print(w.engagedTo)
    notEnoughArgs = test_not_Engaged(men, women)


    if(notEnoughArgs):
        results.append(False)
        return

    checkStableMatching(men, women, matching, numOfPref)


def checkStableMatching(men, women, matching, numOfPref):
    #print("Hello")
    isStable = True

    # check every partner has a partner (definition one)
    if ((numOfPref != len(matching)) or (len(matching) != len(men)) or (len(matching) != len(women))):
        isStable = False
        results.append(isStable)
        return

    # manCoefficient = 0
    # for every match, lets check if
    for man in men:
        # man = men[manCoefficient]

        for pref in man.preferences:
            '''
            if pref == match:
                break # isStable
            else:
                '''
            # find the woman to compare
            womanToCompare = None
            for woman in women:
                if woman.ID == pref:
                    womanToCompare = woman
                    break

            if (prefers(man, womanToCompare)): # negative case
                isStable = False
                break
            else: # nothing unusal here - keep checking
                continue
        # manCoefficient+= 1

    results.append(isStable)


def prefers(woman, man):
    currentChoiceIndexF = woman.inversePref[woman.engagedTo-1]
    potentialChoiceIndexF = woman.inversePref[man.ID-1]
    currentChoiceIndexM = man.inversePref[man.engagedTo-1]
    potentialChoiceIndexM = man.inversePref[woman.ID-1]
    # print(str(currentChoiceIndex) + " " + str(potentialChoiceIndex))
    if ((currentChoiceIndexF > potentialChoiceIndexF) and (currentChoiceIndexM > potentialChoiceIndexM)):
        return True
    else:
        return False

    # == end of prefers function

def printStability(isStable):
    if (isStable):
        print("Yes")
    else:
        print("No")

def test_not_Engaged(men, women):
    for m in men:
        if m.engagedTo == None:
            return True
    for w in women:
        if w.engagedTo == None:
            return True

# starts here
results = []
numOfTestCases = int(input())

while (numOfTestCases > 0):
    getCase();
    numOfTestCases -= 1

for msg in results:
    printStability(msg)
