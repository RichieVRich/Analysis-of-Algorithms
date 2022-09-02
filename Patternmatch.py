def pattermatch(string, p):

    print(string, p)
    valid = 1
    a = 0
    b = 0
    max_b =  len(p) -1

    max_a = len(string)

    while valid and a < max_a:

        if b < max_b:

            b = max_b
        if string[a] == p[b]:
            valid = 1
            a +=1
            b += 1
        elif p[b] == '*':
            valid = 1


            if b < max_b:
                c = b + 1
                if p[c] == string[a]:

                    b += 2
                    if b < max_b:
                        b = max_b - 1
            a += 1


        elif p[b] == '?':
            valid = 1
            a += 1
            b += 1
        else:
            valid = 0

    print('Output = ', valid == 1)



pattermatch("abcde","*a?c*")
#
pattermatch("abcde","*")
pattermatch("abcde", "a*d" )
#pattermatch("abcde","ad")
#