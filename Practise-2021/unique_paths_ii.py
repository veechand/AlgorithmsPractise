class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for i in range(0,  cols)] for j in range(0, rows)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(1,cols):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = 0
        for i in range(1,rows):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0
                
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        
        return dp[-1][-1]   