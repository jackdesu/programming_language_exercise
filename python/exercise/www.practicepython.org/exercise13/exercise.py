def fibonacci(end):
    if end <= 1:
        return end
    else:
        return fibonacci(end-1) + fibonacci(end-2)

user_input = raw_input("please enter a number: ")
print([fibonacci(x) for x in range(1, int(user_input)+1)])
