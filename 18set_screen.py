import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:   
    rw = RandomWalk(10000)   #rw is a instance(means case) of this class
                             #equal rw=RandomWalk() then rw.num_points=50000
    rw.fill_walk()

    plt.figure(figsize=(10,6))   #set this

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=1)

    plt.scatter(0,0,c='green',edgecolors='none',s=10)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=10)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input('make another wakl?(y/n):')
    if keep_running == 'n':
        break
