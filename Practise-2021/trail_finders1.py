"""
Connect Four is a game where two players take turns dropping their color discs into a vertically suspended grid. 
The game ends when a player adds a disc to the playing grid that connects four discs of their color. 
The connected discs can be in a horizontal, vertical or diagonal line. 
Write a function to be called after every turn that returns true if the game is over (and false otherwise).
"""

"""
 Using Stack 
 Storing of values
"""


class QueueElement(object):
    row = None
    col = None
    color = None
    count = None
    direction = None

    def __init__(self, row, col, color, count, direction):
        self.row = row
        self.col = col
        self.color = color
        self.count = count
        self.direction = direction
    def __str__(self):
        return "Row={},col={},color={},count={},direction={}".format(self.row, self.col, self.color, self.count, self.direction)
    def __repr__(self):
        return self.__str__()


class Solution(object):
    def __init__(self, grid):
        self.WIN_COUNT = 4
        self.visited = []
        self.grid = grid
        self.queue = []
        self.TOP = "T"
        self.BOTTOM = "B"
        self.LEFT = "L"
        self.RIGHT = "R"
        self.RIGHT_DIAGONAL = "RD"
        self.LEFT_DIAGONAL = "LD"
        self.DIRECTION_CORDINATES = {
            self.TOP: (-1, 0),
            self.BOTTOM: (1, 0),
            self.LEFT: (0, -1),
            self.RIGHT: (0, 1),
            self.LEFT_DIAGONAL: (1, -1),
            self.RIGHT_DIAGONAL: (1, 1)
        }
        # self.DIRECTION_CORDINATES_ON_MOVE = {
        #     self.HORIZONTAL : [(0,-1),(0,1)],
        #     self.VERTICAL : [(-1,0),(1,0)],
        #     self.FORWARD_DIAGONAL: [(-1,-1),(1,1)],
        #     self.REVERSE_DIAGONAL: [(-1,1),(1,-1)]
        # }
        self.dp = {}

    def isCountAlreadyMet(self, row, col, direction, count):        
        return  (row, col, direction) in self.dp and self.dp[(row, col, direction)] + count >= self.WIN_COUNT
                
    def isExistsInDp(self, row, col, direction):
        return (row, col, direction) in self.dp

    # def addToQueueIfApplicableOneMove(self, coordinate, direction, count, row, col):
    #     pass

    def addToQueueIfApplicable(self, coordinate, direction, count, row, col):
        x, y = coordinate
        newRow = None
        newCol = None 
        if direction in (self.TOP, self.BOTTOM) and 0 <= row+x < len(self.grid) and self.grid[row+x][col] == self.grid[row][col]:
            newRow = row+x
            newCol = col
        elif direction in (self.RIGHT, self.LEFT) and 0 <= col+y < len(self.grid[0]) and self.grid[row][col+y] == self.grid[row][col]:
            newRow = row
            newCol = col+y
        elif direction in (self.LEFT_DIAGONAL, self.RIGHT_DIAGONAL) and row+x < len(self.grid) and row+x >= 0 and  col+y < len(self.grid[0]) and col+y >= 0 and self.grid[row+x][col+y] == self.grid[row][col]:
            newRow = row+x
            newCol = col+y
        # print row, col, newRow, newCol, direction
        if newRow != None and newCol != None:
            # print newRow, newCol
            if self.isExistsInDp(newRow, newCol, direction):
                print "Available in DP"
                if self.isCountAlreadyMet(newRow, newCol, direction, count):
                    return True
            else:
                # print "Inserted"
                self.queue.append(QueueElement(newRow, newCol, self.grid[row][col], count, direction))
        return False

    # def addToQueueIfApplicableOnMove(self, direction, count, row, val):
    #     coordinateAdders = self.DIRECTION_CORDINATES_ON_MOVE[direction]
    #     for adder in coordinateAdders:
    #         x,y = adder
    #         self.queue.append(QueueElement(row+x, col+y, self.grid[row][col], count, direction))

    def isGameOver(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if not self.grid[row][col]:
                    continue
                for direction, coordinate in self.DIRECTION_CORDINATES.items():
                	isGameOver = self.addToQueueIfApplicable(coordinate, direction, 1, row, col)
                self.visited = []
                # print self.queue
                if self.isComplete():
                    print "The winner is", self.grid[row][col]
                    return True
        return False
    def checkForWin(self, coordinatesLocations, row, col):
        if len(coordinatesLocations) < self.WIN_COUNT:
            return False
        count = 0
        for loc in coordinatesLocations:
            rowValue, colValue = loc
            if count >= self.WIN_COUNT-1:
                return True
            if self.grid[rowValue][colValue] == self.grid[row][col]:
                count += 1
            else:
                count = 0
        return count >= self.WIN_COUNT-1
    def filterApplicableResults(self, results):
        return filter(lambda (row,col): row>=0 and col>=0 and row<len(self.grid) and col<len(self.grid[0]), results)
    """
     The above checks the complete Grid. 
     This one checks only a the last changed row and column
     So I need to do BFS around that (row, col)
    """
    def isGameOverOnMove(self, row, col):
        # Horizontal check
        print "Horizontal"
        count = 0
        result = []
        for colValue in range(col-3, col+3):
            result.append((row, colValue))
        result = self.filterApplicableResults(result)
        if self.checkForWin(result, row, col):
            return True
        # Vertical Check
        print "Vertical"
        result = []
        for rowValue in range(row-3, row+3):
            result.append((rowValue, col))
        result = self.filterApplicableResults(result)
        if self.checkForWin(result, row, col):
            return True
            # print (rowValue, col)
        # Diagonal - 1
        print "Diagonal-1"
        result = []
        for i in range(3,-1,-1):
            result.append((row-i,col-i))
        for i in range(1,4):
            result.append((row+i,col+i))
        result = self.filterApplicableResults(result)
        print result
        if self.checkForWin(result, row, col):
            return True

        print "Diagonal-2"
        result=[]
        for i in range(3,-1,-1):
            result.append((row+i,col-i))
        for i in range(1,4):
            result.append((row-i,col+i))
        result = self.filterApplicableResults(result)
        print result
        if self.checkForWin(result, row, col):
            return True             
        return False
        # for rowValue in range(row-3, row+3):
        #     for colValue in range(col-3, col+3):
        #         print (rowValue, colValue)
        #         break
        # Diagonal - 2
        # for rowValue in range(row-3, row+3):
        #     for colValue in range(col-3, col+3):
        #         print (rowValue, colValue)


    # def isGameOverOnMove(self, row, col):
    #     for direction, coordinate in self.DIRECTION_CORDINATES_ON_MOVE.items():
    #         isGameOver = self.addToQueueIfApplicableOnMove(coordinate, direction, 1, row, col)
    #     if self.isCompleteOnMove():
    #         print "The winner is ", self.grid[row][col]
    #         return True
    #     return False

    # def isCompleteOnMove(self):
    #     while(len(self.queue) > 0):
    #         queueElement = self.queue.pop(0)
    #         if queueElement.count == self.WIN_COUNT - 1:
    #             return True
    #         row = queueElement.row
    #         col = queueElement.col
    #         count = queueElement.count
    #         color = queueElement.color
    #         # print "In Queue", row, col, count
    #         if row >= len(self.grid) or row < 0 or col >= len(self.grid[0]) or col < 0 or self.grid[row][col] != color
    #             continue

    #         direction = queueElement.direction
    #         # coordinate = self.DIRECTION_CORDINATES[direction]
    #         # self.dp[(row,col, direction)] = count
    #         self.visited.append((row,col))
    #         self.addToQueueIfApplicableOnMove(coordinate, direction, count+1, row, col)


    def isComplete(self):
        while(len(self.queue) > 0):
            queueElement = self.queue.pop(0)
            if queueElement.count == self.WIN_COUNT - 1:
                return True
            row = queueElement.row
            col = queueElement.col
            count = queueElement.count
            # print "In Queue", row, col, count
            direction = queueElement.direction
            coordinate = self.DIRECTION_CORDINATES[direction]
            self.dp[(row,col, direction)] = count
            self.visited.append((row,col))
            if self.addToQueueIfApplicable(coordinate, direction, count+1, row, col):
                return True

if __name__ == "__main__":
    grid = [[1, None, None, 1], [1, 0, 1, 0], [0, 1, None, 1], [1, 1, 0, None]]
    # grid = [[1, None, None, 1], [1, 0, 1, 0], [1, None, None, 1], [1, 1, 0, None]]
    # grid = [[1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 0], [0, 0, 1,1]]
    # grid = [[1, 1,1,0], [1, 1, 1, 0], [1, 1, 1, 0], [0,0, 0,0]]
    solution = Solution(grid)
    if(solution.isGameOverOnMove(3, 0)):
        print "Winning Move"
    else:
        print "Game Continues..."
