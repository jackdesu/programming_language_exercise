def oneAndLast(arg_list=()):
    return arg_list[0], arg_list[len(arg_list)-1]

array = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(oneAndLast(array))