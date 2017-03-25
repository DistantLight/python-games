""" This is a guessing game. Guess the number between 1 and 9 """
from random import uniform
import curses

STDSCR = curses.initscr() # Initialize curses screen
STDSCR.keypad(True) # Enable keypad mode to return special keys, such as the cursor keys
curses.noecho() # Turn off automatic echoing of keys to the screen
curses.cbreak() # React to keys instantly, without requiring the Enter key to be pressed

def main():
    """ Main entry point """


    STDSCR.clear()

    STDSCR.addstr('Guess a number: ')
    char = ''
    while 1:
        STDSCR.addstr(0, 0, 'Guess a number ... ')
        try:
            STDSCR.addstr(1, 0, 'You guessed %d, the secret number was %d\n' % (guess_number, secret_number))
        except:
            pass
        secret_number = int(uniform(1, 9))
        char = STDSCR.getkey()
        STDSCR.clear()
        try:
            guess_number = int(char)
        except ValueError:
            continue


    # SCREEN.refresh()
    # if secret_number == guess_number:
    #     SCREEN.addstr(0, 0, 'YOU WIN!!!')
    #     exit()

if __name__ == '__main__':
    try:
        main()
    except:
        # Terminate curses application
        curses.nocbreak()
        STDSCR.keypad(False)
        curses.echo()
        curses.endwin()
