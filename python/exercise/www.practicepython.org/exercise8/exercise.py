rock = {"rock": "DREW", "paper": "B", "scissors": "A"}
paper = {"rock": "A", "paper": "DREW", "scissors": "B"}
scissors = {"rock": "B", "paper": "A", "scissors": "DREW"}
match = {"rock": rock, "paper": paper, "scissors": scissors}

# start loop
while True:
    # ask player a to play
    playerA = raw_input("Player A: ").lower()
    # ask player b to play
    playerB = raw_input("Player B: ").lower()

    # to compare player a and b and to display the outcome
    winner = match[playerA][playerB]
    if winner == "DREW":
        print(winner)
    else:
        print("winner is: " + winner)
    # to ask user if next run, if no, break
    nextRun = raw_input("Next run? (Y/N)").lower()
    if nextRun == "y":
        continue
    else:
        break
