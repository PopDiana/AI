from n_puzzle import *
from search import *

def main():

    # n = 8
    n_puzzle_miss = NPuzzleMiss((1, 2, 3, 4, 8, 0, 7, 6, 5), (1, 2, 3, 4, 5, 6, 7, 8, 0), 8)
    n_puzzle_mht = NPuzzleMht((1, 2, 3, 4, 8, 0, 7, 6, 5), (1, 2, 3, 4, 5, 6, 7, 8, 0), 8)
    n_puzzle_euc = NPuzzleEuc((1, 2, 3, 4, 8, 0, 7, 6, 5), (1, 2, 3, 4, 5, 6, 7, 8, 0), 8)
    n_puzzle_rc = NPuzzleRC((1, 2, 3, 4, 8, 0, 7, 6, 5), (1, 2, 3, 4, 5, 6, 7, 8, 0), 8)

    n_path1 = astar_search(n_puzzle_miss).solution()
    n_path2 = astar_search(n_puzzle_mht).solution()
    n_path3 = astar_search(n_puzzle_euc).solution()
    n_path4 = astar_search(n_puzzle_rc).solution()

    print(n_path1, '\n')
    print(n_path2, '\n')
    print(n_path3, '\n')
    print(n_path4, '\n')

    compare_searchers(problems=[n_puzzle_miss, n_puzzle_mht, n_puzzle_euc, n_puzzle_rc],
                      header=['Searcher', 'A* h1(n) Misplaced tiles',
                              'A* h2(n) Manhattan distance','A* h3(n) Euclidean distance', 'A* h4(n) Misplaced tiles on rows and columns'], searchers=[
            astar_search,
            recursive_best_first_search])

if __name__ == "__main__":
    main()
