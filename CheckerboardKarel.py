"""
File: CheckerboardKarel.py
Name: yangziting
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    This file shows how Karel draws a checkerboard with
    beepers (each beeper spaced 1 avenue apart), regardless
    of the rectangle size
    """
    fill_first_street()
    while front_is_clear():
        fill_even_street()
        fill_odd_street()


def fill_first_street():
    """
    Karel will fill the first street with beepers, and each beeper spaced 1 avenue apart.
    Pre-condition: Karel is at the left side of the first street, facing East
    Post:condition: Karel is at the right side of the first street, facing North
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_left()


def fill_even_street():
    """
    Karel will fill the even street with beepers, and each beeper spaced 1 avenue apart.
    Pre-condition: Karel is at the right side of the previous street, facing North
    Post:condition: Karel is at the left side of the this street, facing North
    """
    if on_beeper():
        if front_is_clear():
            move()
            turn_left()
    else:
        if front_is_clear():
            move()
            turn_left()
            put_beeper()
    # Karel is at the right side of this street, facing West
    while front_is_clear():
        if on_beeper():
            move()
            if front_is_clear():
                move()
                put_beeper()
        else:
            if front_is_clear():
                move()
                put_beeper()
    turn_right()


def fill_odd_street():
    """
    Karel will fill the odd street with beepers(except first street), and each
    beeper spaced 1 avenue apart.
    Pre-condition: Karel is at the left side of the previous street, facing North
    Post:condition: Karel is at the right side of the this street, facing North
    """
    if on_beeper():
        if front_is_clear():
            move()
            turn_right()
    else:
        if front_is_clear():
            move()
            turn_right()
            put_beeper()
    # Karel is at the left side of this street, facing East
    while front_is_clear():
        if on_beeper():
            move()
            if front_is_clear():
                move()
                put_beeper()
        else:
            if front_is_clear():
                move()
                put_beeper()
    turn_left()


def turn_right():
    """
    Karel will turn left for 3 times
    """
    for i in range(3):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
