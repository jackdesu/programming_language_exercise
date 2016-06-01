def reverse_string(input_string):
    if input_string is None:
        return None

    result = input_string[::-1]
    return result

print(reverse_string('this is a book'))

