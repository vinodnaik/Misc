import sys
from boards import *

gamedata={}

"""
def writeBoard():
    global board
    for row in board:
        print row

writeBoard()
"""

bd=gameBoard()
bd.drawBoard(1,'X')
bd.drawBoard(5,'X')
bd.drawBoard(9,'X')
#bd.draw()

