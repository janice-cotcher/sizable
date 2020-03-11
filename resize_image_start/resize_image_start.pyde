# a set of inscribed squares and circles
background(52, 229, 235)
size(1000, 500)


def squares(w):
    """Three squares inside of each other
    w is the width of the smallest square
    """
    # light green large sqaure
    fill(52, 235, 58)
    square(100, 100, 3*w)
    #medium green middle square
    fill(40, 181, 44)
    square(100, 100, 2*w)
    # dark green small square
    fill(25, 115, 28)
    square(100, 100, w)


def circles(r):
    """Three circles inside each other
    r is the radius of the smallest circle
    """
    # dark purple large circle
    fill(108, 25, 115)
    circle(750, 250, 3*r)
    # medium purple middle circle
    fill(165, 39, 176)
    circle(750, 250, 2*r)
    # light purple small circle
    fill(220, 52, 235)
    circle(750, 250, r)


squares(100)
circles(100)
