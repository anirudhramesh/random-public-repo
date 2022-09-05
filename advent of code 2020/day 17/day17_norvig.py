#%%

from typing import List, Tuple, Set, Dict
from itertools import product, chain
from functools import lru_cache
import operator
from collections import Counter

#%%

flatten = chain.from_iterable
Picture = List[str]
def lines(text: str) -> List[str]:
    "Split the text into a list of lines."
    return text.strip().splitlines()

#%%

# in17: Picture = lines('''
# ##.#....
# ...#...#
# .#.#.##.
# ..#.#...
# .###....
# .##.#...
# #.##..##
# #.####..
# ''')
in17: Picture = lines(open('input17.txt').read())

#%%

Cell = Tuple[int, ...]

def day17_1(picture, d=3, n=6):
    "How many cells are active in the nth generation?"
    return len(life(parse_cells(picture, d), n))

def parse_cells(picture, d=3, active='#') -> Set[Cell]:
    "Convert a 2-d picture into a set of d-dimensional active cells."
    return {(x, y, *(0,) * (d - 2))
            for (y, row) in enumerate(picture)
            for x, cell in enumerate(row) if cell is active}

def life(cells, n) -> Set[Cell]:
    "Play n generations of Life."
    for g in range(n):
        cells = next_generation(cells)
    return cells

def next_generation(cells) -> Set[Cell]:
    """The set of live cells in the next generation."""
    return {cell for cell, count in neighbor_counts(cells).items()
            if count == 3 or (count == 2 and cell in cells)}

# @lru_cache()
def cell_deltas(d: int):
    return set(filter(any, product((-1, 0, +1), repeat=d)))

def neighbor_counts(cells) -> Dict[Cell, int]:
    """A Counter of the number of live neighbors for each cell."""
    return Counter(flatten(map(neighbors, cells)))

def neighbors(cell) -> List[Cell]:
    "All adjacent neighbors of cell in three dimensions."
    return [tuple(map(operator.add, cell, delta))
            for delta in cell_deltas(len(cell))]


print(day17_1(in17, d=4, n=15))

# print(len(life(in17, 0)))