def isPrime(number):
    prime = True
    for x in range(2, number/2):
        if number % x == 0:
            prime = False
            break
    return prime

userinput = raw_input("please enter a number: ")

print("your input is : " + userinput)
print([x for x in range(1, int(userinput)) if isPrime(x)])

