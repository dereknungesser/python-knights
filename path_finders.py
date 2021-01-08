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
    def build_move_tree(self):
        queue = [self._root]
        while queue:
            node = queue.pop(0)
            moves = self.new_move_positions(node.value)
            child_nodes = [Node(pos) for pos in moves]
            for child_node in child_nodes:
                node.add_child(child_node)
            queue.extend(child_nodes)

    def find_path(self, end_position):
        end_node = self._root.depth_search(end_position)
        return self.trace_to_root(end_node)

    def trace_to_root(self, end_node):
        queue = [end_node]
        path = []
        while queue:
            node = queue.pop(0)
            parent = node.parent
            path.insert(0, node.value)
            if parent == self._root:
                path.insert(0, parent.value)
                return path
            queue.append(parent)





# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# print("This", finder._root.children)
# print(finder.new_move_positions((0, 0)))

finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder.find_path((2, 1))) # => [(0, 0), (2, 1)]
print(finder.find_path((3, 3))) # => [(0, 0), (2, 1), (3, 3)]
print(finder.find_path((6, 2))) # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
print(finder.find_path((7, 6))) # => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
