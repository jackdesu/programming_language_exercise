def isPowerOfFour(self, data):
    if data == 1:
        return True
    occurrenceof1 = False
    run = 0

    while data > 0:
        if occurrenceof1:
            if data & 1:
                return False
        else:
            if data & 1:
                occurrenceof1 = True

        run += 1
        data = data >> 1

    run -= 1
    if (run / 2 > 0) and (run % 2 == 0) and occurrenceof1:
        return True

    return False

print(isPowerOfFour('test', 16))