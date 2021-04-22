from board import Board
from player import Player

class Game:

    def __init__(self):
        self.board = Board()
        self.player_x = Player('x',self.board)
        self.player_0 = Player('0',self.board)
        self.current_player = self.player_x

    def play(self):
        while True:
            print(self.board)
            self.current_player.make_move()
            if self.check_win():
                break
            else:
                if self.check_draw():
                    break
            self.switch_player()
        print('\033[91m {}\033[00m'.format('Game Over'))


    def check_win(self):
        if self.board.win_situation(self.current_player.symbol):
            print(self.board)
            print('\033[96mPlayer {} has won!\033[00m'.format(self.current_player.symbol))
            return True
        return False

    def check_draw(self):
        if self.board.draw_situation():
            print(self.board)
            print('\033[95mIt is a draw!\033[00m')
            return True
        return False

    def switch_player(self):
        if self.current_player == self.player_0:
            self.current_player = self.player_x
        else:
            self.current_player = self.player_0

    def instructions(self):
        print('The game is played on a 3x3 grid, indexed from 0 to 8.')
        print('The 2 players are either "x" or "0".')
        print('The fist player to get 3 marks in a row (vertical, horizontal or diagonal) wins.')
        print('When the 9 squares are full and nobody won, it is a draw.')