# Knight's Shortest Path problem

# Given integers X and Y (representing number of squares in a X * Y board), 
# print the smallest number of moves needed for a knight to traverse the 
# board from corner to corner, and the number of possible paths with that
# number of moves. 

# This is a dynamic programming problem


knight_moves_hor = [-2, -2, 2, 2, -1, -1, 1, 1]
knight_moves_ver = [-1, 1, -1, 1, -2, 2, -2, 2]
output = []

import string

def getInput():
	result = None
	validKnightPath = True # while there is a valid Knight Path
	while(validKnightPath):
		read = raw_input()
		read = read.split(" ")
		read = map(int, read)
		result = isValidCase(read)
		if result == None:
			validKnightPath = False
	if len(output) > 0:
		for res in output:
			print(str(res[0]) + " " + str(res[1]))
			pass

def isValidCase(case):
	global knight_moves_ver
	global knight_moves_hor
	global output
	horiSize = case[0]
	vertSize = case[1]
	adjList = {'default':'default'}
	letters = []

	# create adjacency list
	for vnum in range(1, vertSize+1):
		for hnum in range(1, horiSize+1):
			key = (hnum, vnum)
			values = []
			for i in range(len(knight_moves_hor)):
				phor = hnum+knight_moves_hor[i]
				pver = vnum+knight_moves_ver[i]
				if doesExist(phor, pver, horiSize, vertSize):
					values.append((phor, pver))
			adjList[key] = values
	result = countPaths(adjList, (1, 1), (horiSize, vertSize))
	if result is not None:
		output.append(result)
		return True
	else:
		return None



def countPaths(adjList, sourceNode, destinationNode):
	count = {"default":"default"}
	for vertex in adjList:
		count[vertex] = 0
	count[sourceNode] = 1

	steps = {"default":"default"}
	steps[sourceNode] = 0

	queue = set()
	queue.add(sourceNode)
	while queue:
		next_queue = set()
		for to_process in queue:
			for node in adjList[to_process]:
				if node not in steps:
					steps[node] = steps[to_process] + 1
					next_queue.add(node)
				if steps[node] == steps[to_process] + 1:
					count[node] = count[node] + count[to_process]
		queue = next_queue

	if destinationNode not in steps:
		return None
	else:
		return (str(steps[destinationNode]), str(count[destinationNode]))




def doesExist(horizontalPosition, verticalPosition, horiSize, vertSize):

	if (verticalPosition >= 1 and verticalPosition <= vertSize and horizontalPosition >= 1 and horizontalPosition <= horiSize):
		return True
	else:
		return False



getInput()