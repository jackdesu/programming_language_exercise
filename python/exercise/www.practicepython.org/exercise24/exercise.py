def draw_row(size):
    print "-" + "----" * size


def draw_column(size):
    print "|" + "   |" * size


size = int(raw_input("please enter the size your want: "))

draw_row(size)
for x in range (0, size):
    draw_column(size)
    draw_row(size)
