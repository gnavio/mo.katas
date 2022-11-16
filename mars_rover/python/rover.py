class Obstacle():
    
    def __init__(self, obs_x = 0, obs_y = 0):
        self.x = obs_x
        self.y = obs_y

class Rover(object):

    def __init__(self, start_x = 0, start_y = 0, orientation = 'N', obstacles = []):
        self.x = start_x
        self.y = start_y
        self.orientation = orientation
        self.obstacles = obstacles

    def turn_right(self):
        c_points = ['N', 'E', 'S', 'W']
        self.orientation = c_points[c_points.index(self.orientation) + 1] 

    def turn_left(self):
        c_points = ['N', 'E', 'S', 'W']
        self.orientation = c_points[c_points.index(self.orientation) - 1]   
    
    def forward(self):
        if self.orientation == 'N':
            self.y = (self.y + 1) % 3
        elif self.orientation == 'S':
            self.y = (self.y - 1) % 3
        elif self.orientation == 'E':
            self.x = (self.x + 1) % 3
        elif self.orientation == 'W':
            self.x = (self.x - 1) % 3

    def backward(self):
        if self.orientation == 'N':
            self.y = (self.y - 1) % 3
        elif self.orientation == 'S':
            self.y = (self.y + 1) % 3
        elif self.orientation == 'E':
            self.x = (self.x - 1) % 3
        elif self.orientation == 'W':
            self.x = (self.x + 1) % 3
    
    def detect_obstacle(self, next_move):
        obstacles = self.obstacles
        for obs in obstacles:
            match self.orientation:
                case 'N':
                    if (next_move == 'f' and (obs.x == self.x and obs.y == (self.y + 1) % 3) or 
                        next_move == 'b' and (obs.x == self.x and obs.y == (self.y - 1) % 3)):
                        print('Obstacle detected at: x = ' + str(obs.x) + ', y = ' + str(obs.y))
                        return True
                    else:
                        return False
                case 'E':
                    if (next_move == 'f' and (obs.x == (self.x + 1) % 3 and obs.y == self.y) or 
                        next_move == 'b' and (obs.x == (self.x - 1) % 3 and obs.y == self.y)):
                        print('Obstacle detected at: x = ' + str(obs.x) + ', y = ' + str(obs.y))
                        return True
                    else:
                        return False
                case 'S':
                    if (next_move == 'f' and (obs.x == self.x and obs.y == (self.y - 1) % 3) or 
                        next_move == 'b' and (obs.x == self.x and obs.y == (self.y + 1) % 3)):
                        print('Obstacle detected at: x = ' + str(obs.x) + ', y = ' + str(obs.y))
                        return True
                    else:
                        return False
                case 'W':
                    if (next_move == 'f' and (obs.x == (self.x - 1) % 3 and obs.y == self.y) or 
                        next_move == 'b' and (obs.x == (self.x + 1) % 3 and obs.y == self.y)):
                        print('Obstacle detected at: x = ' + str(obs.x) + ', y = ' + str(obs.y))
                        return True
                    else:
                        return False
                    
    def print_position(self):
        print('Rover position: x = ' + str(self.x) + ', y = ' + str(self.y) + ', orientation = ' + self.orientation + '\n')

    def move(self, movs):
        for m in movs:
            match m:
                case 'f':
                    if len(self.obstacles) == 0 or self.detect_obstacle('f') == False:
                        self.forward()
                    else:
                        break
                case 'b':
                    if len(self.obstacles) == 0 or self.detect_obstacle('b') == False:
                        self.backward()
                    else:
                        break
                case 'r':
                    self.turn_right()
                case 'l':
                    self.turn_left()
        self.print_position()

o1 = Obstacle(2, 0)
robot = Rover(0, 0, 'N')
robot.move(['l','f'])
