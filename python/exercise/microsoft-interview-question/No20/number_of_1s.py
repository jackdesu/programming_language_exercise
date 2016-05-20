a = 1024
number_of_1 = 0
while a > 0:
    if a & 1 == 1:
        number_of_1 += 1
    a = a >> 1

print(number_of_1)