from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

for x in range(0, 501):
    for y in range(0, 501):
        if x % 125 == 0 and y % 125 == 0:
            draw_line(screen, 250, 250, x, y, color)

display(screen)
save_extension(screen, 'img.png')
