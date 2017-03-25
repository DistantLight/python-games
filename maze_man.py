""" Move a man through a maze """
import curses

STDSCR = curses.initscr() # Initialize curses screen
STDSCR.keypad(True) # Enable keypad mode to return special keys, such as the cursor keys
curses.noecho() # Turn off automatic echoing of keys to the screen
curses.cbreak() # React to keys instantly, without requiring the Enter key to be pressed

def main():
    """ Main entry point """
    STDSCR.clear()
    char = ''
    while 1:
        STDSCR.addstr(char)
        char = STDSCR.getkey()
        STDSCR.clear()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # Terminate curses application
        curses.nocbreak()
        STDSCR.keypad(False)
        curses.echo()
        curses.endwin()
