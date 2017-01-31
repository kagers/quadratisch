from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    f = open(fname)
    r = f.read()
    cmds = r.split('\n')
    f.close()
    i = 0
    
    while i<len(cmds):
        if cmds[i] == 'display':
            draw_lines(points, screen, color)
            display(screen)
            clear_screen(screen)
        elif cmds[i] == 'apply':
            matrix_mult(transform,points)
        elif cmds[i] == 'ident':
            ident(transform)
        elif cmds[i] == 'quit':
            break
        else:
            cmd = cmds[i]
            if i<len(cmds)-1:
                i+=1
            args = cmds[i].split(' ')
            if cmd == 'line':
                add_edge(points,int(args[0]),int(args[1]),int(args[2]),
                         int(args[3]),int(args[4]),int(args[5]))
            elif cmd == 'translate':
                new = make_translate(int(args[0]),int(args[1]),int(args[2]))
                matrix_mult(new,transform)
            elif cmd == 'scale':
                new = make_scale(float(args[0]),float(args[1]),float(args[2]))
                matrix_mult(new,transform)
            elif cmd == 'xrotate':
                new = make_rotX(int(args[0]))
                matrix_mult(new,transform)
            elif cmd == 'yrotate':
                new = make_rotY(int(args[0]))
                matrix_mult(new,transform)
            elif cmd == 'zrotate':
                new = make_rotZ(int(args[0]))
                matrix_mult(new,transform)
            elif cmd == 'circle' or cmd == 'c':
                add_circle(points,int(args[0]),int(args[1]),0,
                           int(args[2]),10000)
            elif cmd == 'hermite' or cmd == 'h':
                add_curve(points,int(args[0]),int(args[1]),
                          int(args[2]),int(args[3]),
                          int(args[4]),int(args[5]),
                          int(args[6]),int(args[7]),
                          10000,1)
            elif cmd == 'bezier' or cmd == 'b':
                add_curve(points,int(args[0]),int(args[1]),
                          int(args[2]),int(args[3]),
                          int(args[4]),int(args[5]),
                          int(args[6]),int(args[7]),
                          10000,2)
            elif cmd == 'save':
                draw_lines(points,screen,color)
                save_ppm(screen,args[0])
            else:
                print 'why '+cmd
        i+=1
