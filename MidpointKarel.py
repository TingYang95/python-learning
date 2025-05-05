"""
File: MidpointKarel.py
Name: yangziting
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
        """
        Karel will put a beeper on the corner closest to the center of 1st Street.
        Pre-condition: Karel is at (1,1), facing East.
        Post-condition: Karel is on the corner closest to the center of 1st Street, and a beeper is put at the same place.
        """
        find_the_wall()
        while on_beeper():
            find_midpoint()
        put_beeper()  # A beeper is put on the corner closest to the center of 1st Street.

def find_the_wall():
        """
        Pre-condition: Karel is at (1,1), facing East.
        Post-condition: Karel is at the Southeast corner of the world, which is at the last avenue of 1st street, facing East.
                        There is a beeper put at (1,1), and a beeper put at the the last avenue of 1st street.
        """
        put_beeper()
        while front_is_clear():
            move()
        if not on_beeper():
            put_beeper()

def find_midpoint():
    """
    Pre-condition: Karel is at the Southeast corner of the world, which is at the last avenue of 1st street, facing East.
    Post-condition: Karel is on the corner closest to the center of 1st Street.
    """
    pick_beeper()
    turn_around()
    if not front_is_clear():
        return
    move()
    if not on_beeper():
        put_beeper()
        move()
        while not on_beeper():
            move()
            # Karel is moving the beepers to reach the corner closest to the center of 1st Street.
    else:
        pick_beeper()
        # karel picks all the beepers before puts the last one on the corner closest to the center of 1st Street.


def turn_around():
        turn_left()
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
