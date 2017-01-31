import math
pic = open('pic.ppm', 'w')

pic.write('P3 500 500 255\n')

for i in range(0,500):
    line = ""
    for j in range(0,500):
        r = math.sin(i/24)*i%256
        g = math.cos(j/8)*i%256
        b = math.tan(math.hypot(((i+j)/(i*i+1)),i))%256
        line+='%d %d %d '%(r,g,b)
    pic.write(line)
    pic.write('\n')

pic.close()
