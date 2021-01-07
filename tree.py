class Node:
    def __init__(self,value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, child_node):
        if child_node not in self._children:
            self._children.append(child_node)
        # if child_node._parent != self:
            child_node.parent = self

    def remove_child(self, child_node):
        if child_node in self._children:
            self._children.remove(child_node)
            child_node.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, new_parent):
        if self._parent is new_parent:
            return
        if self._parent is not None:
            self._parent.remove_child(self)
        self._parent = new_parent
        if new_parent is not None:
            new_parent.add_child(self)


    def depth_search(self, value):
        if not self:
            return None
        if self._value == value:
            return self

        for child in self.children:
            result = child.depth_search(value)
            if result:
                return result
        # return None

    def __repr__(self):
        return f'{self.value}'

    

    # def __str__(self):
    #     return f"Node<{self._value}>"    

    # def breadth_search(self, value):
    #     self_list = [self]
    #     while len(self_list) > 0:
    #         new_Node = self_list.pop()
    #         if new_Node.value == value:
    #             return new_Node



node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2

print(node1.children)
print(node2.children)