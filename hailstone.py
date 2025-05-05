"""
File: hailstone.py
name:yangziting
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    When the user enters a positive integer, this file can compute Hailstone sequence
    """
    print('This program computes Hailstone sequences')
    n = int(input('Enter a number: '))
    # "step" is used to calculate how many steps the program must take to reach 1
    step = 0
    # The number must be a positive integer to prevent the program from entering an infinite loop
    if n < 0:
        print('The number must be a positive integer!')
    else:
        while n != 1:
            if n % 2 == 0:
                print(int(n), 'is even, so I take half:', int(hailstone(n)))
                n = hailstone(n)
                step = step + 1
            else:
                print(int(n), 'is odd, so I make 3n+1:', int(hailstone(n)))
                n = hailstone(n)
                step = step + 1
        print('It took ' + str(step) + ' steps to reach 1.')


def hailstone(n):
    """
    The hailstone(n) can return the value, depending on "n" is odd or even
    """
    if n % 2 == 0:
        n = n / 2
        return n
    else:
        n = (3 * n) + 1
        return n


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
