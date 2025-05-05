"""
File: CollectNewspaperKarel.py
Name: yangziting
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    karel is at home's westnorth ,facing East
    karel is at home's westnorth ,facing East with newspaper(beeper)
    """
    go_to_pick_newspaper()
    go_home()


def turn_right():
    for i in range(3):
        turn_left()


def go_to_pick_newspaper():
    """
    pre-condition: Karel starts at Street 4, Avenue 3 and face East.
    post-condition: Karel returns to Street 4, Avenue 3, face East
                    and put down the newspaper.
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def go_home():
    # go back to the starting point
    turn_left()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    put_beeper()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
