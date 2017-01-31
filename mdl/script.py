import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    tmps = []
    screen = new_screen()
        
    for command in commands:
        
        #print command

        if command[0] == 'line':
            add_edge( tmps, command[1], command[2], command[3], command[4], command[5], command[6] )
            matrix_mult(stack[-1], tmps)
            draw_lines(tmps, screen, color)
            tmps=[]

        elif command[0] == 'box':
            add_box( tmps, command[1], command[2], command[3], command[4], command[5], command[6] )
            matrix_mult(stack[-1], tmps)
            draw_polygons(tmps, screen, color)
            tmps=[]

        elif command[0] == 'sphere':
            add_sphere( tmps, command[1], command[2], command[3], command[4], 5 )
            matrix_mult(stack[-1], tmps)
            draw_polygons(tmps, screen, color)
            tmps=[]

        elif command[0] == 'torus':
            add_torus( tmps, command[1], command[2], command[3], command[4], command[5], 5 )
            matrix_mult(stack[-1], tmps)
            draw_polygons(tmps, screen, color)
            tmps=[]

        elif command[0] == 'scale':
            s = make_scale( command[1], command[2], command[3] )
            matrix_mult(stack[-1], s)
            stack[-1]=s

        elif command[0] == 'move':
            t = make_translate( command[1], command[2], command[3] )
            matrix_mult(stack[-1], t)
            stack[-1]=t
        
        elif command[0] == 'rotate':
            angle = command[2] * ( math.pi / 180 )
            if command[1] == 'x':
                r = make_rotX( angle )
            elif command[1] == 'y':
                r = make_rotY( angle )
            elif command[1] == 'z':
                r = make_rotZ( angle )
            matrix_mult(stack[-1], r)
            stack[-1]=r
            
        elif command[0] == 'push':
            stack.append(new_matrix())
            for i in range(4):
                for j in range(4):
                    stack[-1][i][j] = stack[-2][i][j]

        elif command[0] == 'pop':
            stack.pop()

        elif command[0] == 'save':
            save_extension(screen, command[1])

        elif command[0] == 'display':
            display(screen)

        
