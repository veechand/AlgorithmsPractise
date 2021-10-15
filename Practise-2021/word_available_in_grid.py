"""
words are available in m * n ?
Adjacent Cells : Horizontally and Vertically neighboring
How big is the word array - 30000
For each element in the words:
  start_from grid[0][0] and do a BFS
  BFS will be added only if grid char matches with current char
  Need to see with each cell as the starting char
https://leetcode.com/problems/word-search-ii/
"""
import copy
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for word in words:
            if(self.isWordAvailableInBoard(board, word)):
                result.append(word)
        return result
    def isWordAvailableInBoard(self, board, word):
        if len(word) == 0:
            return False # Assuming all cells in grid will be having some alphabet
        startIndex = 0
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[startIndex]:
                    if(self.isWordAvailableStartingFrom(row,col,board,startIndex,word)):
                        return True
        return False
    def isWordAvailableStartingFrom(self,row,col,board,startIndex,word):
        queue = [(row,col, startIndex,set())]
        # visited = set() # This a set of visited tuples (row,col)
        while(len(queue)!=0):
            curRow, curCol, startIndex,visited = queue.pop(0)
            print curRow,curCol,startIndex, visited
            visited.add((curRow,curCol))
            if startIndex >= len(word) - 1:
                return True
            if curRow-1 >=0 and board[curRow-1][curCol] == word[startIndex+1] and (curRow-1,curCol) not in visited: # TOP
                queue.append((curRow-1,curCol,startIndex+1,copy.deepcopy(visited)))
                # visited.add((curRow-1,curCol))
            if curRow+1<len(board) and board[curRow+1][curCol] == word[startIndex+1] and (curRow+1,curCol) not in visited: # BOTTOM
                queue.append((curRow+1,curCol,startIndex+1,copy.deepcopy(visited)))
                # visited.add((curRow+1,curCol))
            if curCol-1 >=0 and board[curRow][curCol-1] == word[startIndex+1] and (curRow,curCol-1) not in visited: # LEFT
                queue.append((curRow,curCol-1,startIndex+1,copy.deepcopy(visited)))
                # visited.add((curRow,curCol-1))
            if curCol+1 < len(board[0]) and board[curRow][curCol+1] == word[startIndex+1] and (curRow,curCol+1) not in visited: # RIGHT
                queue.append((curRow,curCol+1,startIndex+1,copy.deepcopy(visited)))
                # visited.add((curRow,curCol+1))
        return False
        
                
        