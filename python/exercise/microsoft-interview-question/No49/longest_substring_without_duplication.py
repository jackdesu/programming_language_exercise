def longest(input_array):
    if input_array is None:
        return 0

    size = len(input_array)
    if size == 0:
        return 0

    longest_size = 1

    for x in range(0, size):
        current_size = 1
        current_char = input_array[x]
        for y in range(x+1, size):
            if current_char != input_array[y]:
                current_size += 1
            else:
                break

        if current_size > longest_size:
            longest_size = current_size

    return longest_size

test_string = "abcdeabcdefg"
test_input = list(test_string)
print(longest(test_input))