from collections import namedtuple

MAX_ROW = 6
MAX_COLUMN = 7
MIN_VALUE = -(2**32)
MAX_VALUE = 2**32
DEBUG = False
EMPTY = "-"
Piece = namedtuple('Piece', ['x','y'])
QueueElement = namedtuple('QueueElement', ['row','column','player','count', 'direction'])

PLAYER1 = "Y"
PLAYER2 = "R"
DEPTH = 2

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