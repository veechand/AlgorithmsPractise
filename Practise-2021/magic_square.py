"""
Can this have negative numbers?
row * col can be max size 10
row and col can be different
"""
class Solution(object):
    def isAllRowHaveSameValue(self, value, rowSum, startRow, endRow, startCol, endCol):
        for curRow in range(startRow,endRow+1):
            colValueToSubtract = rowSum[curRow][startCol-1] if (startCol-1)>=0 else 0
            curValue = rowSum[curRow][endCol] - colValueToSubtract
            if len(value) == 1 and value[0] != None and curValue != value[0]:
                return False
            value[0] = curValue
        return True
    def isAllColumnsHaveSameValue(self, value, colSum, startRow, endRow, startCol, endCol):
        for curCol in range(startCol,endCol+1):
            rowValueToSubtract = colSum[startRow-1][curCol] if (startRow - 1)>=0 else 0
            curValue = colSum[endRow][curCol] - rowValueToSubtract
            if len(value) == 1 and value[0] != None and curValue != value[0]:
                return False
            # value[0] = curValue
        return True
    def isLeftToRightDiagonalHaveSameValue(self, grid, value, startRow, endRow, startCol, endCol):
        curRow = startRow
        curCol = startCol
        diagonalValue = 0
        while (curRow <= endRow and curCol <= endCol):
            diagonalValue += grid[curRow][curCol]
            curRow += 1
            curCol += 1
        print "In di", value[0]
        return diagonalValue == value[0]
    def isRightToLeftDiagonalHaveSameValue(self, grid, value, startRow, endRow, startCol, endCol):
        curRow = startRow
        curCol = endCol
        diagonalValue = 0
        while (curRow <= endRow and curCol >= 0):
            diagonalValue += grid[curRow][curCol]
            curRow += 1
            curCol -= 1
        print "inlef", value[0]
        return diagonalValue == value[0]
    
    def getColSum(self,rows, cols, grid):
        colSum = [[0 for _ in range(cols)] for j in range(rows)]
        for i in range(cols):
            colSum[0][i] = grid[0][i] 
        for i in range(1,rows):
            for j in range(cols):
                colSum[i][j] = colSum[i-1][j] + grid[i][j]
        return colSum
    def getRowSum(self,rows, cols, grid):
        rowSum = [[0 for _ in range(cols)] for j in range(rows)]
        for i in range(rows):
            rowSum[i][0] = grid[i][0]
        for i in range(rows):
            for j in range(1,cols):
                rowSum[i][j] = rowSum[i][j-1] + grid[i][j]
        return rowSum
    def isValuesDistinct(self, grid, startRow, endRow, startCol, endCol):
        bits = [0]*9
        print "here",startRow, endRow, startCol, endCol
        for curRow in range(startRow, endRow +1):
            for curCol in range(startCol, endCol +1):
                value = grid[curRow][curCol]
                print "value", value
                if value > 9 or value < 1:
                    return False
                if bits[value-1] == 1:
                    return False
                bits[value-1] = 1
        return True
        
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        colSum = self.getColSum(rows, cols, grid)
        rowSum = self.getRowSum(rows, cols, grid)
        totalMagicSquare = 0

        for i in range(rows):
            for j in range(cols):
                if i + 2 >= rows or j + 2 >= cols:
                    continue
                startRow, endRow, startCol, endCol = i, i+2, j, j+2
                value = [None]
                print rowSum
                print colSum
                if (self.isAllRowHaveSameValue(value, rowSum, startRow, endRow, startCol, endCol) and
                self.isAllColumnsHaveSameValue(value, colSum, startRow, endRow, startCol, endCol) and
                self.isLeftToRightDiagonalHaveSameValue(grid, value, startRow, endRow, startCol, endCol) and
                self.isRightToLeftDiagonalHaveSameValue(grid, value, startRow, endRow, startCol, endCol) and
                self.isValuesDistinct(grid,startRow, endRow, startCol, endCol)):
                    totalMagicSquare += 1
        return totalMagicSquare