input = raw_input("please enter a number: ")
for x in range(2, int(input)/2 + 1):
    if int(input) % x == 0:
        print x