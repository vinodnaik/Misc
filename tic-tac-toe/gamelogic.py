#!/usr/bin/env python

import random
import sys

selectedPositions=[]

blocklist=[[2,3,4,5,7,9],
           [1,3,5,8],
           [1,2,6,9],
           [1,7,5,6],
           [1,2,3,4,5,6,7,8,9],
           [3,4,5,9],
           [3,5,8,9,1,4],
           [2,5,7,9],
           [1,5,7,8,3,6],]

wins = [7, 56, 448, 73, 146, 292, 273, 84]

def aiChoice(userSelection):
    return random.choice(list(set(blocklist[userSelection-1])-set(selectedPositions)))


def makeUserSelection(userSelection):
    if int(userSelection) in selectedPositions:
        print "Position $userSelection already selected"
        return False
    else:
        selectedPositions.append(int(userSelection))
        return True


def checkWinner(plr):
    global wins
    if len(plr.selection) <=2:
        return False
    i=0
    j=1
    

def main():
    print aiChoice(int(sys.argv[1]))

if __name__=='__main__':
    main()
