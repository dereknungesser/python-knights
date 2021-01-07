from tree import Node


class KnightPathFinder:
   def __init__(self, initial_cords):
       self._initial_cords = initial_cords
       self._root = Node(initial_cords)
       self._considered_postitions = set((initial_cords))

    def get_valid_moves(self, pos):
        pos = (x, y)
        new_moves = {
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        }
        return possible_moves
