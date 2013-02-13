import csplot
import time 
import random
from copy import deepcopy	#for copying Boards
from copy import copy		#for copying states

class Board():
    class_attribute = None
    
    def __init__(self, width, height=None):
    #creates a 2d array
        self.width = width
	if height is None:
	    self.height = width
	else:
	    self.height = height
	    
        self.board = [[0]*self.width for x in range(self.height)]

    def update1a(self):
	#adds a diagonal strip of "on" cells from SW corner
	new = deepcopy(self)
	
	for row in range(self.height):
	    for col in range(self.width):
		if row == col:
		    new.board[row][col] = 1
		    
	return new
  
    def update1b(self):
       #adds a diagonal strip of "on" cells from NW corner
	new = deepcopy(self)
	   
	for row in range(self.height):
	    for col in range(self.width):
		if (self.height-1 - row) == col:
		    new.board[row][col] = 1
		    
	return new
		    
    def update1c(self):
	#adds a diagonal strip of "on" cells from SE corner
	new = deepcopy(self)
	
	for row in range(self.height):
	    for col in range(self.width):
		if row == (width-1 - col):
		    new.board[row][col] = 1
		    
	return new
		    
    def update1d(self):
	#adds a diagonal strip of "on" cells from NE corner
	new = deepcopy(self)    
	
	for row in range(self.height):
	    for col in range(self.width):
		if (self.height - row) == (self.width - col):
		    new.board[row][col] = 1
		    
	return new
    
    def diagnals(self):
	# applies diagnal lines from all corners
	new = deepcopy(self)
	new = update1a(new)
	new = update1b(new)
	new = update1c(new)
	return update1d(new)
     
    def random(self):
	# returns a board generated randomly of the same size as self
	new = deepcopy(self)
	new.board = [[random.choice([0,1])for x in ([0]*self.width)] 
	        for z in [0]*self.height]
	return new
    
    
    def fill(self):
	# returns a board that is all 1s, same dimentions as self
	new = deepcopy(self)
	new.board = [[1]*self.width for R in [1]*self.height]
	return new
		    
    def blank(self):
	# returns a board that is all 1s, same dimentions as self
	new = deepcopy(self)
	new.board = [[0]*self.width for R in [1]*self.height]
	return new
    
    
    def border(self, wide=1, bordervalue=0):
	# returns a board that has a border added on top of board B to it 
	# of width: wide and of value: bordervalue

	exception = False
	
	if self.width < wide: exception = True
	if self.height < wide: exception = True
	if exception: 
	    if bordervalue:
		return self.fill()
	    else:
		return self.blank()
	
	new = deepcopy(self)    
		   
	for row in range(wide) + range(self.height - wide, self.height):
	    for col in range(self.width):
		new.board[row][col] = bordervalue
	       
	for col in range(wide) + range(self.width - wide, self.width):
	    for row in range(self.height):
		new.board[row][col] = bordervalue
		
	return new
    
    def invert(self):
	# returns a board that is the inverse of the input
	new = deepcopy(self)    
	   
	for row in range(self.height):
	    for col in range(self.width):
		if self.board[row][col]:
		    new.board[row][col] = 0
		else :
		    new.board[row][col] = 1
	return new
		    
    
    def update2(self):
	return self.fill().boarder()
    
    def updateR(self):
	return self.random().border()
    
    
    def neighbors(self , row , col , wide = 1):
	# returns the number of neighbors that are within a radius of wide
	# of cell self.board[row][col] 
	
	# error catching
	rowL = max(0, row-wide)
	rowU = min(row+wide+1, self.height)
	
	colL = max(0, col-wide)
	colU = min(col+wide+1, self.width)
	
	
	sum = -self.board[row][col]
	for r in range(rowL, rowU):
	    for c in range (colL, colU):
		sum += self.board[r][c]
	
	return sum    



def life(width, height=None):
    # will become John Conway's Game of Life... 
    
    if height is None: height = width 
    
    B = Board(width, height).random()

    while True:     			# run forever
	csplot.show(B.board)  		# show current B
	time.sleep(0.25)	   	# pause a bit
	B = B.random()              # sets the new board correctly
	    

def updateNextLife(B):

    newB = B.blank()
    
    for row in range(B.height):
	for col in range(B.width):    
	    n = B.neighbors(row, col)
	    #if ( n > 3 ) or ( n < 2 ):
		#newB[row][col] = 0
	    if n == 3 : 
		newB.board[row][col] = 1
	    elif n == 2:
		newB.board[row][col] = copy(B.board[row][col])
	    else :
		newB.board[row][col] = 0
		
    return newB
		
def life2(B):
    
    # is John Conway's Game of Life...
    csplot.showAndClickInIdle(B.board)
    # hold s and click on the grid to bring a cell to life
    # then close the grid and life will play

    while True:
	csplot.show(B.board)             # show B
	time.sleep(0.25)                 # pause a bit
	B = updateNextLife(B)            # sets the new board correctly
	
	if B.board == B.blank().board:
	    break
	
    csplot.show(B.board)
    csplot.done()
