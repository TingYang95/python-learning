"""
File: quadratic_solver.py
Name:yangziting
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
    """
    TODO:To calculate the value of x.
    """
    a =float(input('a:'))
    b =float(input('b:'))
    c =float(input('c:'))
    d = b*b-4*a*c   #  discriminant 判別式

    if d >0:
       r1 = (((-b) + math.sqrt(b * b -4* a * c)) /2* a)
       r2 = (((-b) - math.sqrt(b * b -4* a * c)) /2* a)
       print('Two roots: '+str(r1) +','+str(r2))
    elif d == 0:
       r1 = (((-b) + math.sqrt(b * b -4* a * c)) /2* a)
       print('One root: '+str(r1))
    elif d <= 0:
       print('No real roots')

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
