""" Move a man through a maze """
import curses

STDSCR = curses.initscr() # Initialize curses screen
STDSCR.keypad(True) # Enable keypad mode to return special keys, such as the cursor keys
curses.noecho() # Turn off automatic echoing of keys to the screen
curses.cbreak() # React to keys instantly, without requiring the Enter key to be pressed

X_CORD = 0
Y_CORD = 0

CHARACTER = '+'

def move(direction):
    """ Update X/Y coordinates to move the character """
    global X_CORD
    global Y_CORD

    if direction == 'KEY_LEFT':
        X_CORD -= 1
    elif direction == 'KEY_RIGHT':
        X_CORD += 1
    elif direction == 'KEY_UP':
        Y_CORD -= 1
    elif direction == 'KEY_DOWN':
        Y_CORD += 1


def main():
    """ Main entry point """
    STDSCR.clear()
    char = ''
    while 1:
        STDSCR.addstr(Y_CORD, X_CORD, CHARACTER)
        char = STDSCR.getkey()
        move(char)
        STDSCR.clear()

if __name__ == '__main__':
    try:
        main()
    except:
        # Terminate curses application
        curses.nocbreak()
        STDSCR.keypad(False)
        curses.echo()
        curses.endwin()
