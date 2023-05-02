x = 10

def multiply_x_by_y():
    global x
    y = 5
    x = x*y
    return x

assert multiply_x_by_y() == 50