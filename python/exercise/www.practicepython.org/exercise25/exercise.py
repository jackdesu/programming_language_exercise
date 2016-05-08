total_run = 0


def binary_search(target, start, end):
    global total_run
    total_run += 1

    if start == end:
        return False

    middle = (start+end) / 2
    if middle == target:
        return True
    elif target > middle:
        return binary_search(target, middle, end)
    else:
        return binary_search(target, start, middle)


goal = int(raw_input("please enter a number (0 ~ 100): "))
guess = 50;
if goal < 0 or goal > 100:
    print goal, " is not a valid input!"
else:
    found = binary_search(goal, 0, 100)
    if found:
        print "Total guess: ", total_run
    else:
        print "not found!"
