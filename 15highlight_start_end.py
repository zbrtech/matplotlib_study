import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()   #rw is a instance(means case) of this class
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=15)

    plt.scatter(0,0,c='green',edgecolors='none',s=16)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=16)

    plt.show()

    keep_running = input('make another wakl?(y/n):')
    if keep_running == 'n':
        break
