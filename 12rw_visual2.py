import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()   #rw is a instance(means case) of this class
rw.num_points=10000
rw.fill_walk()

plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show()
