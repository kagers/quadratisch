from display import *
from matrix import *
from math import sin, cos, radians
PI = math.pi

def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    w = r+cx
    x = cy
    while t<1.001:
        y = r*cos(2*PI*t) + cx
        z = r*sin(2*PI*t) + cy
        add_edge(points, w, x, 0, y, z, 0)
        w = y
        x = z
        t+=1.0/step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    xc = generate_curve_coefs(x0,x1,x2,x3,curve_type)
    yc = generate_curve_coefs(y0,y1,y2,y3,curve_type)

    t=0.0
    step = 1.0/step
    while t<=1:
        x1 = t*( t*( t*xc[0][0] + xc[0][1] ) + xc[0][2] ) + xc[0][3] 
        y1 = t*( t*( t*yc[0][0] + yc[0][1] ) + yc[0][2] ) + yc[0][3] 
        add_edge(points,x0,y0,0,x1,y1,0)
        x0 = x1
        y0 = y1
        t+=step
    
def draw_lines( matrix, screen, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
        
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

