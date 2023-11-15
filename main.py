global grid


def affichage(A):
    a = ''
    
    for i in range(8):
        for j in range(8):
            if A[i][j] == 'b':
                a = a + '⛵'
            elif A[i][j] == '':
                a = a + '🌊'
            elif A[i][j] == 'h' :
                a = a + '💥'
            else :
                a = a + '💦'
        a = a + '\n'
    print(a)
    
