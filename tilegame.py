import random
import copy
from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
from random import shuffle

goalConfiguration = [[1,2,3],[4,5,6],[7,8,9]]#the goal state of the tile game. DO NOT TOUCH
expandedStates = 0

def generateBoard():
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

def swapTiles(board,r1,c1,r2,c2):
    """
    Swaps tiles [r1][c1] with [r2][c2]. 0<=r1,r2,c1,c2<-=2
    """
    aboard = copy.deepcopy(board)
    if ((r1+1 == r2 and c1 == c2) or (r1-1 == r2 and c1 == c2) or (c1+1 == c2 and r1 == r2) or (c1-1 == c2 and r1 == r2)): 
        temp = aboard[r1][c1]
        aboard[r1][c1] = aboard[r2][c2]
        aboard[r2][c2] = temp
        return aboard
    else:
        print "swapTiles was given non-adjacent tiles"
        return board

def expandableStates(board,reset):
    """given a board state, returns a list of all valid states that could be followed from here by swapping tiles"""
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
    if reset:
        expandedStates = 0
    else:
        expandedStates = expandedStaes + len(expandable)
    return expandable
                    

def isGoalState(board):
    return board == goalConfiguration
                    
def boardSolver(tFile):
    board = generateBoard(tFile)

    bfsBoard = BFS(board)
    dfsBoard = DFS(board)
    aBoard = Astar(board,heuristic)
    ucsBoard = UCS(board)

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

    #UCS board
    if isGoalState(ucsBoard):
        print ("[X] UCS has found the correct configuration!")
    else:
        print ("[ ] UCS has NOT found the correct configuration!")

def BFS(board):
    #TODO: FILL IN
    return board

def DFS(board):
    #TODO: FILL IN
    return board

def Astar(board,heuristic):
    #TODO: FILL IN
    return board

def UCS(board):
    #TODO: FILL IN
    return board

def heuristic(board):
    #TODO: FILL IN
    #This function should use the board state to make an estimate of the cheapest path to the goal.
    return board

def grapher(board,BFS,DFS,Astar,UCS,heuristic):
    #TODO: FILL IN
    #Run BFS,DFS,Astar and UCS on on the given board, and graph the number of nodes each expand.
    pass

if __name__ == '__main__':
    #TODO
    #You can use this function to experiment with your functions.
    #when you handin, only run boardSolver("tilePuzzles.txt") in this function.

    #boardSolver()
    
    originalBoard = generateBoard()
    displayBoard(originalBoard)
    newBoard = swapTiles(originalBoard,0,0,1,0)
    for es in expandableStates(newBoard):
        displayBoard(es)
    print isGoalState(newBoard)

            
