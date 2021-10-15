from collections import namedtuple
import copy
import random
import pprint
import sys
from trial1_details import *

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
	 IF all the rows in the boards are filled
	"""
	def isBoardComplete(self, board=None):
		board = board if board else self.board
		for col in range(MAX_COLUMN):
			if self.isValidColumn(col):
				return False
		return True

	def getAllEmptyColumns(self):
		result = []
		for col in range(MAX_COLUMN):
			if self.isValidColumn(col):
				result.append(col)
		return result

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

	def isTerminalNode(self, board, player):
		return self.isWinningMove(player, board) or self.isBoardComplete(board)

	def scoreBoard(self, player):
		"""
		Yet to be implemented
		Score Card is something that tells how good is this board status
		So if there's a continuous four you add some value 
		and if 3 some other value
		and if opponent has same thing you decrement some value
		"""
		score = 0
		curCol = MAX_COLUMN//2
		for row in range(MAX_ROW):
			if self.board[row][curCol] == player:
				score+=3
		otherPlayer = PLAYER1 if player == PLAYER2 else PLAYER2
		#Horizontal
		for row in range(0, MAX_ROW):
			for col in range(0, MAX_COLUMN-3):
				if self.board[row][col] == player and self.board[row][col+1] == player and self.board[row][col+2] == player and self.board[row][col+3] == player:
					score = score + 100
				if self.board[row][col] == player and self.board[row][col+1] == player and self.board[row][col+2] == player and self.board[row][col+3] == EMPTY:
					score = score + 10
				if self.board[row][col] == player and self.board[row][col+1] == player and self.board[row][col+2] == EMPTY and self.board[row][col+3] == EMPTY:
					score = score + 5
				if self.board[row][col] == otherPlayer and self.board[row][col+1] == otherPlayer and self.board[row][col+2] == otherPlayer and self.board[row][col+3] == EMPTY:
					score = score - 10
		#Vertical
		for col in range(0, MAX_COLUMN):
			for row in range(0, MAX_ROW-3):
				if self.board[row][col] == player and self.board[row+1][col] == player and self.board[row+2][col] == player and self.board[row+3][col] == player:
					score = score + 100
				if self.board[row][col] == player and self.board[row+1][col] == player and self.board[row+2][col] == player and self.board[row+3][col] == EMPTY:
					score = score + 10 
				if self.board[row][col] == player and self.board[row+1][col] == player and self.board[row+2][col] == EMPTY and self.board[row+3][col] == EMPTY:
					score = score + 5
				if self.board[row][col] == otherPlayer and self.board[row+1][col] == otherPlayer and self.board[row+2][col] == otherPlayer and self.board[row+3][col] == EMPTY:
					score = score - 10

		#Left-Right Diagonal
		for row in range(0, MAX_ROW-3):
			for col in range(0, MAX_COLUMN-3):
				if self.board[row][col] == player and self.board[row+1][col+1] == player and self.board[row+2][col+2] == player and self.board[row+3][col+3] == player:
					score = score + 100
				if self.board[row][col] == player and self.board[row+1][col+1] == player and self.board[row+2][col+2] == player and self.board[row+3][col+3] == EMPTY:
					score = score + 10 
				if self.board[row][col] == player and self.board[row+1][col+1] == player and self.board[row+2][col+2] == EMPTY and self.board[row+3][col+3] == EMPTY:
					score = score + 5
				if self.board[row][col] == otherPlayer and self.board[row+1][col+1] == otherPlayer and self.board[row+2][col+2] == otherPlayer and self.board[row+3][col+3] == EMPTY:
					score = score - 10
			#Right-Left Diagonal
		if DEBUG:
			print "Score", score
		return score

	def chooseAPosition(self, player):
		value, location = self.minimax(DEPTH, player, True)
		return location[1]

	def minimax(self, depth, player, maximizingPlayer):
		if True:
			print "Depth={}, player={}".format(depth, player)
		isTerminal = self.isTerminalNode(self.board, player)
		if depth == 0 or isTerminal:
			if isTerminal:
				if DEBUG:
					print "In IsTerminal == True"
				if self.isWinningMove(PLAYER1):
					if DEBUG:
						print "This is a winning move for Player 1"
					return (MAX_VALUE, None)
				elif self.isWinningMove(PLAYER2):
					if DEBUG:
						print "This is a winning move for Player 2"
					return (MIN_VALUE, None)
				else:
					return (None, 0)
			else: # Depth got to zero
				if DEBUG:
					print "In IsTerminal == False"
				return (self.scoreBoard(PLAYER2), None)
		else:
			if maximizingPlayer:
				value = MIN_VALUE
				location = None
				possiblColumns = self.getAllEmptyColumns()
				for col in possiblColumns:
					row = self.getRowLocation(col)
					self.board[row][col] = PLAYER1
					score = self.minimax(depth-1, PLAYER1, False)[0]
					if DEBUG:
						print "In Player 1: Got the score as {} while the value is {}".format(score, value)
					if score > value:
						value = score
						location = (row, col)
					self.board[row][col] = EMPTY
				return (value, location)
			else:
				possiblColumns = self.getAllEmptyColumns()
				value = MAX_VALUE
				location = None
				for col in possiblColumns:
					row = self.getRowLocation(col)
					self.board[row][col] = PLAYER2
					score = self.minimax(depth-1, PLAYER2, True)[0]
					if DEBUG:
						print "In Player 2: Got the score as {} while the value is {}".format(score, value)
					if score < value:
						value = score
						location = (row, col)
					self.board[row][col] = EMPTY
				return (value, location)



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
	
	def isWinningMove(self, player, board=None):
		board = board if board else self.board
		# print "In winning_move"
		queue = []
		for row in range(MAX_ROW):
			for column in range(MAX_COLUMN):
				if self.board[row][column] != player:
					continue
				queue=[]
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
			column = self.getColumnLocation(player) if player == PLAYER1 else self.chooseAPosition(player)
			# column = self.getColumnLocation(player)
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

