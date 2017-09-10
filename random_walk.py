from random import choice   #this is file 11

class RandomWalk():       #one class to randomly and autoly create walk steps
                          #this class contain 2 funtions and 3 properties

    def __init__(self,num_points=5000):   #1 of 2 functions of this class. to send steps arguments to this class itself. and declare 3 properties 
        self.num_points = num_points       #self.number_points is 1 of 3 properties of this class. this shuxing use the sent argument
        self.x_values = [0]                #self.x_values is 1 of 3 properties of this class. it is a list to store up x direction steps
        self.y_values = [0]                #just like x

    def fill_walk(self):                   #1 of 2 functions of this class.to randomly and autoly create walk steps
        while len(self.x_values) < self.num_points:   #just use 2 properties
            x_direction = choice([1,-1])              #decide x go to left or right
            x_distance = choice([0,1,2,3,4])          #decide distance of one step
            x_step = x_direction * x_distance         #combine direction and distance to create the x_step property

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue                              #refuse x,y all is 0, because it means do not move

            next_x = self.x_values[-1] + x_step       #joint the self.x_values property(-1 means the last one of the list) and the x_step to create next_x who will append to be the last self.x_values
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
