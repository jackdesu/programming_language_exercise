import random

start = random.randint(0, 100)
end = start + random.randint(1, 100)
space = list(str(x) for x in range(start, end))

print space

guess = raw_input("what number you want to check? ")
print guess, "is in the list? ", guess in space
