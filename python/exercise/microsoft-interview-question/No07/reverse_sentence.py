def reverse(input_data, start_index, end_index):
    # simply switch start and end
    while start_index < end_index:
        tmp = input_data[start_index]
        input_data[start_index] = input_data[end_index]
        input_data[end_index] = tmp
        start_index += 1
        end_index -= 1


def reverse_array(input_data):
    if input_data is None:
        return None

    if len(input_data) < 1:
        return None

    # to reverse whole sentence, ex "ab cd ef gh" -> "gh fe dc ba"
    reverse(input_data, 0, len(input_data)-1)

    # to reverse each word
    start = 0
    end = 0
    while end < len(input_data):
        if input_data[end] is " ":
            reverse(input_data, start, end-1)
            start = end + 1
        end += 1

    reverse(input_data, start, len(input_data)-1)

    return "".join(input_data)

def reverse_string(input_data):
    if input_data is None:
        return None

    converted_list = input_data.split(" ")
    reversed_list = converted_list[::-1]

    return " ".join(reversed_list)


test_data_string = "This is a book"
test_data_array = list(test_data_string)

print(reverse_string(test_data_string))
print(reverse_array(test_data_array))