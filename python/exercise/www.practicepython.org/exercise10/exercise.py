import random


def randomNum():
    size = random.randint(1, 20)
    list = []
    index = 0
    while index < size:
        list.append(random.randint(1, 100))
        index += 1
    return list

a = randomNum()
b = randomNum()

print(a)
print(b)

print(set([x for x in a if x in b]))
