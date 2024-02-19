#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Lets play a game of "Guess my number".

I will be thinking af a number between 1 and 100.
You shall try to guess the number.

I will let you know if your guess is lower or higher than
the number that I am thinking of.

You have 5 guesses. Then you loose.

"""

#import shell
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PigDiceGame import game


def main():
    """Execute the main program."""
    #print(__doc__)
    #shell.Shell().cmdloop()
    game.Game().startGame()


if __name__ == "__main__":
    main()
