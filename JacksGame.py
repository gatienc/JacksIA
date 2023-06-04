import random
import Config
import numpy as np
from termcolor import colored
from tabulate import tabulate

# Toss the dice
def TossDice():
    # Generate a random number between 1 and 6
    dice = random.randint(1,6)
    return dice

class Player_board:
    def __init__(self, board=np.zeros((Config.LINES_SIZE,Config.LINES_NUMBER),dtype=int)):
        # Initialize the board
        # The board is a list of lists, each list corresponds to a row in the board
        # The board is initialized with blank squares
        # The board is initialized with a player in the first square
        self.board = board
        
    # Add a dice to the board
    def addDice(self, dice:int, position:int,opponent)->np.matrix:
        # Set the board position to the dice value
        if position > Config.LINES_SIZE:
            print("Position out of range")
            return self.board
        #set the dice always on the bottom if possible
        placed=False
        index=0
        while placed==False and index<Config.LINES_SIZE:
            if self.board[index][position] == 0:
                self.board[index][position] = dice
                placed=True
            else:
                index+=1
        if placed:
            return self.board
        else:
            print("No more space in this column")
            
    
    
    
    def PointForColumn(self, column_number):
        valDict=dict()
        column=self.board[:,column_number]
        for element in column: 
            if element==0:
                continue
            if element not in valDict:
                valDict[element]=1
            else: 
                valDict[element]+=1

        #calculation of csore
        score=0
        for key in valDict:
            score+=key*(valDict[key]**2)
        return score
            
    # Print the board
    def PrintBoard(self):
        print(colored(tabulate(self.board), 'blue'))



Player_board = Player_board()
Player_board.addDice(dice=1, position=0,opponent=None)
Player_board.addDice(dice=2, position=0,opponent=None)
Player_board.addDice(dice=TossDice(), position=2,opponent=None)


Player_board.PrintBoard()  
