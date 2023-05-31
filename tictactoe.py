#autor: Sebastian Gąciarz
import os
import random

def printWhite(data):
    print("\033[0m" + data, end="")

def printRed(data):
    print("\033[31m" + data, end="")

def printGreen(data):
    print("\033[32m" + data, end="")

def screenXO(screen):
    os.system('cls')

    
    corners = {
               "upperLeft":     "┌",    
               "upperRight":    "┐",    
               "mediumLeft":    "├",    
               "mediumRight":   "┤",    
               "bottomLeft":    "└",    
               "bottomRight":   "┘",    
               "upperMid":      "┬",    
               "midiumMid":     "┼",    
               "bottomMid":     "┴"     
              }
    lines =   {
               "vertical": "│",         
               "horizontal": "─"        
              }
    
    size = len(screen)                  

    verticalLine = [lines["horizontal"]*3]*size         
    
    
    verticalUp = corners["upperMid"].join(verticalLine)
    verticalMid = corners["midiumMid"].join(verticalLine)
    verticalDown = corners["bottomMid"].join(verticalLine)

   

    printWhite(corners["upperLeft"]+verticalUp+corners["upperRight"]+"\n")
 
    for i,row in enumerate(screen):
        printWhite(lines["vertical"])
        for j in row:
            if(j>0): printGreen(" X ")
            elif j<0: printRed(" O ")
            else: printWhite("   ")
            printWhite(lines["vertical"])            
        print()
        if(i < size-1): printWhite(corners["mediumLeft"]+verticalMid+corners["mediumRight"]+"\n")

    printWhite(corners["bottomLeft"]+verticalDown+corners["bottomRight"]+"\n")

def checkWin(screen):
    for i in range(len(screen)):
        row = screen[i]
        if row.count(row[0]) == len(row) and row[0] != 0:
            return row[0]

    for i in range(len(screen)):
        if screen[0][i] == screen[1][i] == screen[2][i] and screen[0][i] != 0:
            return screen[0][i]

    if screen[0][0] == screen[1][1] == screen[2][2] and screen[0][0] != 0:
        return screen[0][0]

    if screen[0][2] == screen[1][1] == screen[2][0] and screen[0][2] != 0:
        return screen[0][2]

    return 0

def checkDraw(dane):
    for row in dane:
        for cell in row:
            if cell == 0:
                return False
    return True

def computerMove(screen):
    empty = []
    for i in range(3):
        for j in range(3):
            if screen[i][j] == 0:
                empty.append((i, j))
    while True:
        x, y = random.choice(empty)
        if screen[y][x] == 0:
            break
    return x, y

if __name__ == "__main__":

    rozmiar = 3
    dane = []
    for i in range(rozmiar):
        kolumna = [0 for i in range(rozmiar)]
        dane.append(kolumna)

    gracz = 1
    while True:
        screenXO(dane)
        if gracz == 1:
            printGreen("Gracz 1\n")
            while True:
                try: 
                    x = int(input("Podaj wsp x: "))
                    y = int(input("Podaj wsp y: "))
                    if x >= 0 and x < rozmiar and y >= 0 and y < rozmiar:
                        if dane[y][x] == 0:
                            dane[y][x] = gracz
                            break
                        else:
                            print("To pole jest już zajęte, wybierz inne.")
                    else:
                            print("Podane współrzędne wykraczają poza zakres tablicy.")
                except:
                    print("Podaj liczbę!")           
        else:
            printRed("Komputer\n")
            x, y = computerMove(dane)
            dane[y][x] = gracz
            input("Naciśnij Enter aby kontynuować...")

        if checkWin(dane):
            screenXO(dane)
            if gracz == 1:
                printGreen("Gracz 1 wygrał!")
            else:
                printRed("Komputer wygrał!")
            break

        if checkDraw(dane):
            screenXO(dane)
            print("Remis!")
            break

        gracz *= -1
