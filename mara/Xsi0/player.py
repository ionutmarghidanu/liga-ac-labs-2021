class Player:

    def __init__(self,symbol,board):
        self.symbol = symbol
        self.board = board

    def __str__(self):
        return 'Player {}'.format(self.symbol)

    def make_move(self):
        while True:
            move = input("Choose the position for {}: \n>".format(self.symbol))
            try:
                move = int(move)
                if self.board.add_move(move, self.symbol):
                    break
            except ValueError:
                print("Please enter a number.")