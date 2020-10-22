#!/usr/bin/env python3

# Question
# A robot moves in a plane starting from the original point (0,0). The robot can move UP, DOWN, LEFT
# and RIGHT with a given steps. # Write a program to compute the distance from current position after
# a sequence of movement and original point. Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2 (rounded up)


class Robot:

    total_distance_traveled = 0
    starting_x_coordinate = 0
    starting_y_coordinate = 0


    def __init__(self, starting_x=0, starting_y=0):
        self.x = starting_x
        self.y = starting_y
        Robot.starting_x_coordinate = starting_x
        Robot.starting_y_coordinate = starting_y


    def __repr__(self):
        return f'Robot({Robot.starting_x_coordinate},{Robot.starting_y_coordinate})'


    def __str__(self):

        message = f'''\nCurrent coordinates: ({self.x}, {self.y}).
Total distance traveled: {Robot.total_distance_traveled}
The distance from the starting point: {self.calculate_distance()}'''

        # example message
        '''
        Current coordinates: (-3, 2).
        Total distance traveled: 11
        The distance from the starting point: 3.61
        '''

        return message


    def calculate_distance(self):
        return round(((self.x - Robot.starting_x_coordinate)**2 + (self.y - Robot.starting_y_coordinate)**2)**(1/2), 2)


    def up(self, distance):
        self.y += distance
        Robot.total_distance_traveled += distance
 

    def down(self, distance):
        self.y -= distance
        Robot.total_distance_traveled += distance


    def left(self, distance):
        self.x -= distance
        Robot.total_distance_traveled += distance
 

    def right(self, distance):
        self.x += distance
        Robot.total_distance_traveled += distance


if __name__ == '__main__':

    robot_1 = Robot()

    print(repr(robot_1))
    print(robot_1)

    # UP 5
    robot_1.up(5)
    print(robot_1)

    # DOWN 3
    robot_1.down(3)
    print(robot_1)

    # LEFT 3
    robot_1.left(3)
    print(robot_1)

    # RIGHT 2
    robot_1.right(2)
    print(robot_1)

