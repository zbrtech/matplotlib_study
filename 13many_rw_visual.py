import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()   #rw is a instance(means case) of this class
    rw.fill_walk()

    plt.scatter(rw.x_values,rw.y_values,s=15)
    plt.show()

    keep_running = input('make another wakl?(y/n):')
    if keep_running == 'n':
        break
