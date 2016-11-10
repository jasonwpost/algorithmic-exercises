# Count number of crossing wires 

# Given a list of wire positions on two buildings, count the number crossing wires
# wires can't share the same position

# input is divided up into lines - first line is number of test cases
# second line is number of wires
# rest of the lines represent the wire positions (i.e. 5 4 means position 5 on
# one building, and 4 on another)

# This problem is basically just adapting the Divide and Conquer inversions problem

import math
#from builtins import input

class Case:

	def __init__(self, size):
		self.size = size
		self.wiresA = []
		self.wiresB = []
		self.max_length = 0

	def addCase(self, x, y):
		length = self.computeLength(x, y)
		newCase = (x, y, length)
		self.wiresA.append(x)
		self.wiresB.append(y)

	def computeLength(self, x, y):
		length = math.fabs(y - x);
		if (length > self.max_length):
			self.max_length = length
		return length

	# using in built function - sort lists based on elements of wiresA
	def checkandSort(self):
		combined = list(zip(self.wiresA, self.wiresB))
		#print(combined)
		combined.sort()
		self.wiresA = [a[0] for a in combined]
		self.wiresB = [b[1] for b in combined]


	# returns list of wires of longest length in the set (can be draws)
	def returnListOfLongestLength(self):
		solution = []
		i = 0
		for item in self.wires:
			if item[2] == self.max_length:
				solution.append(i+1)
			i += 1
		return solution



def formatOutput(caseNum, result):
	result = str(result)
	print("Case #{}: {}".format(caseNum, result))


# takes list of wires, returns result()
def countInversionsHandler(case):
	#prep for mergesort
	case.checkandSort()
	result = countStageOne(case.wiresB)
	return result[0]


# breaking the list down
def countStageOne(lst):
	if len(lst) == 0 or len(lst) == 1:
		return 0, lst # returning base case - no inversion + the list given
	else:
		# usual mergeSorty stuff, with added inversion counters
		mid = int(len(lst)/2)
		leftCount, leftResult = countStageOne(lst[:mid])
		rightCount, rightResult = countStageOne(lst[mid:])
		#resolve the two counted/sorted lists
		totalCount, totalResult = countStageTwo(leftResult,rightResult)

		return (leftCount+rightCount+totalCount),totalResult

# merging the lists together and calculating num of inversions
def countStageTwo(leftList, rightList):
	result, leftPointer, rightPointer = 0, 0, 0
	mergedList = []
	lengthOfLeftList = len(leftList)
	lengthOfRightList = len(rightList)
	
	while leftPointer < lengthOfLeftList and rightPointer < lengthOfRightList:
		# trival case
		if leftList[leftPointer] <= rightList[rightPointer]:
			mergedList.append(leftList[leftPointer])
			leftPointer += 1
		# problem case
		else:
			mergedList.append(rightList[rightPointer])
			rightPointer += 1

			# Right list is all technically sorted - any inversions will
			# only come from left side as left side should be all completed

			# calculate the inversion.
			result += (lengthOfLeftList - leftPointer) 

	# copy remaining elements from left
	if (leftPointer != lengthOfLeftList):
		for i in range(leftPointer,lengthOfLeftList):
			mergedList.append(leftList[i])

	# copy remaining elements from right
	if (rightPointer != lengthOfRightList):
		for i in range(rightPointer, lengthOfRightList):
			mergedList.append(rightList[i])


	#print (result)
	return result, mergedList


# # # # # # # # # # # #
# Program starts here #
# # # # # # # # # # # #

cases = [] # will hold the case sizes

# handles input of cases
numOfCases = input()
numOfCases = int(numOfCases)
for num in range(numOfCases):
	
	numberForThisCase = input() # get number of wires
	numberForThisCase = int(numberForThisCase)
	temp = Case(numberForThisCase) # make new case object
	for num in range(numberForThisCase): # read in different wires for each this
		read = raw_input()
		read = read.split(" ")
		read = map(int, read)
		temp.addCase(read[0], read[1])
	#temp.checkandSort()
	cases.append(temp)

# handles output of cases
i = 1
for case in cases:
	formatOutput(i, countInversionsHandler(case))
	i = i+1