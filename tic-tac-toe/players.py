#!/usr/bin/env python

from gamelogic import *
from boards import *
from display import *
import sys
import curses

class player:
    selection=[]
    def __init__(self,choice='X'):
        self.symbol=choice
    def choosePosition(choice):
        self.position=choice
    def returnSymbol(self):
        return self.symbol

class computer:
    selection=[]
    def __init__(self,choice):
        self.symbol= 'O' if choice == 'X' else 'O'
        
    def returnSymbol(self):
        return self.symbol


def main():

    global selectedPositions
    newBoard=gameBoard()
    newBoard.drawBoard()

    pl=player()
        
    userchoice=raw_input("Please select your symbol: X or O")
    while userchoice not in ['X','O','x','o']:
        userchoice=raw_input("Please select valid symbol: X or O")

    pl.symbol=userchoice.upper()
        
    pl=player(userchoice.upper())
    co=computer(userchoice.upper())
    print "User",pl.returnSymbol(),"Computer",co.returnSymbol()

    while 1:
        userchoice=raw_input("Its your turn, make a selection")
        while not makeUserSelection(userchoice):
            userchoice=raw_input("Make a valid choice. either the position is already filled")
        newBoard.drawBoard(int(userchoice),pl.symbol)
        pl.selection.append(pow(2,int(userchoice)))
        if checkWinner(pl):
            print "Player you win"
            break
        
        compchoice=aiChoice(int(userchoice))
        while not makeUserSelection(compchoice):
            compchoice=aiChoice(int(userchoice))
        newBoard.drawBoard(int(compchoice),co.symbol)
        co.selection.append(pow(2,int(userchoice)))

        if checkWinner(co):
            print "Player you loose"
            break
        
        
if __name__=='__main__':
    main()
