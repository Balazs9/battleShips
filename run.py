from random import randint
from termcolor import colored

scores = {"computer": 0, "player": 0}

class Game:
    def __init__(self, size, number_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.number_ships = number_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))
    
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            slef.board[x] [y] = "*"
            return "Hit"
        else:
            return "Missed"
