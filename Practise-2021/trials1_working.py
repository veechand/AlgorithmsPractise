from collections import namedtuple
import random
import pprint
import sys

MAX_ROW = 6
MAX_COLUMN = 7

DEBUG = False
EMPTY = "-"
Piece = namedtuple('Piece', ['x','y'])
QueueElement = namedtuple('QueueElement', ['row','column','player','count', 'direction'])

PLAYER1 = "Y"
PLAYER2 = "R"

TOP = "T"
BOTTOM = "B"
LEFT = "L"
RIGHT = "R"
RIGHT_BOTTOM_DIAGONAL = "RBD"
LEFT_BOTTOM_DIAGONAL = "LBD"
RIGHT_TOP_DIAGONAL = "RTD"
LEFT_TOP_DIAGONAL = "LTD"

DIRECTION_CORDINATES = {
    TOP: (-1, 0),
    BOTTOM: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1),
    LEFT_BOTTOM_DIAGONAL: (1, -1),
    LEFT_TOP_DIAGONAL: (-1, 1),
    RIGHT_TOP_DIAGONAL: (-1, -1),
    RIGHT_BOTTOM_DIAGONAL: (1, 1)
}
WIN_COUNT = 4

class Solution(object):
	def __init__(self):
		self.board = [[EMPTY for _ in range(MAX_COLUMN)] for _ in range(MAX_ROW)]

	def placePiece(self, row, column, player):
		if self.board[row][column] != EMPTY:
			raise Exception("Position already occupied")
		self.board[row][column] = player

	def isValidColumn(self, inputColumn):
		return inputColumn < MAX_COLUMN and  self.board[-1][inputColumn] == EMPTY  # That's the last row is not filled

	"""
	Get the column location from the user
	"""
	def getColumnLocation(self, player):
		inputColumn = None
		while inputColumn == None or not self.isValidColumn(inputColumn):
			inputColumn = input("Enter a column to place ({})".format(player))
		return inputColumn

	def pickRandomColumn(self):
		inputColumn = random.randint(0, MAX_COLUMN)
		while not self.isValidColumn(inputColumn):
			inputColumn = random.randint(0, MAX_COLUMN)
		return inputColumn
		

	"""
	Get the last unfilled row on the board
	"""
	def getRowLocation(self, column):
		for row in range(MAX_ROW):
			if self.board[row][column] == EMPTY:
				return row
	def printBoard(self):
		# pprint.pprint(self.board)
		print "==================================================="
		for row in range(MAX_ROW-1,-1,-1):
			for col in range(MAX_COLUMN):
				print "{}    ".format(self.board[row][col]),

			print

	def isComplete(self, queue):
		while (len(queue) >0):
			queueElement = queue.pop(0)
			row, col, count, player, direction = queueElement.row, queueElement.column, queueElement.count, queueElement.player, queueElement.direction
			if row < 0 or row >= MAX_ROW or col < 0 or col >= MAX_COLUMN or self.board[row][col] != player :
				continue
			if DEBUG:
				print "row={},col={},count={},player={},direction={}".format(row, col, count, player, direction)
			if count == WIN_COUNT - 1:
				return True
			x, y = DIRECTION_CORDINATES[direction]
			if DEBUG:
				print "My X={}, Y={}".format(x,y)
			newRow, newCol = row+x, col+y
			if DEBUG: 
				print "row={},col={},newRow={},newCol={},direction={}".format(row, col, newRow, newCol, direction)
			queue.append(QueueElement(newRow, newCol, player, count+1, direction))
		return False

	"""
	This method is going to check only the rows that are corresponding to the currently changed row and columns
	"""
	def isThisAWinningMove(self, player, changedRow, changedCol):
		#Vertical
		count = 0
		for i in range(-3,4):
			if changedRow-i < 0 or changedRow-i >= MAX_ROW:
				continue
			if self.board[changedRow-i][changedCol] == player:
				count += 1
				if count == WIN_COUNT:
					return True
			else:
				count = 0
		#Horizontal
		count = 0
		for i in range(-3,4):
			if changedCol-i < 0 or changedCol-i >= MAX_COLUMN:
				continue
			if self.board[changedRow][changedCol-i] == player:
				count += 1
				if count == WIN_COUNT:
					return True
			else:
				count = 0
		# LEFT-RIGHT Diagonal
		count = 0
		for i in range(3,-1,-1):
				if changedRow-i < 0 or changedRow-i >= MAX_ROW or changedCol-i < 0 or changedCol-i >= MAX_COLUMN:
					continue
				if self.board[changedRow-i][changedCol-i] == player:
					count += 1
					if count == WIN_COUNT:
						return True
				else:
					count = 0
		for i in range(1,4):
				if changedRow+i < 0 or changedRow+i >= MAX_ROW or changedCol+i < 0 or changedCol+i >= MAX_COLUMN:
					continue
				if self.board[changedRow+i][changedCol+i] == player:
					count += 1
					if count == WIN_COUNT:
						return True
				else:
					count = 0

		#RIGHT-LEFT Diagonal
		count = 0
		for i in range(3,-1,-1):
			if changedRow+i < 0 or changedRow+i >= MAX_ROW or changedCol-i < 0 or changedCol-i >= MAX_COLUMN:
				continue
			if self.board[changedRow+i][changedCol-i] == player:
				count += 1
				if count == WIN_COUNT:
					return True
			else:
				count = 0			
		for i in range(1,4):
			if changedRow-i < 0 or changedRow-i >= MAX_ROW or changedCol+i < 0 or changedCol+i >= MAX_COLUMN:
				continue
			if self.board[changedRow-i][changedCol+i] == player:
				count += 1
				if count == WIN_COUNT:
					return True
			else:
				count = 0
		return False
	
	def isWinningMove(self, player):
		# print "In winning_move"
		queue = []
		for row in range(MAX_ROW):
			for column in range(MAX_COLUMN):
				if self.board[row][column] != player:
					continue
				queue=[]a
				for direction, adders in DIRECTION_CORDINATES.items():
					x,y = adders
					queue.append(QueueElement(row+x, column+y, player, 1, direction))
				if DEBUG:
					print "Processing row {} col {}".format(row, column)
					pprint.pprint(queue)
				if self.isComplete(queue):
					return True
		if DEBUG:
			print "Out of Winning Move"
		return False



	def playGame(self):
		player = PLAYER1 if random.randint(0,1) == 0 else PLAYER2
		while True:
			# column = self.getColumnLocation(player) if player == PLAYER1 else self.pickRandomColumn()
			column = self.getColumnLocation(player)
			row = self.getRowLocation(column)
			self.placePiece(row, column, player)
			self.printBoard()
			if self.isWinningMove(player):
			# if self.isThisAWinningMove(player, row, column):
				print "{} Wins !! :-D".format(player)
				sys.exit(0)
			player = PLAYER1 if player == PLAYER2 else PLAYER2
			


"""
The challenge with this is isWinningMove will do a complete BFS 
3 3 2 4 4 2 2 3 3 0 4 4 1 1 0 2 2 	1 0 24 6 6 66 6 6 55
"""				





if __name__ == "__main__":
	solution = Solution()
	solution.playGame()


