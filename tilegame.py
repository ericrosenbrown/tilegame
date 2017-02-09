import random
import copy
from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

goalConfiguration = [[1,2,3],[4,5,6],[7,8,9]]#the goal state of the tile game. DO NOT TOUCH

MARGIN = 30  #Size of buffer around the board
SIDE = 60  #Side of each board square
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 3 #Width and Height of the whole board, i.e. the Tkinter Canvas
globalExpandedNodes = 0 #Counts the number of expanded nondes per search algorithm. DO NOT TOUCH THIS VARIABLE. 
class gridDisplay(Frame):
    def __init__(self, parent, board):
        """
        Initialize an instance of the board within the TKinter hierarchy. Draws the game grid and fills it in
        with the current state of the board as passed into it by the displayBoard method. Numbers part of the 
        goal configuration are displayed in blue, the rest in black.
        """
        Frame.__init__(self, parent) 
        self.parent = parent 
        self.board = board
        self.pack(fill=BOTH)
        self.canvas = Canvas(self, width = WIDTH, height = HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)

        for i in xrange(4):
            color = "red" if (i == 0 or i == 3) else "gray" #Color the grid boundaries red.
            x0 = x1 = MARGIN + i * SIDE
            y0 = MARGIN
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
            self.canvas.create_line(y0, x0, y1, x1, fill=color)

        for i in xrange(3):
            for j in xrange(3):
                answer = self.board[i][j] #Current state of board at i,j
                if answer != 0:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    original = goalConfiguration[i][j] #Goal state of board at i, j
                    color = "blue" if answer == original else "black" #Number printed in blue if part of goal state, black if not.
                    self.canvas.create_text(x, y, text=answer, tags="numbers", fill=color)

def generateBoard():
    """
    Parses the tFile for initial board configurations, chooses one, and assigns it to the board
    """
    aboard = []
    nums = range(1,10);
    random.shuffle(nums)
    aboard.append([nums[0],nums[1],nums[2]])
    aboard.append([nums[3],nums[4],nums[5]])
    aboard.append([nums[6],nums[7],nums[8]])

    return aboard
    

def displayBoard(board):
    """
    Displays the current board, both printed to the console as well as in a pop up graphical window.
    """
    for x in range(3):
       print board[x]
    print "\n"
    root = Tk()
    gridDisplay(root, board)
    root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
    root.wm_title("Game Progress")
    root.mainloop()


def swapTiles(board,r1,c1,r2,c2):
    """
    Swaps tiles [r1][c1] with [r2][c2]. 0<=r1,r2,c1,c2<-=2
    """
    aboard = copy.deepcopy(board)
    
    temp = aboard[r1][c1]
    aboard[r1][c1] = aboard[r2][c2]
    aboard[r2][c2] = temp
    return aboard

def expandableStates(board):
    global globalExpandedNodes
    globalExpandedNodes += 1
    expandable = []
    for i in range(9):
        for x in range(-1,2):
            for y in range(-1,2):
                if x != y and (-1*x != y):
                    indexX = i/3
                    indexY = i%3
                    if indexX+x >= 0 and indexX+x <=2 and indexY+y >=0 and indexY+y <=2:
                        temp = swapTiles(copy.deepcopy(board),indexX,indexY,x+indexX,y+indexY)
                        if not temp in expandable:
                            expandable.append(copy.deepcopy(temp))
    return expandable
                    

def isGoalState(board):
    return board == goalConfiguration
                    
def boardSolver(board):
    #DO NOT TOUCH THIS FUNCTION
    #This function takes in a board, runs BFS, DFS and A* on board, and counts the number of expanded nodes, then graphs them.
    global globalExpandedNodes
    bfsBoard = BFS(board)
    
    bfscount = globalExpandedNodes
    print "BFS used expandNodes " + str(bfscount) + " times."
    globalExpandedNodes = 0
    
    dfsBoard = DFS(board)

    dfscount = globalExpandedNodes
    print "DFS used expandNodes " + str(dfscount) + " times."
    globalExpandedNodes = 0
    
    aBoard = Astar(board,heuristic)
    
    acount = globalExpandedNodes
    acount = globalExpandedNodes
    print "A* used expandNodes " + str(acount) + " times."
    
    globalExpandedNodes = 0

    #BFS
    if isGoalState(bfsBoard):
        print ("[X] BFS has found the correct configuration!")
    else:
        print ("[ ] BFS has NOT found the correct configuration!")

    #DFS
    if isGoalState(dfsBoard):
        print ("[X] DFS has found the correct configuration!")
    else:
        print ("[ ] DFS has NOT found the correct configuration!")

    #A*
    if isGoalState(aBoard):
        print ("[X] A* has found the correct configuration!")
    else:
        print ("[ ] A* has NOT found the correct configuration!")

    grapher(bfscount,dfscount,acount)

def BFS(board):
    #TODO: FILL IN.
    return board

def DFS(board):
    #TODO: FILL IN
    return board

def Astar(board,heuristic):
    #TODO: FILL IN
    return board

def heuristic(board):
    #This function should use the board state to make an estimate of the path to the goal.
    return 0

def grapher(bfs,dfs,astar):
    #TODO: FILL IN
    pass


if __name__ == '__main__':
    #You can do whatever you want here, you'll only be graded on BFS, DFS, Astar and heuristic.
    
    originalBoard = generateBoard()
    newBoard = swapTiles(originalBoard,0,0,1,1)
    print isGoalState(newBoard)
    boardSolver(newBoard)
    displayBoard(originalBoard)

            
