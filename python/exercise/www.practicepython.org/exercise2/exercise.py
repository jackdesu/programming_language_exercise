while True:
    userinput = raw_input("please input number: ")
    check = raw_input("please input check: ")
    if userinput == "exit":
        break;

    intvalue = int(userinput)
    mod = intvalue % int(check)
    if mod == 0:
        if intvalue % 4:
            print("even")
        else:
            print("divide4 by 4")
    else:
        print("odd")