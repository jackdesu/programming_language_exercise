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

def generate_data(loop):
    data_set = []
    for x in range(0, 10):
        data_set.append(Node(x+1, None))
        if x > 0:
            data_set[x-1].set_next(data_set[x])

    if loop:
        data_set[4].set_next(data_set[3])
    return data_set[0]

def is_loop(head):
    if head is None:
        return False

    fast_index = head.get_next()

    if fast_index is None:
        return False

    slow_index = fast_index

    fast_index = fast_index.get_next()
    if fast_index is None:
        return False

    while (fast_index is not None) and (slow_index is not None):
        if fast_index == slow_index:
            return True

        slow_index = slow_index.get_next()
        fast_index = fast_index.get_next()

        if fast_index is not None:
            fast_index = fast_index.get_next()

    return False

test_root_without_loop = generate_data(False)
print(is_loop(test_root_without_loop))

test_root_with_loop = generate_data(True)
print(is_loop(test_root_with_loop))