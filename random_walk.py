# random_walk.py
# -*- coding: utf-8 -*-

from random import choice

class RandomWalk():
    """The class intended to generate a random walk."""

    def __init__(self, num_points=5000):
        """Initialization of the random walk attributes."""
        self.num_points = num_points

        # The starting point has the coordinates (0, 0).
        self.x_values = [0]
        self.y_values = [0]