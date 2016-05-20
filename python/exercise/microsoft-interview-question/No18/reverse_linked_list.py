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

def generate_data():
    a = Node(1, None)
    b = Node(2, None)
    c = Node(3, None)
    a.set_next(b)
    b.set_next(c)

    return a
global_root = None

def reverse_linked_list(root, previous):
    if root is None:
        return None

    global global_root
    global_root = root
    if root.get_next() is not None:
        tmp = root.get_next()
        reverse_linked_list(tmp, root)
    root.set_next(previous)

test_root = generate_data()
reverse_linked_list(test_root, None)

traverse(global_root)