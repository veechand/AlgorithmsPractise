"""
When a person who knows it meets any other person, they immediately share the story with them.
Initially, only person 1 knows the story. Given a list of meetings between people in a form of
(person_1_id, person_2_id, timestamp) construct a list of the persons who will know the story
at the very end.

Eg2: [(1, 2, 100), (2, 3, 100), (4, 5, 100)], 2
where the first parameter is array of the Persons meet at particular timestamp, second parameter is the PersonId who knows the story first.
Output: [1, 2, 3]
"""

from collections import deque
MAX_VALUE = 2**32

class GraphNode(object):
	value = None
	knownTimeStamp = None
	edges = [] # List of type Edge
	def __init__(self, value, knownTimeStamp = MAX_VALUE, edges = []):
		self.value = value
		self.knownTimeStamp = knownTimeStamp
		self.edges = edges
class GraphEdge(object):
	person1 = None # Of type Node
	person2 = None
	meetingTime = None
	def __init__(self, person1, person2, meetingTime):
		self.person1 = person1
		self.person2 = person2
		self.meetingTime = meetingTime

class Solution(object):
	def __init__(self):
		self.nodes = {}
	def constructGraph(self, meetings):
		# [(1, 2, 100), (3,4, 200), (1,3, 300), (2,5, 400)]
		for meeting in meetings:
			person1, person2, meetingTime = meeting
			person1Node = self.getPersonNode(person1)
			person2Node = self.getPersonNode(person2)
			person1Node.edges.append(GraphEdge(person1Node, person2Node, meetingTime))
			person2Node.edges.append(GraphEdge(person2Node, person1Node, meetingTime))

	def getPersonNode(self, personName):
		if personName not in self.nodes:
			self.nodes[personName] = GraphNode(personName, knownTimeStamp=MAX_VALUE, edges=[])
		return self.nodes[personName]

	def findPersonsWhoKnowsTheStory(self, root):
		queue = deque()
		queue.append(root)
		visitedNodes = []
		while(len(queue)>0):
			curNode = queue.popleft()
			visitedNodes.append(curNode.value)
			for edge in curNode.edges:
				if edge.person2.value not in visitedNodes:
					queue.append(edge.person2)
				if edge.meetingTime >= curNode.knownTimeStamp and edge.person2.knownTimeStamp > edge.meetingTime:
					edge.person2.knownTimeStamp = edge.meetingTime
		pass
	def printGraph(self):
		for key, value in self.nodes.items():
			print key
			for edge in value.edges:
				print edge.person1.value, edge.person2.value, edge.meetingTime
	def printStoryKnownNodes(self):
		for key, value in self.nodes.items():
			if value.knownTimeStamp != MAX_VALUE:
				print key, value.knownTimeStamp

if __name__ == "__main__":
	input_list = [(1, 2, 100), (3,4, 200), (1,3, 300), (2,5, 400)]
	firstKnownPerson = 3
	solution = Solution()
	solution.constructGraph(input_list)
	rootNode = solution.getPersonNode(firstKnownPerson)
	rootNode.knownTimeStamp = 0
	# solution.printGraph()
	solution.findPersonsWhoKnowsTheStory(rootNode)
	solution.printStoryKnownNodes()