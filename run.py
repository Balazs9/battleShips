import random
from random import randint
from termcolor import colored

scores = {"computer": 0, "player": 0}

x = random.randint(0, 9)
y = random.randint(0, 9)


class Game:

    """
    Main game, sets board size, number of ships,
    the players name, and the board
    """

    def __init__(self, size, number_ships, player_name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.number_ships = number_ships
        self.player_name = player_name
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
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Missed"
  
    def point(self, size):
        """
        Return a random integer in a range of 0 and size
        """

        return randint(0, size-1)

    def guess_validate(self, x, y):
        """
        player guess the row and column and
        validator checks if it is an integer
        if not ValueError
        """

        try:
            for value in values:
                value = int(value)

                if (value < 0 and value > 9):
                    raise ValueError(
                        "Sorry must be between 0 and 9, please try again")
        except ValueError as e:
            print(f"Sorry: {e}, is not a number, try again please!")
            return False

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.number_ships:
            print("")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "O"


def new_game(): 
    """
    Start the new game, sets ships numbers, board size, restart the scoretbale
    """

    size = 9
    number_ships = 5
    scores["computer"] = 0
    scores["player"] = 0
    print(colored("         *", "yellow"))
    print(colored("     ******   ", "yellow"))
    print(colored("     *    *   ", "yellow"))
    print(colored("*    *    *  *", "yellow"))
    print(colored(" ************", "yellow"))
    print(colored("  **********", "yellow"))
    print(colored("*" * 35, "red"))
    print(colored("Game rules: ", "yellow"))
    print(colored("Two players game, human against the computer.", "yellow"))
    print(colored("Each player guess their number.", "yellow"))
    print(colored("Then the bets will be visible on the boards.", "yellow"))
    print(colored("Each player has 5 chance to bet", "yellow"))
    print(colored("***********************************", "red"))
    print(colored("Good luck and have fun!", "red"))
    print(colored("***********************************", "red"))
    player_name = input("Please enter your name: ")
    print(f"Hello {player_name} , enjoy the game!")
    game = Game(size, number_ships, player_name, type)
    game.print()
    game.guess(x, y)
    game.add_ship(x, y)
    game.point(size)


new_game()
