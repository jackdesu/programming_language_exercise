a = int(raw_input("please enter 1st number: "))
b = int(raw_input("please enter 2nd number: "))
c = int(raw_input("please enter 3rd number: "))

big = None
if not a < b and not b < c:
    big = a
elif not b < a and not a < c:
    big = b
else:
    big = c

print(str(big) + " is the max")
