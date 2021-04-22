import game
import os

try:
    os.system('cls')
    tic_tac_toe = game.Game()
    result = 0
    while True:
        while result != 2:
            os.system('cls')
            tic_tac_toe.print_board()

            while True:
                try:
                    cell = int(input('Choose a cell (from 1 to 9): ')) - 1
                    if cell < 0 or cell > 8:
                        raise ValueError()
                except ValueError:
                    print("\nYou have to enter an integer value between 1 and 9!")
                else:
                    result = tic_tac_toe.play_turn(cell)
                    if result == 1:
                        print('\nThis cell is already taken!')
                    else:
                        break

        print('{}\'S SCORE: {} pts'.format(tic_tac_toe.players['x'].name, tic_tac_toe.players['x'].score))
        print('{}\'S SCORE: {} pts'.format(tic_tac_toe.players['o'].name, tic_tac_toe.players['o'].score))

        if input('\n\nPress \'y\' to start new game: ') == 'y':
            result = 0
            tic_tac_toe.new_match()
        else:
            break
except KeyboardInterrupt:
    os.system('cls')
    print(f'You left the game :(\n')
