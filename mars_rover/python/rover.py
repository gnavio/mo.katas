class Rover(object):

    def __init__(self, start_x = 0, start_y = 0, orientation = 'N'):
        self.x = start_x
        self.y = start_y
        self.orientation = orientation

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
        match next_move:
                case 'f':
                    self.forward()
                case 'b':
                    self.backward()
                case 'r':
                    self.turn_right()
                case 'l':
                    self.turn_left()
    
    def print_position(self):
        print('Rover position: x = ' + str(self.x) + ', y = ' + str(self.y) + ', orientation = ' + self.orientation + '\n')

    def move(self, movs):
        for m in movs:
            match m:
                case 'f':
                    self.forward()
                case 'b':
                    self.backward()
                case 'r':
                    self.turn_right()
                case 'l':
                    self.turn_left()
        self.print_position()


robot = Rover()
robot.move(['r','r','f','f'])
