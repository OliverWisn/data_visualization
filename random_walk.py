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

    def fill_walk(self):
        """Generate all points for the random walk."""

        # Performing the steps until the expected number of points is 
        # achieved.
        while len(self.x_values) < self.num_points:

            # Determining the direction and the distance to be traveled 
            # in this direction.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Rejection of the movements that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Determining the next values of X and Y.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)