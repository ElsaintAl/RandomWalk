import random


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        self.rng = random.Random()

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            x_step = self.get_step()
            y_step = self.get_step()

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        """Provides the direction and distance of the steps."""
        while True:
            # Decide which direction to go and how far to go in that direction.
            direction = self.rng.choice([1, -1])
            distance = self.rng.choice([0, 1, 2, 3, 4])

            # Reject moves that go nowhere.
            if (step := direction * distance) != 0:
                return step
