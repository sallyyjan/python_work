import matplotlib.pyplot as plt

from random_walk import RandomWalk

class RandomWalkVisualize:
    """Visualize a random walk using different plot"""
    
    def __init__(self, num_points):
        """Intialize attributes of a walk."""
        self.num_points = num_points
    
    def visualize_scatter(self):
        """Visualize random walk using scatter plot"""

        # Keep making new walks, as long as program is active.
        while True:
            # Make a random walk
            rw = RandomWalk(num_points=self.num_points)
            rw.fill_walk()

            # Plot the points in the walk
            plt.style.use('classic')
            fig, ax = plt.subplots()
            point_numbers = range(rw.num_points)
            ax.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, 
                cmap=plt.cm.Blues, edgecolors='none')
            
            # Emphasize the first and end points.
            ax.scatter(0, 0, c='green', edgecolors='none', s=100)
            ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', 
                s=100)

            # Remove axis.
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)

            plt.show()

            keep_running = input("Make another walk as scatter? (y/n): ")
            if keep_running == 'n':
                break
    
    def visualize_line(self):
        """Visualize random walk using a line plot."""

        # Keep making new walks, as long as program is active.
        while True:
            # Make a random walk
            rw = RandomWalk(num_points=self.num_points)
            rw.fill_walk()

            # Plot the points in the walk
            plt.style.use('classic')
            fig, ax = plt.subplots()
            point_numbers = range(rw.num_points)
            ax.plot(rw.x_values, rw.y_values, linewidth=1, c='blue')

            # Remove axis.
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)

            plt.show()

            keep_running = input("Make another walk as line? (y/n): ")
            if keep_running == 'n':
                break


# visualize random walk
rwv = RandomWalkVisualize(5000)
rwv.visualize_line()
rwv.visualize_scatter()