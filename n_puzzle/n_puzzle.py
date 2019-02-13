from problem import NPuzzle
from math import *


class NPuzzleMiss(NPuzzle):
    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles """
        return sum(s != g for (s, g) in zip(node.state, self.goal))


class NPuzzleMht(NPuzzle):
    def h(self, node):
        """ implement Manhattan distance. Hint! Look at
        Missplaced Tiles heuristic function above """
        return sum(abs(e - s) for (s, e) in zip(node.state, self.goal))


class NPuzzleEuc(NPuzzle):
    """ implement Euclidean distance. """
    def h(self, node):
        return sqrt(sum(pow((x - s), 2) for (s, x) in zip(node.state, self.goal)))

class NPuzzleRC(NPuzzle):
    def h(self, node):
        size = ceil(sqrt(len(self.goal)))
        sr = sc = 0
        for i in range(0, size):
            sr = sr + sum(s != g for (s, g) in zip(node.state[i * size:(i + 1) * size], self.goal[i * size:(i + 1) * size]))
        for i in range(0, size):
            sc = sc + sum(s != g for (s, g) in zip(node.state[i:len(node.state):size], self.goal[i:len(self.goal):size]))
        return sr + sc
