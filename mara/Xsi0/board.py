class Board:

    def __init__(self):
        self.values = [' ' for i in range(9)]
        self.solutions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                     [0, 3, 6], [1, 4, 7], [2, 5, 8],
                     [0, 4, 8], [2, 4, 6]]
    
    def __str__(self):
        s = '\n\t  {}  |  {}  |  {}'.format(self.values[0], self.values[1], self.values[2])
        s += '\n\t-----|-----|-----'
        s += '\n\t  {}  |  {}  |  {}'.format(self.values[3], self.values[4], self.values[5])
        s += '\n\t-----|-----|-----'
        s += '\n\t  {}  |  {}  |  {}'.format(self.values[6], self.values[7], self.values[8])
        s += '\n\n'
        return s

    def add_move(self,pos,symbol):
        """
        Returns True if the 'symbol' is successfully placed at position 'pos'
        """
        if 0 <= pos < 9:
            if self.values[pos] == ' ':
                self.values[pos] = symbol
                return True
            else:
                print('The position {} is already occupied (by "{}")'.format(pos,self.values[pos]))
                return False
        else:
            print('The position {} is out of range, please enter a nr from 0 to 8.'.format(pos))
            return False

    def win_situation(self,symbol):
        """
        Returns True is the player 'symbol' has won
        """
        for possible_sol in self.solutions:
            if all( self.values[cell] == symbol for cell in possible_sol):
                return True
        return False

    def draw_situation(self):
        """
        Returns True it is a draw
        """
        if not self.win_situation('x') and not self.win_situation('0'):
            if ' ' not in self.values:
                return True
        return False