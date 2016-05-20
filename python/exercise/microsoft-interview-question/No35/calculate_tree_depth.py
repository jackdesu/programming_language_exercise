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

    input_data[0].set_left(input_data[1])
    input_data[0].set_right(input_data[2])

    input_data[1].set_left(input_data[3])
    input_data[1].set_right(input_data[4])

    input_data[4].set_left(input_data[6])

    input_data[2].set_right(input_data[5])

    input_data[5].set_right(input_data[7])
    input_data[7].set_right(input_data[8])
    input_data[8].set_right(input_data[9])


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

def calculate_depth(head, depth):
    if head is None:
        return 0

    depth += 1
    left_depth = depth
    right_depth = depth
    if head.get_left() is not None:
        left_depth = calculate_depth(head.get_left(), depth)

    if head.get_right() is not None:
        right_depth = calculate_depth(head.get_right(), depth)

    if left_depth > depth:
        depth = left_depth

    if right_depth > depth:
        depth = right_depth

    return depth

initial_array = []
generate_data_set(initial_array)

print(calculate_depth(initial_array[0], 0))