from __future__ import division
from collections import defaultdict
import heapq

# class Graph(object):
# 	# name = None
# 	# edges = None
# 	# def __init__(self, name, edges):
# 	# 	self.name = name
# 	# 	self.edges = edges
# 	"""
# 	Key - Node Name
# 	Value - List of edges
# 	"""
# 	nodesDict = defaultdict(list)
# 	def __init__(self):
# 		pass

class Edge(object):
	source = None
	destination = None
	weight = None
	def __init__(self, source, destination, weight):
		self.source = source
		self.destination = destination
		self.weight = weight

class Solution(object):
	def __init__(self):
		self.graph = None
		self.HYPHEN = "-"
		self.KEYWORD_BID = "bid"
		self.KEYWORD_SELL = "ask"
	"""
	 @input: Map
	 @returns: Graph
	"""
	def buildGraph(self, tickerMap):
		graph = defaultdict(list)
		for ticker, price in tickerMap.items():
			tickerSrc, tickerDst = ticker.split(self.HYPHEN)
			srcDstExchangeRate = price[self.KEYWORD_BID]
			dstSrcExchangeRate = 1.0/price[self.KEYWORD_SELL]
			srcDstEdge = Edge(tickerSrc, tickerDst, srcDstExchangeRate)
			dstSrcEdge = Edge(tickerDst, tickerSrc, dstSrcExchangeRate)
			graph[tickerSrc].append(srcDstEdge)
			graph[tickerDst].append(dstSrcEdge)	
		self.graph = graph
	def findShortestDistance(self, src, dst):
		heap=[]
		visited = set()
		weightAndParentMap = {}
		heapq.heappush(heap, (0,src, None))
		while len(heap) > 0:
			weight, curElement, parent = heapq.heappop(heap)
			if curElement in visited:
				continue
			visited.add(curElement)
			weightAndParentMap[curElement] = (weight,parent)
			if curElement == dst:
				break
			for edge in self.graph[curElement]:
				heapq.heappush(heap, (weight+edge.weight,edge.destination,curElement))
		# print weightAndParentMap, visited
		print weightAndParentMap[dst][0],
		node = dst
		while node is not None:
			print node,
			node = weightAndParentMap[node][1]

		return weightAndParentMap[dst]


	def printGraph(self):
		for nodeName, edges in self.graph.items():
			print "Edges for source Node", nodeName
			for edge in edges:
				print edge.source, "-->", edge.destination, "-->", edge.weight
			print "====================="

if __name__ == "__main__":
	"""
	BTC - USD - Exchange Rate
	USD - BTC - Exchange
	BTC - EUR - Exchange Rate
	"""
	tickers = {
	  "BTC-USD": { "ask": 1000, "bid": 990 },
	  "BTC-EUR": { "ask": 1200, "bid": 1150 },
	  "BTC-ETH": { "ask": 220, "bid": 210 },
	  "ETH-EUR": { "ask": 220, "bid": 210 }
	}

	solution = Solution()
	solution.buildGraph(tickers)
	# solution.printGraph()
	solution.findShortestDistance("USD", "EUR")
	print 
	solution.findShortestDistance("EUR", "USD")
	print
	solution.findShortestDistance("ETH", "BTC")