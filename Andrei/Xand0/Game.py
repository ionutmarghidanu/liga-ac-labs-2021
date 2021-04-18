from Player import Player
import random


class Game:

    def __init__(self, player1_name, player2_name):

        self.player1 = Player(player1_name, ' ')
        self.player2 = Player(player2_name, ' ')
        self.moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.current_player = None
        self.points = [0, 0]
        self.initial_player_info()
        self.play()

    def initial_player_info(self):
        temp = random.randint(0, 1)
        if temp == 0:
            self.player1.char = '0'
            self.player2.char = 'X'
            self.current_player = self.player2
        else:
            self.player1.char = 'X'
            self.player2.char = '0'
            self.current_player = self.player1

    def print_board(self):
        print(" _ _ _ _ _ _ ")
        print("| {} | {} | {} |".format(self.moves[0], self.moves[1], self.moves[2]))
        print(" -----------")
        print("| {} | {} | {} |".format(self.moves[3], self.moves[4], self.moves[5]))
        print(" -----------")
        print("| {} | {} | {} |".format(self.moves[6], self.moves[7], self.moves[8]))
        print(" -----------")

    def print_points(self):
        print(self.player1.name, "has ", self.points[0], " points")
        print(self.player2.name, "has ", self.points[1], " points\n")

    def checkLines(self):
        if (((self.moves[0] == self.moves[1]) and (self.moves[1] == self.moves[2])) or
                ((self.moves[3] == self.moves[4]) and (self.moves[4] == self.moves[5])) or
                ((self.moves[6] == self.moves[7]) and (self.moves[7] == self.moves[8]))):
            return 1
        return 0

    def checkCols(self):
        if (((self.moves[0] == self.moves[3]) and (self.moves[3] == self.moves[6])) or
                ((self.moves[1] == self.moves[4]) and (self.moves[4] == self.moves[7])) or
                ((self.moves[2] == self.moves[5]) and (self.moves[5] == self.moves[8]))):
            return 1
        return 0

    def checkDiags(self):
        if (((self.moves[0] == self.moves[4]) and (self.moves[4] == self.moves[8])) or
                ((self.moves[2] == self.moves[4]) and (self.moves[4] == self.moves[6]))):
            return 1
        return 0

    def checkWin(self):
        if self.checkLines() or self.checkCols() or self.checkDiags():
            return 1
        return 0

    def checkDraw(self):
        draw = 0
        for i in range(9):
            if self.moves[i] == 'X' or self.moves[i] == '0':
                draw = 1
            else:
                draw = 0
                break
        return draw

    def match(self, current_player):
        self.moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while True:
            self.print_board()
            try:
                print(current_player.name, " turn : ", end="")
                move = int(input())
            except ValueError:
                print("You need to enter a number between 1 and 9!\n")
                continue

            if move < 1 or move > 9:
                print("You need to enter a number between 1 and 9!\n")
                continue

            if self.moves[move - 1] == 'X' or self.moves[move - 1] == '0':
                print("This position is already taken!")
                continue

            self.moves[move - 1] = current_player.char

            if self.checkWin():
                self.print_board()
                print(current_player.name, " won!")
                return current_player

            if self.checkDraw():
                self.print_board()
                print("Draw!")
                return "Draw"

            if current_player == self.player1:
                current_player = self.player2
            else:
                current_player = self.player1

    def play(self):
        while 1:
            print("Enter 1 for a new game")
            print("Enter 0 to Exit")
            try:
                choice = int(input("Your option: "))
            except ValueError:
                print("You need to enter 0 or 1!\n")
                continue
            if choice == 0:
                print("Final Score")
                self.print_points()
                break
            elif choice == 1:
                winner = self.match(self.current_player)
                if winner == self.player1:
                    self.points[0] += 1
                elif winner == self.player2:
                    self.points[1] += 1
                print("Score:")
                self.print_points()
            else:
                print("You need to enter 0 or 1!\n")
                continue
            if self.current_player == self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1

            if self.player1.char == 'X':
                self.player1.char = '0'
            else:
                self.player1.char = 'X'

            if self.player2.char == 'X':
                self.player2.char = '0'
            else:
                self.player2.char = 'X'
