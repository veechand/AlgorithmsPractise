import numpy as np
import pygame
import sys
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board

def drop_piece(board, row, col, piece):
	board[row][col] = piece

def is_valid_location(board, col):
	return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

def print_board(board):
	print(np.flip(board, 0))

# def winning_move(board, piece):
# 	# Check horizontal locations for win
# 	for c in range(COLUMN_COUNT-3):
# 		for r in range(ROW_COUNT):
# 			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
# 				return True

# 	# Check vertical locations for win
# 	for c in range(COLUMN_COUNT):
# 		for r in range(ROW_COUNT-3):
# 			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
# 				return True

# 	# Check positively sloped diaganols
# 	for c in range(COLUMN_COUNT-3):
# 		for r in range(ROW_COUNT-3):
# 			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
# 				return True

# 	# Check negatively sloped diaganols
# 	for c in range(COLUMN_COUNT-3):
# 		for r in range(3, ROW_COUNT):
# 			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
# 				return True
from collections import namedtuple
QueueElement = namedtuple('QueueElement', ['row','column','player','count', 'direction'])
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

def winning_move(board, piece):
	print "In winning_move"
	queue = []
	for row in range(ROW_COUNT):
		for column in range(COLUMN_COUNT):
			if board[row][column] != piece:
				continue
			queue=[]
			for direction, adders in DIRECTION_CORDINATES.items():
				x,y = adders
				queue.append(QueueElement(row+x, column+y, piece, 1, direction))
			if isComplete(queue, board):
				print "Out of Winning Move"
				return True
	print "Out of Winning Move"
	return False


def isComplete(queue, board):
	while (len(queue) >0):
		queueElement = queue.pop(0)
		row, col, count, player, direction = queueElement.row, queueElement.column, queueElement.count, queueElement.player, queueElement.direction
		if row < 0 or row >= ROW_COUNT or col < 0 or col >= COLUMN_COUNT or board[row][col] != player :
			continue
		print row, col, count, player, direction
		if count == WIN_COUNT - 1:
			return True
		x, y = DIRECTION_CORDINATES[direction]
		newRow, newCol = row+x, col+y
		queue.append(QueueElement(newRow, newCol, player, count+1, direction))
	return False


def draw_board(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
			else: 
				pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			#print(event.pos)
			# Ask for Player 1 Input
			if turn == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 1)

					if winning_move(board, 1):
						label = myfont.render("Player 1 wins!!", 1, RED)
						screen.blit(label, (40,10))
						game_over = True


			# # Ask for Player 2 Input
			else:				
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 2)

					if winning_move(board, 2):
						label = myfont.render("Player 2 wins!!", 1, YELLOW)
						screen.blit(label, (40,10))
						game_over = True

			print_board(board)
			draw_board(board)

			turn += 1
			turn = turn % 2

			if game_over:
				pygame.time.wait(30000)