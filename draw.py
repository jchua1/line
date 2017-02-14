from display import *

def draw_line(screen, x0, y0, x1, y1, color):
    slope = (y1 - y0) / (x1 - x0)
    if 0 <= slope <= 1:
        octant_1(screen, x0, y0, x1, y1, color)
    elif slope > 1:
        octant_2(screen, x0, y0, x1, y1, color)
    elif -1 <= slope < 0:
        octant_8(screen, x0, y0, x1, y1, color)
    else:
        octant_7(screen, x0, y0, x1, y1, color)

def octant_1(screen, x0, y0, x1, y1, color):
    x = x0
    y = y0
    A = y1 - y0
    B = -(x1 - x0)
    d = 2 * A + B
    while x < x1:
        plot(screen, color, x, y)
        if d > 0:
            y += 1
            d += 2 * B
        x += 1
        d += 2 * A
    pass

def octant_2(screen, x0, y0, x1, y1, color):
    x = x0
    y = y0
    A = y1 - y0
    B = -(x1 - x0)
    d = A + 2 * B
    while y < y1:
        plot(screen, color, x, y)
        if d < 0:
            x += 1
            d += 2 * A
        y += 1
        d += 2 * B
    pass

def octant_8(screen, x0, y0, x1, y1, color):
    x = x0
    y = y0
    A = y1 - y0
    B = -(x1 - x0)
    d = 2 * A - B
    while x < x1:
        plot(screen, color, x, y)
        if d < 0:
            y -= 1
            d -= 2 * B
        x += 1
        d += 2 * A
    pass

def octant_7(screen, x0, y0, x1, y1, color):
    x = x0
    y = y0
    A = y1 - y0
    B = -(x1 - x0)
    d = A - 2 * B
    while y > y1:
        plot(screen, color, x, y)
        if d > 0:
            x += 1
            d += 2 * A
        y -= 1
        d -= 2 * B
    pass
