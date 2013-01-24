import csplot
import time 
import random
from copy import deepcopy
from copy import copy

def createBoard(width, height=None):
    #creates a 2d array
    if height is None:  height=width
    return [ [0]*width for R in range(height) ]
    
def update1a(B):
    #adds a diagonal strip of "on" cells from SW corner
    
    width = len(B[0])
    height = len(B)
    Bnew = deepcopy(B)
    
    for row in range(height):
        for col in range(width):
            if row == col:
                Bnew[row][col] = 1
		
    return Bnew

def update1b(B):
   #adds a diagonal strip of "on" cells from NW corner
    
    width = len(B[0])
    height = len(B)
    Bnew = deepcopy(B)
       
    for row in range(height):
        for col in range(width):
            if (height-1 - row) == col:
                Bnew[row][col] = 1
		
    return Bnew
                
def update1c(B):
    #adds a diagonal strip of "on" cells from SE corner
    
    width = len(B[0])
    height = len(B)  
    Bnew = deepcopy(B)
    
    for row in range(height):
        for col in range(width):
            if row == (width-1 - col):
                Bnew[row][col] = 1
		
    return Bnew
                
def update1d(B):
    #adds a diagonal strip of "on" cells from NE corner
    
    width = len(B[0])
    height = len(B)
    Bnew = deepcopy(B)    
    
    for row in range(height):
        for col in range(width):
            if (height - row) == (width - col):
                Bnew[row][col] = 1
		
    return Bnew

def diagnals(B):
    # applies diagnal lines form all corners
    Bnew = deepcopy(B)
    Bnew = update1a(Bnew)
    Bnew = update1b(Bnew)
    Bnew = update1c(Bnew)
    return update1d(Bnew)


def randomBoard(B):
    # returns a board generated randomly of the same size as input
    width = len(B[0])
    height = len(B)
    Bnew = deepcopy(B)   
    
    for row in range(height):
        for col in range(width):
            Bnew[row][col] = random.choice([0,1])
    return Bnew    
		
def randomBoard2(B):
    # returns a board generated randomly of the same size as input
    return [[random.choice([0,1])for col in row] for row in B]

def randomBoard3(B):
    # returns a board generated randomly of the same size as input
    width = len(B[0])
    height = len(B)
    return [[random.choice([0,1])for x in ([0]*width)] for z in [0]*height]


def fill(B):
    # returns a board that is all 1s, same dimentions as B
    width = len(B[0])
    height = len(B)
    return [[1]*width for R in [1]*height ]
                
def blank(B):
    # returns a board that is all 0s, same dimentions as B
    width = len(B[0])
    height = len(B)
    return createBoard(width, height)


def border(B, wide=1, bordervalue=0):
    ''' returns a board that has a border added on top of board B to it 
    of width: wide and of value: bordervalue'''
    
    width = len(B[0])
    height = len(B)
    exception = False
    
    if width < wide: exception = True
    if height < wide: exception = True
    if exception: 
	if bordervalue:
	    return fill(B)
	else:
	    return blank(B)
    
    Bnew = deepcopy(B)    
               
    for row in range(wide) + range(height - wide, height):
        for col in range(width):
            Bnew[row][col] = bordervalue
           
    for col in range(wide) + range(width - wide, width):
        for row in range(height):
            Bnew[row][col] = bordervalue
	    
    return Bnew

def invert(B):
    # returns a board that is the inverse of the input
    width = len(B[0])
    height = len(B)
    Bnew = deepcopy(B)    
       
    for row in range(height):
        for col in range(width):
            if B[row][col]:
                Bnew[row][col] = 0
            else :
                Bnew[row][col] = 1
    return Bnew
		

def update2(B):
    return border(fill(B))

def updateR(B):
    return border(RandomBoard(B))

#print createBoard(3,3)


def life(width, height=None):
    # will become John Conway's Game of Life... 
    
    if height is None: height = width 
    
    B = randomBoard(createBoard(width, height))

    while True:     			# run forever
	csplot.show(B)  		# show current B
	time.sleep(0.25)	   	# pause a bit
	B = randomBoard(B)              # sets the new board correctly
	    
def neighbors(B , row , col , wide = 1):
    '''returns the number of neighbors that are within a radius of wide
    of cell B[row][col]'''
    
    width = len(B[0])
    height = len(B)    
    
    # error catching
    rowL = max(0, row-wide)
    rowU = min(row+wide+1, height)
    
    colL = max(0, col-wide)
    colU = min(col+wide+1, width)
    
    
    sum = -B[row][col]
    for r in range(rowL, rowU):
	for c in range (colL, colU):
	    sum += B[r][c]
    
    return sum
    
def updateNextLife(B):
    
    width = len(B[0])
    height = len(B)
    newB = blank(B)
    
    for row in range(height):
	for col in range(width):    
	    n = neighbors(B , row , col)
	    #if ( n > 3 ) or ( n < 2 ):
		#newB[row][col] = 0
	    if n == 3 : 
		newB[row][col] = 1
	    elif n == 2:
		newB[row][col] = copy(B[row][col])
	    else :
		newB[row][col] = 0
		
    return newB
		
def life2(B):
    
    """ will become John Conway's Game of Life... """
    csplot.showAndClickInIdle(B)
    # hold s and click on the grid to bring a cell to life
    # then close the grid and life will play

    while True:
	csplot.show(B)                   # show B
	time.sleep(0.25)                 # pause a bit
	B = updateNextLife(oldB)         # sets the new board correctly
