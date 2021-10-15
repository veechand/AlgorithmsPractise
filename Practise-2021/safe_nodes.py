"""
https://leetcode.com/problems/find-eventual-safe-states/submissions/
"""
from copy import copy

class Solution(object):
    """
        Find the cycle creating edges in the graph
    """
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        done = []
        processing = []
        waiting = []
        cycleNodes = set()
        waiting.extend(range(0,len(graph)))
        result = filter(lambda node: self.getNodesThatCreateCycles(graph, done, processing, waiting, cycleNodes, None, node), range(len(graph)))
        return result
        
    def getNodesThatCreateCycles(self, graph, done, processing, waiting, cycleNodes, parentNode, curNode):
        if curNode in waiting:
            waiting.remove(curNode)
        if curNode in processing:
            return False
        if curNode in done:
            return True
        processing.append(curNode)
        edges = graph[curNode]
        for edge in edges:
            if not self.getNodesThatCreateCycles(graph, done, processing, waiting, cycleNodes, curNode, edge):
                return False
        processing.remove(curNode)
        done.append(curNode)
        return True
        
                
            
            
            
        