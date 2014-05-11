"""


"""
import sys

spacelist=[[' ']*3+[' ']+[' ']*3+['|']]*2+[' ']*3+[' ']+[' ']*3
class gameBoard:
    #board=[]
    def __init__(self):
        self.board=['       |       |       ',
                    '       |       |       ',
                    '       |       |       ',
                    ' ------ ------- ------ ',
                    '       |       |       ',
                    '       |       |       ',
                    '       |       |       ',
                    ' ------ ------- ------ ',
                    '       |       |       ',
                    '       |       |       ',
                    '       |       |       ']
        
    def drawBoard(self,pos=10,val=' ',rowlen=21):
        if pos <=3:
            self.board[1]=self.board[1][:7*pos-3]+val+self.board[1][7*pos-2:]
        elif pos <=6:
            pos-=3
            self.board[5]=self.board[5][:7*pos-3]+val+self.board[5][7*pos-2:]
        elif pos <=9:
            pos-=6
            self.board[9]=self.board[9][:7*pos-3]+val+self.board[9][7*pos-2:]

        for row in range(len(self.board)):
            sys.stdout.write('\033[%d;%dH%s' % (row+1,1,self.board[row]))
	    
	#print self.board


def main():
    bd=gameBoard()
    bd.drawBoard()
    bd.drawBoard(3,'x')
    bd.drawBoard(5,'o')
    
if __name__=='__main__':
    main()
    
