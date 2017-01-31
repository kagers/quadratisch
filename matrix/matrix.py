from math import radians, cos, sin

def make_translate( x, y, z ):
    return [[1,0,0,x],
            [0,1,0,y],
            [0,0,1,z],
            [0,0,0,1]]

def make_scale( x, y, z ):
    return [[x,0,0,0],
            [0,y,0,0],
            [0,0,z,0],
            [0,0,0,1]]
    
def make_rotX( theta ):
    t = radians(theta)
    return [[1,0,0,0],
            [0,cos(t),-sin(t),0],
            [0,sin(t),cos(t),0],
            [0,0,0,1]]

def make_rotY( theta ):
    t = radians(theta)
    return [[cos(t),0,-sin(t),0],
            [0,1,0,0],
            [sin(t),0,cos(t),0],
            [0,0,0,1]]

def make_rotZ( theta ):
    t = radians(theta)
    return [[cos(t),-sin(t),0,0],
            [sin(t),cos(t),0,0],
            [0,0,1,0],
            [0,0,0,1]]

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    for row in matrix:
        r="|\t"
        i = 0
        while i < len(row):
            r+=str(row[i])+"\t"
            i+=1
        r+="|"
        print r

def ident( matrix ):
    i = 0
    while i<len(matrix):
        j = 0
        while j<len(matrix[i]):
            if i==j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    return matrix

def scalar_mult( matrix, x ):
    for row in matrix:
        for col in row:
            col*=x
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m3 = new_matrix(len(m2[0]),len(m1))
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                m3[i][j]+=m1[i][k]*m2[k][j]
    return m3

'''
print_matrix(make_translate(1,2,3))
print
print_matrix(make_scale(4,5,6))
print
print_matrix(make_rotX(30))
print
print_matrix(make_rotY(90))
print
print_matrix(make_rotZ(180))
print

m1 = new_matrix(3,2)
m2 = new_matrix(2,3)

m1[0][0] = 1
m1[0][1] = 2
m1[0][2] = 3
m1[1][0] = 4
m1[1][1] = 5
m1[1][2] = 6

m2[0][0] = 7
m2[0][1] = 8
m2[1][0] = 9
m2[1][1] = 10
m2[2][0] = 11
m2[2][1] = 12

print_matrix(m1)
print
print_matrix(m2)
print
print_matrix(scalar_mult(m1,2))
print
print_matrix(matrix_mult(m1,m2))
'''
