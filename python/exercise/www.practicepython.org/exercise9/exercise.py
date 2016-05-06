import random

totalTrial = 0
hit = 0
while True:
    totalTrial += 1
    # to ask user input 1 ~ 9
    inputNumber = raw_input("please input a number (1 ~ 9): ")
    # to make a random number and compare it
    result = random.randint(1, 9) - int(inputNumber)
    if result == 0:
        print("Good guess!")
        hit += 1
    elif result > 0:
        print("almost there, you are " + str(result) + " below the target")
    else:
        print("almost there, you are " + str(result * -1) + " above the target")

    # to ask if user want to next run
    nextRun = raw_input("Play again? (Y/N)").lower()
    if nextRun == "y":
        continue
    else:
        print("Total play: " + str(totalTrial) + " success: " + str(hit))
        break
