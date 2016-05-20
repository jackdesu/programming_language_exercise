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
    for x in range(0, 9):
        input_data.append(Node(None, None, x + 1))

    input_data[1].set_left(initial_array[0])
    input_data[1].set_right(initial_array[2])

    input_data[3].set_left(initial_array[1])
    input_data[3].set_right(initial_array[8])

    input_data[8].set_left(initial_array[6])

    input_data[6].set_left(initial_array[4])
    input_data[6].set_right(initial_array[7])

    input_data[4].set_right(initial_array[5])

initial_array = []
generate_data_set(initial_array)

head = initial_array[3]

def traverse_list(node_head, tail):
    node_head.print_value()

    if tail:
        if node_head.get_left() is not None:
            traverse_list(node_head.get_left(), tail)
    else:
        if node_head.get_right() is not None:
            traverse_list(node_head.get_right(), tail)

def get_minimum_node(node_head):
    if node_head.get_left() is not None:
        return get_minimum_node(node_head.get_left())
    else:
        return node_head


global_head = get_minimum_node(initial_array[3])
global_tail = global_head

def transform_binary_search_tree(node_head):
    if node_head.get_left() is not None:
        transform_binary_search_tree(node_head.get_left())

    #node_head.print_value()
    global global_tail

    # a special case to handle head == tail case
    if node_head is not global_tail:
        global_tail.set_right(node_head)
        node_head.set_left(global_tail)

    global_tail = node_head

    if node_head.get_right() is not None:
        transform_binary_search_tree(node_head.get_right())



def transform_to_linked_list(node_head):
    if node_head == None:
        return None

    if node_head.get_left() == None and node_head.get_right() == None:
        return node_head


#traverse_list(initial_array[3])
transform_binary_search_tree(initial_array[3])
traverse_list(global_head, False)
traverse_list(global_tail, True)
