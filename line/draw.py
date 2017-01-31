from display import *

def draw_line(screen, x0, y0, x1, y1, color):
    if x1 < x0:
        #print "switched"
        draw_line(screen, x1, y1, x0, y0, color);
    
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1

    if y1 > y0: # 1 2 5 6
        d = A*2 + B
        if A < -B:
            #print "1"
            while x < x1: # 1 5
                plot(screen, color, x, y)
                if d > 0:
                    y+=1
                    d+=B*2
                x+=1
                d+=A*2
        else:
            #print "2"
            while y < y1: # 2 6
                plot(screen, color, x, y)
                if d < 0:
                    x+=1
                    d+=A*2
                y+=1
                d+=B*2
    else: # 3 4 7 8
        d = A*2 - B
        if A > B:
            #print "4"
            while x < x1: # 4 8
                plot(screen, color, x, y)
                if d < 0:
                    y-=1
                    d-=B*2
                x+=1
                d+=A*2
        else:
            #print "3"
            while y > y1: # 3 7
                plot(screen, color, x, y)
                if d > 0:
                    x+=1
                    d+=A*2
                y-=1
                d-=B*2
