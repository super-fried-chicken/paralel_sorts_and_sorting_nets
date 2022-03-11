lis = [(0 , 1), (1 , 2), (2 , 3), (0 , 1), (1 , 2), (0 , 1)]
lis1 = [(0 , 1), (2 , 3), (0 , 2), (1 , 3), (1 , 2)]

def print_line (x, y, num):
    i = 0
    while i < x:
        print ('. ', end = '')
        i = i + 1
    i = x
    while i < y:
        print ('._', end = '')
        i = i + 1
    i = y
    while i < num:
        print ('. ', end = '')
        i = i + 1
    print ('.')

def print_stick (num):
    i = 0
    while i < num:
        print ('| ', end = '')
        i = i + 1
    print ('|')
    
def print_net (lis, num) :
    for i in lis:
        print_stick (num)
        print_line ( i[0] , i[1] , num)
    print_stick (num)

print_net (lis, 3)

print ( )
print ( )

print_net (lis1, 3)

        
    
