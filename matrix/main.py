from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]


shape = [[0,20],[30,30],[0,0],[1,1]]

add_edge(shape, 20,30,0,20,50,0)
add_edge(shape, 20,50,0,0,50,0)
add_edge(shape, 0,50,0,0,30,0)

add_edge(shape, 60,30,0,40,30,0)
add_edge(shape, 60,50,0,40,50,0)
add_edge(shape, 40,30,0,40,50,0)
add_edge(shape, 60,30,0,60,50,0)

add_edge(shape, 0,20,0,10,5,0)
add_edge(shape, 10,5,0,20,20,0)

add_edge(shape, 40,20,0,50,5,0)
add_edge(shape, 50,5,0,60,20,0)

add_edge(shape, 30,20,0,30,70,0)
add_edge(shape, 30,70,0,20,70,0)    

add_edge(shape, 5,85,0,55,85,0)

draw_lines(matrix_mult(make_scale(0.35,0.35,0.35),
                       matrix_mult(make_translate(1250,800,0),shape)),screen,
           color)
draw_lines(matrix_mult(make_scale(3,5,5),shape),screen,color)
draw_lines(matrix_mult(make_translate(300,300,0),
                       matrix_mult(make_rotZ(45),shape)),screen,color)

x = 200
theta = 1
while x<XRES:
    draw_lines(matrix_mult(make_translate(x,0,0),
                           matrix_mult(make_rotX(theta),shape)),screen,color)
    x+=65
    theta+=12

x = 200
while x<XRES:
    draw_lines(matrix_mult(make_translate(x,120,0),
                           matrix_mult(make_rotX(theta),shape)),screen,color)
    x+=65
    theta+=12

x = 200
while x<XRES:
    draw_lines(matrix_mult(make_translate(x,240,0),
                           matrix_mult(make_rotX(theta),shape)),screen,color)
    x+=65
    theta+=12

display(screen)
