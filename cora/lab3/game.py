import player


def current_message(player_turn):
    return '{}\'S TURN'.format(player_turn.name.upper())


class Game:
    def __init__(self):
        player1_name = input('Type first player\'s name: ')
        player2_name = input('Type second player\'s name: ')

        self.players = {
            'x': player.Player(player1_name),
            'o': player.Player(player2_name)
        }

        self.reset_game(self.players['x'])

    def reset_game(self, starting_player):
        self.board = [' '] * 9
        self.result = -1
        self.winner_line = None
        self.starting_player = starting_player
        self.player_turn = starting_player
        self.message = current_message(starting_player)

    #  0 => x-player wins
    #  1 => o-player wins
    # -1 => not a winning line
    def check(self, i, j, k):
        if self.board[i] != ' ' and self.board[i] == self.board[j] == self.board[k]:
            self.winner_line = [i, j, k]

            if self.board[i] == 'x':
                return 0
            else:
                return 1

        return -1

    # -1 => game not finished
    #  0 => x-player wins
    #  1 => o-player wins
    #  2 => game finished with tie
    def which_game_state(self):
        # verify rows
        for i in [0, 3, 6]:
            self.result = self.check(i, i + 1, i + 2)
            if self.result != -1:
                return

        # verify columns
        for i in [0, 1, 2]:
            self.result = self.check(i, i + 3, i + 6)
            if self.result != -1:
                return

        # verify first diagonal
        self.result = self.check(0, 4, 8)
        if self.result != -1:
            return

        # verify second diagonal
        self.result = self.check(2, 4, 6)
        if self.result != -1:
            return

        # verify if there is any empty tile
        for i in range(9):
            if self.board[i] == ' ':
                self.result = -1
                return

        self.result = 2

    def play_turn(self, i):
        if self.board[i] != ' ':
            return 1

        self.board[i] = 'x' if self.player_turn == self.players['x'] else 'o'
        self.player_turn = self.players['o'] if self.player_turn == self.players['x'] else self.players['x']
        self.message = current_message(self.player_turn)
        self.which_game_state()

        if self.result == 0 or self.result == 1:
            p = self.players['x'] if self.result == 0 else self.players['o']
            print('\n{} WINS!'.format(p.name))
            p.award_points(1.0)
            return 2

        elif self.result == 2:
            print('\nIT\'S A TIE!')
            self.players['x'].award_points(0.5)
            self.players['o'].award_points(0.5)
            return 2

        return 0

    def print_board(self):
        print('\n {} | {} | {}'.format(self.board[0], self.board[1], self.board[2]))
        print('---+---+---')
        print(' {} | {} | {}'.format(self.board[3], self.board[4], self.board[5]))
        print('---+---+---')
        print(' {} | {} | {}'.format(self.board[6], self.board[7], self.board[8]))
        print('\n\n{}'.format(self.message))

    # alternate who starts the game
    # if last game was not finished, the same player starts
    def new_match(self):
        if self.result == -1:
            self.reset_game(self.starting_player)
        else:
            self.reset_game(self.players['o'] if self.starting_player == self.players['x'] else self.players['x'])
