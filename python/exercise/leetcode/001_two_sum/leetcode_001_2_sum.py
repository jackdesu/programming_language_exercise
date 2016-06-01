def find_2_index(numbers, target):
    history = {}
    history.setdefault(numbers[0], 0)
    for x in range(1, len(numbers)):
        difference = target - numbers[x]
        found = history.get(difference, -1)
        if found > -1:
            return [found, x]
        history.setdefault(numbers[x], x)

test_input = [1,2,3,4,5,6,7,8]

print(find_2_index(test_input, 15))