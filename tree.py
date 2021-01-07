class Node 
    def __init__(self,value)
        self._value =value
        self._parent = None
        self._children = list()

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, child_node):
        if child_node not in self._children
            self._children.append(child_node)
        if child_node._parent != self:
            child_node._parent = self           

    def remove_child(self, child_node):
        if child_node in self._children
            self.children.remove(child_node)   
            child_node._parent = None 

    @property
    def parent(self):
        return self._parent   

    @parent.setter
    def parent(self, child_node)
        self._parent = child_node
        child_node.add_child(self)
