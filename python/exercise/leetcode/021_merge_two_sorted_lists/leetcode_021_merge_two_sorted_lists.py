class Node:
    def __init__(self, value, next):
        self._value = value
        self._next = next

    def set_value(self, value):
        self._value = value

    def set_next(self, next):
        self._next = next

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

def traverse(root):
    print(root.get_value())
    if root.get_next() is not None:
        traverse(root.get_next())

def generate_data(base):
    a = Node(base+1, None)
    b = Node(base+2, None)
    c = Node(base+3, None)
    a.set_next(b)
    b.set_next(c)

    return a

data_node_a = generate_data(1)
data_node_b = generate_data(2)

def  merge_2_sorted_list(nodea, nodeb):
    root = None

    if nodea is None:
        return nodeb

    if nodeb is None:
        return nodea

    root = current = Node(-1, None)

    while nodea is not None and nodeb is not None:
        if nodea.get_value() > nodeb.get_value():
            current.set_next(nodeb)
            nodeb = nodeb.get_next()
        else:
            current.set_next(nodea)
            nodea = nodea.get_next()
        current = current.get_next()

    if nodea is not None:
        current.set_next(nodea)
    elif nodeb is not None:
        current.set_next(nodeb)

    return root.get_next()

merged_root = merge_2_sorted_list(data_node_a, data_node_b)
traverse(data_node_a)