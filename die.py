# die.py
# -*- coding: utf-8 -*-

from random import randint

class Die():
    """Class representing the single game die."""

    def __init__(self, num_sides=6):
        """Assuming that the dice is in the form of the cube."""
        self.num_sides = num_sides

    def roll(self):
        """
        Return of a value from 1 to the number of faces the dice has.
        """
        return.randint(1, self.num_sides)