""" This is a guessing game. Guess the number between 1 and 9 """
from random import uniform
import curses
from os import environ
environ['LINES'] = '10'
environ['COLUMNS'] = '80'

STDSCR = curses.initscr() # Initialize curses screen
STDSCR.keypad(True) # Enable keypad mode to return special keys, such as the cursor keys
curses.noecho() # Turn off automatic echoing of keys to the screen
curses.cbreak() # React to keys instantly, without requiring the Enter key to be pressed

def main():
    """ Main entry point """
    guess_number = None
    secret_number = None

    STDSCR.clear()
    char = ''

    while 1:
        STDSCR.addstr(0, 0, 'Guess a number ... ')
        if guess_number and secret_number:
            STDSCR.addstr(1, 0, 'You guessed %d, the secret number was %d\n' % (guess_number, secret_number))
            if guess_number == secret_number:
                line_num = 2
                with open('win_ascii.txt', 'r') as handle:
                    text = handle.read()
                    for line in text.splitlines():
                        STDSCR.addstr(line_num, 0, line)
                        line_num += 1

        secret_number = int(uniform(1, 9))
        char = STDSCR.getkey()

        STDSCR.clear()

        try:
            guess_number = int(char)
        except ValueError:
            guess_number = None
            continue

if __name__ == '__main__':
    curses.resizeterm(10, 80)
    try:
        main()
    except:
        # Terminate curses application
        curses.nocbreak()
        STDSCR.keypad(False)
        curses.echo()
        curses.endwin()
