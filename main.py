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
    
def main():
	
 	grid = [['' for _ in range(8)] for _ in range(8)]
  
	grid[0][1] = 'b'
	grid[0][2] = 'b'
	grid[0][3] = 'b'

	grid[3][2] = 'b'
	grid[3][3] = 'b'

	grid [7][5] = 'b'
	grid [6][5] = 'b'
	grid [5][5] = 'b'
	grid [4][5] = 'b'	
	affichage(grid)
	sendMissileAlt(0,5)
	sleep(2)
	affichage(grid)
 
main()