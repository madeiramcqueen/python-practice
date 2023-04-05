#  A random walk is a path that has no direction but is determined by a series of decisions

from random import choice 

# Create a random class to generate random walks
class RandomWalk:
    def __init__(self, num_points=500):
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]