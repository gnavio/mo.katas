import unittest

from rover import Rover

"""
Mars rover moves through


                       N
        --------------------------------
        |   0,2   |   1,2   |   2,2    |
        -------------------------------- 
    W   |   0,1   |   1,1   |   2,1    |    E
        -------------------------------- 
        |   0,0   |   1,0   |   2,0    |
        --------------------------------
                       S
                   
"""


class MarsRoverTestCase(unittest.TestCase):
    
    # Movement

    def test_rover_move_forward_N(self):
        rover = Rover(start_x = 1, start_y = 1, orientation = 'N')
        movements = ['f']
        expected_position = (1, 2)
        rover.move(movements)
        self.assert_rover_position(expected_position, rover)

    def test_rover_move_backward_N(self):
        rover = Rover(start_x = 1, start_y = 1, orientation = 'N')
        movements = ['b']
        expected_position = (1, 0)
        rover.move(movements)
        self.assert_rover_position(expected_position, rover)

    def test_rover_move_forward_E(self):
        rover = Rover(start_x = 1, start_y = 1, orientation = 'E')
        movements = ['f']
        expected_position = (2, 1)
        rover.move(movements)
        self.assert_rover_position(expected_position, rover)

    def test_rover_move_backward_E(self):
        rover = Rover(start_x = 1, start_y = 1, orientation = 'E')
        movements = ['b']
        expected_position = (0, 1)
        rover.move(movements)
        self.assert_rover_position(expected_position, rover)

    def test_rover_move_forward_S(self):
        rover = Rover(start_x = 1, start_y = 1, orientation = 'S')
        movements = ['f']
        expected_position = (1, 0)
        rover.move(movements)
        self.assert_rover_position(expected_position, rover)

    def test_rover_move_backward_S(self):
        rover = Rover(start_x = 1, start_y = 1, orientation = 'S')
        movements = ['b']
        expected_position = (1, 2)
        rover.move(movements)
        self.assert_rover_position(expected_position, rover)

    def test_rover_move_forward_W(self):
        rover = Rover(start_x = 1, start_y = 1, orientation = 'W')
        movements = ['f']
        expected_position = (0, 1)
        rover.move(movements)
        self.assert_rover_position(expected_position, rover)

    def test_rover_move_backward_W(self):
        rover = Rover(start_x = 1, start_y = 1, orientation = 'W')
        movements = ['b']
        expected_position = (2, 1)
        rover.move(movements)
        self.assert_rover_position(expected_position, rover)


    # Turn

    def test_rover_turn_right(self):
        rover = Rover(start_x = 1, start_y = 1, orientation = 'N')
        movements = ['r', 'r', 'r']
        expected_orientation = 'W'
        rover.move(movements)
        self.assert_rover_orientation(expected_orientation, rover)

    def test_rover_turn_left(self):
        rover = Rover(start_x = 1, start_y = 1, orientation = 'N')
        movements = ['l', 'l', 'l']
        expected_orientation = 'E'
        rover.move(movements)
        self.assert_rover_orientation(expected_orientation, rover)

    
    # Wrapping

    def test_rover_wrapping_N(self):
        rover = Rover(start_x = 1, start_y = 1, orientation = 'N')
        movements = ['f', 'f', 'f', 'b', 'b','b']
        expected_position = (1, 1)
        rover.move(movements)
        self.assert_rover_position(expected_position, rover)

    def test_rover_wrapping_S(self):
        rover = Rover(start_x = 1, start_y = 1, orientation = 'S')
        movements = ['b', 'b','b', 'f', 'f', 'f']
        expected_position = (1, 1)
        rover.move(movements)
        self.assert_rover_position(expected_position, rover)
    
    def test_rover_wrapping_E(self):
        rover = Rover(start_x = 1, start_y = 1, orientation = 'E')
        movements = ['f', 'f', 'f', 'b', 'b','b']
        expected_position = (1, 1)
        rover.move(movements)
        self.assert_rover_position(expected_position, rover)
    
    def test_rover_wrapping_W(self):
        rover = Rover(start_x = 1, start_y = 1, orientation = 'W')
        movements = ['b', 'b','b', 'f', 'f', 'f']
        expected_position = (1, 1)
        rover.move(movements)
        self.assert_rover_position(expected_position, rover)


    # Asserts

    def assert_rover_position(self, expected_position, rover):
        self.assertEqual(expected_position[0], rover.x)
        self.assertEqual(expected_position[1], rover.y)

    def assert_rover_orientation(self, expected_orientation, rover):
        self.assertEqual(expected_orientation, rover.orientation)
