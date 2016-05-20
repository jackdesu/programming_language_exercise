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

def get_size(root):
    if root is None:
        return 0

    size = 1
    while root.get_next() is not None:
        size +=1
        root = root.get_next()

    return size

def find_kth_from_end(k, root, size):
    if root is None:
        return None

    if k > size:
        return None

    for x in range(0, size-k):
        root = root.get_next()

    return root

def generate_data_set():
    data_list = []
    for x in range(0, 10):
        data_list.append(Node(x+1, None))

    for x in range(0, len(data_list)-1):
        data_list[x].set_next(data_list[x+1])

    return data_list

def traverse_linked_list(root):
    while root is not None:
        print(root.get_value())
        root = root.get_next()

# try to calculate the size of this list, L
# from root, go L-k step and return it
test_data = generate_data_set()
traverse_linked_list(test_data[0])
print(find_kth_from_end(2, test_data[0], get_size(test_data[0])).get_value())
