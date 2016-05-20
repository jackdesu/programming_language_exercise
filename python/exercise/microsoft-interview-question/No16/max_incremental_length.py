# to find the max length k
def get_max_length(input_data):

    if input_data is None:
        return 0

    if len(input_data) < 3:
        return len(input_data)

    input_data.sort()

    start = 0
    end = 0
    current_start=0
    current_end=0

    for x in range(0, len(input_data)-1):
        if (input_data[x+1] - input_data[x]) == 1:
            current_end = x

        if (current_end - current_start) > (end - start):
            start = current_start
            end = current_end

            current_start = x
            current_end = x

    return end - start + 2

test_data = [1,2,3, 5, 6, 7, 8, 9]
print(get_max_length(test_data))