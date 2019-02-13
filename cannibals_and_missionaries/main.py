from cannibals import Cannibals
from search import *


def main():

    cannibals_and_missionaries = Cannibals((3, 3, 'LEFT', 0, 0), (0, 0, 'RIGHT', 3, 3))
    path = breadth_first_graph_search(cannibals_and_missionaries).solution()

    print(path, '\n')


if __name__ == "__main__":
    main()
