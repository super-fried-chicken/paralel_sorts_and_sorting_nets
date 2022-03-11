lis = [(0 , 1), (1 , 2), (2 , 3), (0 , 1), (1 , 2), (0 , 1)]
listic = [(0 , 1), (2 , 3), (4 , 5), (6 , 7), (0 , 2), (1 , 3),(4 , 6), (5 , 7)]

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
        #print_stick (num)
        print_line ( i[0] , i[1] , num)
    #print_stick (num)

print_net (listic, 7)

print ( )
print ( )


def maximum (lis, l, maxim) :
    i = 0
    while i < (len (lis)):        
        if (lis[i][0] in l) or (lis[i][1] in l):       
            maxim = max(maxim, (len(l)))
            l = []
        else:
            l.append (lis[i][0])
            l.append (lis[i][1])
        i = i + 1
    return maxim



print (maximum (listic, [], 0)/2)










      
