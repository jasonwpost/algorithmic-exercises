# Exam Creation Problem

# We have a database of exam questions and we would like to create
# an exam with the questions in the data base. We have specific topics 
# and specific difficulty levels we would like to include in our exam 
# and we want to know if there are enough questions in the database for 
# us to create the exam

# input is broken up by input lines: 
# {number of questions in database} {number of questions we want}
# {k strings representing difficulty}
# {k strings representing the topics we want}
# and the remaining lines represent the database:
# {name of question} {topic of question} {difficulty of question}





# Trick is to model this like a bipartitle graph with network flow

# We first build the graph with the database provided - the difficulties and
# topics avaiable serve as nodes, while the edge capacities serve as the number
# of questions availble at that difficulty - i.e. hard - math might have a 
# capacity of 2. 

# we then set sources and sinks from the intial information - i.e. if 2 easy,
# 1 medium, 1 hard is specified, the easy, medium and hard sources will be
# set as such, and the sinks wil be set the same way. If these set in a way
# that the graph doesn't support, we return No, otherwise we carry onto the
# FF Algorithm to find if an assignment is possible. If so, return Yes, else
# we return no.



from collections import Counter
import string
import networkx as nx
#import matplotlib.pyplot as mpl # testing

def getInput():
	numOfLoops = int(raw_input())
	for i in range(0, numOfLoops):
		currentResult = "nothing"
		specifications = raw_input()
		specifications = specifications.split(" ")
		specifications = map(int, specifications)

		numOfQInDB = specifications[0] # num of qs in database
		numOfQReq = specifications[1] # num of qs requested

		difficultiesReq = raw_input()
		difficultiesReq = difficultiesReq.split(" ")
		difficulty = "d"
		difficultiesReq = [x + difficulty for x in difficultiesReq]
		topicsReq = raw_input()
		topicsReq = topicsReq.split(" ")
		topic = "t"
		topicsReq = [x + topic for x in topicsReq]
		qsInDB = []
		for n in range(0, numOfQInDB):
			q = raw_input()
			q = q.split(" ")

			qsInDB.append(q)

		if numOfQReq > numOfQInDB:
			print("No")
			currentResult = "No"
		# Construct the graph


		# work out diff and topic vertices
		difficultyVertices = {"default":"default"}
		edges = {"default":"default"}
		topicVertices = {"default":"default"}
		for q in qsInDB:

			difKey = q[2] + difficulty
			topV = q[1] + topic
			edge = difKey
			if edge in edges:
				# if this edge alredy exists, check that the target of this edge exists too
				if topV in edges[edge]:
					edges[edge][topV] += 1 #update capacity
				else:
					edges[edge][topV] = 1
			else:
				edges[edge] = {topV : 1}

			if difKey in difficultyVertices:
				difficultyVertices[difKey][1] += 1 # update degree of nodes
			else:
				difficultyVertices[difKey] = [0, 1]

			if topV not in topicVertices:
				topicVertices[topV] = [0, 0]# update list of topics
		topicVertices.pop('default')
		difficultyVertices.pop("default")
		edges.pop('default')

		# We should now have our network - now we can assign weights to them and
		# do some basic checking

		topicsReq = dict(Counter(topicsReq))
		difficultiesReq = dict(Counter(difficultiesReq))
		for diff in difficultiesReq:
			# if not in our graph, return no
			if currentResult == "No":
				break
			elif diff not in difficultyVertices:
				#print(difficultyVertices)
				#print(diff)
				print("No")
				currentResult = "No"
			# if we want more questions in this difficult level than we have
			# return no
			elif difficultiesReq[diff] > difficultyVertices[diff][1]:
				print("No")
				currentResult = "No"
			# else, assign this as to node a demand
			else:
				difficultyVertices[diff][0] = difficultiesReq[diff]
		# same thing for topicsReq		
		for topic in topicsReq:
			# if not in graph, return no
			if currentResult == "No":
				break
			if topic not in topicVertices:
				print("No")
				currentResult = "No"
			# else, assign this as to node a demand
			else:
				topicVertices[topic][0] = topicsReq[topic]
		# if any of the tests have failed - we just print no and go back

		if currentResult == "No":
			continue
		
		#print(difficultyVertices)
		#print(topicVertices)
		#print(edges)
		# else, we can set up the graph and run ford fulkerson
		G = nx.DiGraph()
		for source in edges:
			for target in edges[source]:
				G.add_edge(source, target, capacity = edges[source][target])

		sourceAmount = 0
		for v in difficultiesReq:
			G.add_edge("source", v, capacity = difficultiesReq[v])
			sourceAmount += difficultiesReq[v]
		for v in topicsReq:
			G.add_edge(v, "sink", capacity = topicsReq[v])

		flow = nx.maximum_flow_value(G, 'source', 'sink')
		if flow == sourceAmount:
			print("Yes")
		else:
			print("No")

		'''
		# Testing
		pos = nx.spring_layout(G)
		pos.update((n, (1, i)) for i, n in enumerate(["source"]))
		pos.update((n, (2, i)) for i, n in enumerate(difficultyVertices))
		pos.update((n, (3, i)) for i, n in enumerate(topicVertices))
		pos.update((n, (4, i)) for i, n in enumerate(["sink"]))

		nx.draw_networkx_nodes(G, pos)
		nx.draw_networkx_labels(G, pos)
		nx.draw_networkx_edges(G, pos, arrows = True)
		mpl.show()
		'''


getInput()
