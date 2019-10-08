#!/user/bin/env pyhton3
import sys


class initialize:
    def __init__(self, m1, m2, distance, gravitational_force):
        self.m1 = 0.0
        self.m2 = 0.0
        self.distance = 0.0
        self.gravitational_force = 0.0
        if len(sys.argv) < 5:
            exit()
        else:
            # todo:
            # type check args
            # if they contain an E or 10^x then it is scientific notation
            # else parse to float



            self.m1 = m1
            self.m2 = m2
            self.distance = distance
            self.gravitational_force = gravitational_force


if __name__ == 'main':
    initialize()
