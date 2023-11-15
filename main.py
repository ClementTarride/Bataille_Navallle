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
    
def sendMissileAt(rowIndex,columnIndex):
    if grid[rowIndex][columnIndex] == 'b' :
        grid[rowIndex][columnIndex] =  'h'
        return True
    elif grid[rowIndex][columnIndex] == '' :
        grid[rowIndex][columnIndex] = 'm'
        return False
    else :
        print("La case a déja été touché")
        return False
    
