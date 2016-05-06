a = [1, 3, 5, 7, 9, 2, 4, 3, 6, 7, 3, 1, 8, 9]


def get_list_without_dup_by_set(arg_list):
    return set(arg_list)


def get_list_without_dup_by_list(arg_list):
    result = []
    for x in arg_list:
        if x not in result:
            result.append(x)
    return result

print(get_list_without_dup_by_set(a))
print(get_list_without_dup_by_list(a))
