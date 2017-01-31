from display import *
from draw import *
import math

def actual():
    screen = new_screen()
    
    #sun
    color = [ 207, 123, 0 ]
    the = 0.0
    while the < math.pi/2:
        draw_line(screen, 0, 0, int(XRES/4*math.cos(the)), 
                  int(YRES/4*math.sin(the)), color)
        the += 0.05
    
    #ocean liner
    color[BLUE] = MAX_COLOR
    color[RED] = 0
    color[GREEN] = 0
    y = YRES/2
    while y < YRES:
        draw_line(screen, 0, y, XRES, y, color)
        color[BLUE] -= 7
        y+=7

    color[BLUE] = MAX_COLOR
    color[RED] = 0
    color[GREEN] = 0
    x=0
    while x < XRES:
        draw_line(screen, x, YRES/2, XRES/2, YRES, color)
        color[RED] += 2
        color[GREEN] += 2
        x+=7

    display(screen)


actual()


def example():
    #octant I
    draw_line( screen, 0, 0, XRES - 1, YRES - 75, color )
    #octant II
    draw_line( screen, 0, 0, XRES - 75, YRES - 1, color )
    #octant VIII
    draw_line( screen, 0, YRES - 1, XRES - 1, 75, color )
    #octant VII
    draw_line( screen, 0, YRES - 1, XRES - 75, 0, color )
    
    
    color[ GREEN ] = 0
    color[ BLUE ] = MAX_COLOR
    #octant V
    draw_line( screen, XRES - 1, YRES - 1, 0, 75, color )
    #octant VI
    draw_line( screen, XRES - 1, YRES - 1, 75, 0, color )
    #octant IV
    draw_line( screen, XRES - 1, 0, 0, YRES - 75, color )
    #octant III
    draw_line( screen, XRES - 1, 0, 75, YRES - 1, color )
    

    color[ RED ] = MAX_COLOR
    color[ BLUE ] = 0
    #y = x
    draw_line( screen, 0, 0, XRES - 1, YRES - 1, color )
    #y = -x
    draw_line( screen, 0, YRES - 1, XRES - 1, 0, color )
    
    #color[ GREEN ] = MAX_COLOR
    #horizontal
    draw_line( screen, 0, YRES / 2, XRES - 1, YRES / 2, color )
    #vertical
    draw_line( screen, XRES / 2, 0, XRES / 2, YRES - 1, color )

    display(screen)

