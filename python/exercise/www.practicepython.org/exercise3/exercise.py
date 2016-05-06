#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#print ([x for x in a if x < 5])

userlist = raw_input("please enter a number list and separator is ',': ")
smallerthan = raw_input("please enter your filter: ")
print([x for x in userlist.split(",") if int(x) < int(smallerthan)])