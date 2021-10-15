class Solution(object):
    def __init__(self):
        self.MAX = 2**32
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        result = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        memo = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 0:
                    continue
                minimumDistance = self.findMinimumDistanceToZero(row, col, mat, memo,[], 0)
                result[row][col] = minimumDistance
        return result
    
    def findMinimumDistanceToZero(self, row, col, mat, memo, visited, count):
        if (row,col) in visited:
            return self.MAX
        visited.append((row,col))
        if row >= len(mat) or col >= len(mat[0]) or row < 0 or col < 0:
            visited.pop(-1)
            return self.MAX
        # print row,col
        if memo[row][col] != -1:
            return count + memo[row][col]
        if mat[row][col] == 0:
            visited.pop(-1)
            return count
        bottom = self.findMinimumDistanceToZero(row+1, col, mat, memo, visited, count+1)
        # print "bottom", bottom
        top = self.findMinimumDistanceToZero(row-1, col, mat,memo, visited, count+1)
        # print "top", top
        left = self.findMinimumDistanceToZero(row, col-1, mat, memo,visited, count+1)
        # print "left", left
        right = self.findMinimumDistanceToZero(row, col+1, mat, memo,visited, count+1) 
        # print "right", right
        minimumValue =  min(bottom,top,left,right)
        if minimumValue != self.MAX:
            memo[row][col] = minimumValue - count
        # print visited
        visited.pop(-1)
        return minimumValue

# solution = Solution()
# mat = [[0,1,1,0,0],[0,1,1,0,0],[0,1,0,0,1],[1,1,1,1,0],[1,0,0,1,0]]
# memo = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
# # result = solution.findMinimumDistanceToZero(4, 0, mat, memo, [], 0)
# result = solution.updateMatrix(mat)
# print result