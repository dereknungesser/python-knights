from tree import Node


class KnightPathFinder:
   def __init__(self, initial_cords):
       self._root = tree.Node(initial_cords)
       self._considered_postitions = set((initial_cords))

