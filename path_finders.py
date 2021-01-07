from tree import Node


class KnightPathFinder:
    def __init__(self, initial_cords):
       self._initial_cords = initial_cords
       self._root = Node(initial_cords)
       self._considered_postitions = set((initial_cords))

    def get_valid_moves(self, pos):
        (x, y) = pos
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
        possible_moves = {
            (x + i, y + j) for (i , j) in new_moves
            if(x + i <= 8 and x + i >=0 and y + j <= 8 and y + j >= 0)
        }

        return possible_moves

    def new_move_positions(self, pos):
        possible_moves = self.get_valid_moves(pos)

        new_moves = possible_moves.difference(self._considered_postitions)

        self._considered_postitions = self._considered_postitions.union(new_moves)
        return new_moves


finder = KnightPathFinder((0, 0))
print(finder.new_move_positions((0, 0)))