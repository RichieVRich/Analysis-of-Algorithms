def options(x,y,m, len):

    #
    m[y][x]
    #
    neg_right = 0
    neg_down = 0

    if x < len - 1:
        right = m[y][x+1]
    else:
        right = -9999
    if y < len - 1:
        down = m[y+1][x]
    else:
        down = -9999


    if right < down:
        return 1
    elif down < right:
        return 2
    else:
        0

def getTesla(M):

    length = len(M)
    pos_x = 0
    pos_y = 0
    end_goal = len(M)
    total = M[0][0]
    hp = 0
    while pos_x != end_goal - 1 or pos_y != end_goal - 1:
        print('coridant = x: ', pos_x, ' y: ', pos_y)
        test = options(pos_x, pos_y, M , length)
        print((test))
        if test == 1:
            pos_y += 1
        elif test == 2:
            pos_x += 1
        print(pos_x, pos_y)
        total += M[pos_y][pos_x]
        print('total= ', total)
    if M[0][0] < 0:
        hp = abs(M[0][0]) + 1
        print('output:' ,hp)







M = [[-1, -2, 2], [10, -8, 1], [-5, -2, -3]]

getTesla(M)