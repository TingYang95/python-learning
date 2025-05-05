"""
File: PotholeFilling.py
Name: yangziting
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *

def main():
    """
    TODO:
    """
    pass
    for i in range(3):
        go_in()
        put_99()
        go_out()

def put_99():
    for i in range(99):
        put_beeper()

def go_in():
    """
    karel is at the upper left of the pothole facing East
    karel is in the pothole facing South
    """
    move()
    turn_right()
    move()

def go_out():
    """
     karel is in the pothole facing South
     karel is at the upper left of the pothole facing East
    """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()

def turn_right():
    for i in range(3):
        turn_left()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
