from board import Board
from player import Player
from game import Game

if __name__=="__main__":
    while True:
        print('Do you want to start a new game?[y/n]')
        response = input('>')
        if response == 'y':
            game = Game()
            game.instructions()
            game.play()
            del game
        if response =='n':
            break