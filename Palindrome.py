def checkPalindrome_1(string, k):
    print('checkPalindrome1 says: ')
    x = 0
    y = len(string) - 1
    z = 0
    length = len(string) -1
    check = 0
    while x <= length or y >= 0:

        if x == y:
            check = 1
        if string[x] == string[y] and x != y:
            x += 1
            y -= 1
        else:
            z += 1
            x += 1
            y -= 1
        if x == y and check == 1:
            break

    print('output:' , z)

def split(word):
          return [char for char in word]



def checkPalindrome_2(string, k):
    print('checkPalindrome2 says:')
    length = (len(string) + 1) //2 + 1

    Matrix = [ [0] * length for i in range(length)]
    x = 1
    y = 1
    w = 0
    z = 0
    length -= 1
    # String Split method credit GeeksforGeeks
    #   https://www.geeksforgeeks.org/python-split-given-string-into-equal-halves/
    test, test2 = string[:len(string)//2],string[len(string)//2:]

    for  i in test:
        for j in reversed(test2):
           # print(i,j, z, w, i == j)
            if i == j:
                Matrix[y][x] = Matrix[y-1][x-1] + 1

            else:
                Matrix[y][x] = max(Matrix[y-1][x],Matrix[y][x-1])

            x += 1
        y += 1
        x = 1
        w = 0

    answer = Matrix[length-1][length-1] * 2
    a = len(string)
    answer = a - answer

    print('output:' , answer)


str1 = "abdba"
checkPalindrome_1(str1,1)
checkPalindrome_2(str1,2)