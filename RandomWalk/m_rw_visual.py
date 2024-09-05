import matplotlib.pyplot as plt

from m_random_walk import RandomWalk

while True:
    # Make a random walk.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    plt.plot(rw.x_values, rw.y_values, linestyle='-.', linewidth=0.5)

    # Emphasize the first and last points.
    ax.plot(0, 0, '.', c='green', markersize=10)
    ax.plot(rw.x_values[-1], rw.y_values[-1], '.', c='red', markersize=10)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running.lower() == 'n':
        break
