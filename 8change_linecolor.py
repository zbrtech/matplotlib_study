import matplotlib.pyplot as plt

x_values = list(range(1,1001))       #1000 points
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,c='red',edgecolor='none',s=40)  #c='red' or c=(0,0,0.8)

plt.axis([0,1100,0,1100000])        #the range of x ,Y

plt.show()
