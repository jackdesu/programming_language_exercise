def check_if_post_ordered(input_array, start_index, root_index):
    # input data validation
    if len(input_array) == 0:
        return False

    size = root_index - start_index
    # tree head should be last item
    current_root = input_array[root_index]

    # try to find out left/right tree
    # check left tree, every item in left tree should less than current root
    right_tree_start = start_index
    for x in range(start_index, root_index):
        if input_array[x] > current_root:
            right_tree_start = x
            break

    # check right tree, every item in right tree should greater than current root
    for x in range(right_tree_start, root_index):
        if input_array[x] < current_root:
            return False

    # check if left tree is also in post ordered
    left = True
    left_tree_index = right_tree_start -1
    if start_index < left_tree_index-1:
        left = check_if_post_ordered(input_array, start_index, left_tree_index)

    # check if right tree is also in post ordered
    right = True
    if right_tree_start < root_index-1:
        right = check_if_post_ordered(input_array, right_tree_start, root_index-1)

    return left and right

test_data = [5,7,6,9,11,10,8]
print(check_if_post_ordered(test_data, 0, len(test_data)-1))