import queue

class Node:
    def __init__(self, left, right, value):
        self._left = left
        self._right = right
        self._value = value


    def get_left(self):
        return self._left


    def get_right(self):
        return self._right


    def get_value(self):
        return self._value


    def set_left(self, left):
        self._left = left


    def set_right(self, right):
        self._right = right


    def set_value(self, value):
        self._value = value

    def print_value(self):
        print(self._value)


def generate_data_set(input_data):
    for x in range(0, 11):
        input_data.append(Node(None, None, x + 1))

    input_data[7].set_left(input_data[5])
    input_data[7].set_right(input_data[9])

    input_data[5].set_left(input_data[4])
    input_data[5].set_right(input_data[6])

    input_data[9].set_left(input_data[8])
    input_data[9].set_right(input_data[10])


def traverse_top_bottom(root):
    if root is None:
        return

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        current = q.get()
        current.print_value()

        if current.get_left() is not None:
            q.put(current.get_left())

        if current.get_right() is not None:
            q.put(current.get_right())

def mirror_btree(root):
    if root is None:
        return

    if root.get_left() is not None:
        mirror_btree(root.get_left())

    if root.get_right() is not None:
        mirror_btree(root.get_right())

    tmp = root.get_left()
    root.set_left(root.get_right())
    root.set_right(tmp)

initial_array = []
generate_data_set(initial_array)
mirror_btree(initial_array[7])
traverse_top_bottom(initial_array[7])