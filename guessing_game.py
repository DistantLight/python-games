""" This is a guessing game. Guess the number between 1 and 9 """

# from os import system
from random import uniform
import curses
SCREEN = curses.initscr()
# from getch import getch

def main():
    """ Main entry point """
    secret_number = int(uniform(1, 9))

    curses.noecho()
    # curses.cbreak()
    SCREEN.keypad(True)

    SCREEN.clear()
    SCREEN.addstr(0, 0, 'Guess a number: ')
    # SCREEN.refresh()

    key_input = SCREEN.getch()
    try:
        if key_input == ord('q'):
            exit()
        guess_number = int(key_input)
    except ValueError:
        return

    SCREEN.addstr(0, 0, 'You guessed %d, the secret number was %d' % (guess_number, secret_number))
    SCREEN.refresh()
    if secret_number == guess_number:
        SCREEN.addstr(0, 0, 'YOU WIN!!!')
        exit()

if __name__ == '__main__':
    while 1:
        main()
