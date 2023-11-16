import time
import sys
import signal
from colorama import Fore, Back, Style

global grid

class Errorvaleur(Exception):
    pass

def gestionnaire_signal(signal,frame):
    print(Fore.LIGHTMAGENTA_EX +"\nVous allez quitter le programme" )
    time.sleep(2)
    sys.exit(0)
def gestionnaire_signal_ctrl_z(signal,frame):
    print(Fore.WHITE + "\t")
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 'b':
                grid[i][j]= 'h'
    affichage(grid)

    
signal.signal(2,gestionnaire_signal)
signal.signal(signal.SIGTSTP, gestionnaire_signal_ctrl_z)

def affichage(A):
    a = ''
    h = 1
    for b in range(ord('A'),ord('I')):
        grid[0][h] = chr(b)
        h+= 1
    for i in range(9):
        for j in range(9):
            if i == 0 and j == 0 :
                a = '  |'
                grid[i][j] = ' '
            elif i == 0 and j != 0:
                a += ' ' + grid[i][j] + ' |'
            elif j == 0 and i != 0:
                a += str(i) + ' |'
                grid[i][j] = str(i)
            elif A[i][j] == 'b':
                a += '⛵ |'
            elif A[i][j] == '':
                a += '🌊 |'
            elif A[i][j] == 'h':
                a += '💥 |'
            elif A[i][j] == 'm':
                a += '💦 |'
            a += ' '
        a += '\n'
    print(Fore.WHITE + a)

def askSendMissile(rowIndex, columnIndex):
    
    if grid[rowIndex][columnIndex] == 'b':
        grid[rowIndex][columnIndex] = 'h'
        return True
    elif grid[rowIndex][columnIndex] == '':
        grid[rowIndex][columnIndex] = 'm'
        return False
    else:
        print(Fore.WHITE + "La case a déjà été touchée")
        return False

def isGameOver():
    for i in range(1,9):
        for j in range(1,9):
            if grid[i][j]== 'b':
                return False
    return True

def input_value():
    a = [0,0]
    x,y =0,0
    while True :
        try :
            print(Fore.LIGHTCYAN_EX + "Donnez des cohordonnées pour tirer X,Y séparé par un espace :  X Y")
            try :
                x,y = input().split()
                x = int(x)
                y = int(y)
            except :
                print("valeur de x, y erronés")
            if x < 0 or x > 9 :
                raise Errorvaleur("la valeur de x est mauvaise")
            if y < 0 or y > 9 :
                raise Errorvaleur("La valeur de y est mauvaise")
            a[0] = y
            a[1] = x
            return a
        except Errorvaleur as e:
            print(Fore.LIGHTRED_EX+f"Erreur de valeur : {e}")

def main():
    a = [0,0]
    global grid
    condition = True
    condition_exeption = True
    grid = [['' for _ in range(9)] for _ in range(9)]

    grid[1][1] = 'b'
    grid[1][2] = 'b'
    grid[1][3] = 'b'

    grid[3][2] = 'b'
    grid[3][3] = 'b'

    grid[7][5] = 'b'
    grid[6][5] = 'b'
    grid[5][5] = 'b'
    grid[4][5] = 'b'

    while (isGameOver() == False):
        try :
            affichage(grid)
            a = input_value() 
            askSendMissile(a[0],a[1])
        except KeyboardInterrupt :
            sys.exit(0)

main()
