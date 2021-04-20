class GameState:
    _board_mapping = 'OX.'

    def __init__(self):
        self.board = [[-1, -1, -1],
                      [-1, -1, -1],
                      [-1, -1, -1]]
        self.available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == -1]
        self.next_player = 1

    def no_moves_left(self):
        if not self.available_moves:
            return True

    def is_won(self):
        for i in range(3):
            # Horizontal
            if self.board[i][0] != -1 and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True

                # Vertical
            if self.board[0][i] != -1 and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True

                # Diagonals
            if self.board[0][0] != -1 and self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return True

            if self.board[2][0] != -1 and self.board[2][0] == self.board[1][1] == self.board[0][2]:
                return True

        return False

    def is_over(self):
        return self.no_moves_left() or self.is_won()

    def proceed_with_move(self, chosen_move):
        move = self.available_moves.pop(chosen_move)
        self.board[move[0]][move[1]] = self.next_player
        self.next_player = (self.next_player + 1) % 2

    def print_board(self):
        print("\nCurrent board state:")
        print("*****")
        for i in range(3):
            m = [self._board_mapping[self.board[i][j]] for j in range(3)]
            print(f'*{m[0]}{m[1]}{m[2]}*')

        print("*****\n")

    def next_player_mapping(self):
        return self._board_mapping[self.next_player]

    def print_available_moves(self):
        print('Please choose one of the following moves:')
        for i, v in enumerate(self.available_moves):
            print(f'Move {i}: ' + str(v))


class Game:
    def __init__(self):
        self.state = GameState()

    def play(self):
        while not self.state.is_over():
            self.state.print_board()

            self.state.print_available_moves()

            user_input = self.__wait_input()
            while not self.__valid_input(user_input):
                print('Invalid move!\n')
                self.state.print_available_moves()
                user_input = self.__wait_input()

            self.state.proceed_with_move(int(user_input))

        self.state.print_board()
        self.__print_results()

    def __wait_input(self):
        return input(f"'{self.state.next_player_mapping()}' to move: ")

    def __valid_input(self, user_input):
        return user_input.isnumeric() and 0 <= int(user_input) < len(self.state.available_moves)

    def __print_results(self):
        print("\nGame finished!")

        if self.state.is_won():
            if self.state.next_player == 1:
                print("'O' wins!")
            else:
                print("'X' wins!")
        else:
            print("It's a draw!")


def main():
    Game().play()


if __name__ == "__main__":
    main()
