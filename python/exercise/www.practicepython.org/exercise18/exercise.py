import random

initial_set = list("0123456789")
print(initial_set)

puzzle = []
for x in range(0, 4):
    puzzle.append(initial_set.pop(random.randint(0, len(initial_set)-1)))

total_guess = 0
while True:
    user_guess = raw_input("what is your guess: ")
    user_guess_list = list(user_guess)
    total_guess += 1
    cows = 0
    bulls = 0
    for index in range(0, 4):
        current = user_guess_list[index]
        print("current: " + str(current))
        if current in puzzle:
            if index == puzzle.index(current):
                cows += 1
            else:
                bulls += 1

    if cows == 4:
        print("Bingo!, total guess: ", total_guess)
        break
    else:
        print("hmm hmm ", cows, " cows, ", bulls, " bulls")
