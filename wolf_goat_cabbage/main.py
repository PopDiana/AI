from wolf_goat_cabbage import WolfGoatCabbage
from search import *


def main():

    problem = WolfGoatCabbage((1, 1, 1, 'LEFT', 0, 0, 0), (0, 0, 0, 'RIGHT', 1, 1, 1))  # ( wolf, goat, cabbage )
    path = breadth_first_graph_search(problem).solution()

    print(path, '\n')


if __name__ == "__main__":
    main()
