input = raw_input("please enter a palindrome: ")
if input == input[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
