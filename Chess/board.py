class gameBoard():
    def __init__(self):
        self.board = [['c','r','b','Q','K','b','r','c'],['p','p','p','p','p','p','p','p'],[' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' '],['p','p','p','p','p','p','p','p'],['c','r','b','Q','K','b','r','c']]
        self.mask = [[2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2],[0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]

    def printScreen(self):
        for i in range(7, -1, -1):
            for j in range(8):
                if self.mask[i][j] == 2:
                    print('\x1b[34m' + self.board[i][j]+'  ', end='')
                if self.mask[i][j] == 1:
                    print('\x1b[31m' + self.board[i][j]+'  ', end='')
                if self.mask[i][j] == 0:
                    print('\x1b[37m' + '_'+'  ', end='')
            print('\x1b[37m' + '\n')

    def letterToNumber(self, start):
        #print(start)
        match start:
            case 'a':
                return -1
            case 'b':
                return 1
            case 'c':
                return 2
            case 'd':
                return 3
            case 'e':
                return 4
            case 'f':
                return 5
            case 'g':
                return 6
            case 'h':
                return 7
            case _:
                return False

    def move(self, start, finish):
            self.mask[finish[0]][finish[1]] = self.mask[start[0]][start[1]]
            self.board[finish[0]][finish[1]] = self.board[start[0]][start[1]]
            self.mask[start[0]][start[1]] = 0
            self.board[start[0]][start[1]] = '_'

    def proccessMove(self, move, player):
        #verify format ex. "a2 to a3"
        if len(move) != 8:
            print('length error')
            return False, 'a'
        move = move.lower()
        #verify starting position in board
        start = move[0:2]

        xStart = self.letterToNumber(start[0:1])
        if xStart == False:
            print('letter to number error')
            return False, 'b'
        if xStart == -1:#returning 0 qualifies as false
            xStart = 0
        
        yStart = (eval(move[1:2]) - 1)
        if yStart > 7 or yStart < 0:
            return False, 'c'
        #verify ending position in board
        end = move[6:8]
        
        if start == end:
            return False, 'd'
        
        xEnd = self.letterToNumber(end[0:1])
        if xEnd == False:
            print('letter to number error part 2')
            return False, 'e'
        if xEnd == -1:
            xEnd = 0
        
        yEnd = (eval(end[1:2]) - 1)
        if yEnd > 7 or yEnd < 0:
            return False, 'f'
        #verify moving correct peice
        if not ((self.mask[yStart][xStart] == 1 and player == False) or (self.mask[yStart][xStart] == 2 and player == True)):
            return False, 'g' #1=False, 2 = True
        #destination detection
        if self.mask[yStart][xStart] == self.mask[yEnd][xEnd]:
            print('same team error')
            return False, 'i'
        #verify peice ability
        peice = self.board[yStart][xStart]
        
        if peice == 'p':
            #if pawn not moved
            #print(yStart, player, self.mask[yStart + 1][xStart], self.mask[yEnd][xEnd])
            if (yStart == 1 and player == True):
                if not (yEnd == 2 or yEnd == 3):
                    return False, '1'
                if (yEnd == 3 and xEnd != xStart):
                    return False, '2'
                if (yEnd == 3 and (self.mask[yStart + 1][xStart] != 0 or self.mask[yEnd][xEnd] != 0)):
                    return False, '3'
                elif xStart == xEnd:
                    self.move([yStart,xStart], [yEnd, xEnd])
                    return True
            if (yStart == 6 and player == False):
                if not (yEnd == 5 or yEnd == 4):
                    return False, '4'
                if (yEnd == 4 and xEnd != xStart):
                    return False, '5'
                if (yEnd == 4 and (self.mask[yStart - 1][xStart] != 0 or self.mask[yEnd][xEnd] != 0)):
                    return False, '6'
                elif xEnd == xStart:
                    self.move([yStart,xStart], [yEnd, xEnd])
                    return True
            #pawn moved
            if (yStart != 1 and player == False and yEnd != yStart - 1):
                return False, '7'
            if (yStart != 6 and player == True and yEnd != yStart + 1):
                return False, '8'
            if (xStart == xEnd and self.mask[yEnd][xEnd] == 0):
                self.move([yStart,xStart], [yEnd, xEnd])
                return True
            if ((xEnd == xStart + 1 or xEnd == xStart - 1) and self.mask[yEnd][xEnd] != 0):
                self.move([yStart,xStart], [yEnd, xEnd])
                return True
        if peice == 'K':
            if (xStart == xEnd + 1 or xStart == xEnd - 1 or xStart == xEnd) and (yStart == yEnd + 1 or yStart == yEnd - 1 or yStart == yEnd):
                self.move([yStart,xStart], [yEnd, xEnd])
                return True
            else: 
                #print(xStart, xEnd, yStart, yEnd)
                return False
        if peice == 'r':
            if yEnd == yStart + 1 and (xEnd == xStart + 2 or xEnd == xStart - 2):
                self.move([yStart,xStart], [yEnd, xEnd])
                return True
            if yEnd == yStart + 2 and (xEnd == xStart + 1 or xEnd == xStart - 1):
                self.move([yStart,xStart], [yEnd, xEnd])
                return True
            if yEnd == yStart -2 and (xEnd == xStart + 1 or xEnd == xStart - 1):
                self.move([yStart,xStart], [yEnd, xEnd])
                return True
            if yEnd == yStart - 1 and (xEnd == xStart + 2 or xEnd == xStart - 2):
                self.move([yStart,xStart], [yEnd, xEnd])
                return True
        if peice == 'c':
            #print('call to c')
            if xStart != xEnd and yStart != yEnd:
                return False
            if xStart != xEnd:
                #print('call to delta x')
                #temp = 0
                if xStart < xEnd:
                    #temp = 1
                    for i in range(xStart+1, xEnd, 1):
                        if self.mask[yStart][i] != 0:
                            return False, '10'
                    self.move([yStart,xStart], [yEnd, xEnd])
                    return True
                if xStart > xEnd:
                    for i in range(xStart-1, xEnd, -1):
                        if self.mask[yStart][i] != 0:
                            return False, '11'
                    self.move([yStart,xStart], [yEnd, xEnd])
                    return True
            if yStart != yEnd:
                #print('call to delta y')
                if yStart < yEnd:
                    for i in range(yStart+1, yEnd, 1):
                        if self.mask[i][xStart] != 0:
                            print(self.mask[xStart][i])
                            return False, '12'
                    self.move([yStart,xStart], [yEnd, xEnd])
                    return True
                if yStart > yEnd:
                    for i in range(yStart-1, yEnd, -1):
                        if self.mask[i][xStart] != 0:
                            return False, '13'
                    self.move([yStart,xStart], [yEnd, xEnd])
                    return True
        if peice == 'b':
            if abs(xEnd - xStart) != abs(yEnd - yStart):
                return False, '13'
            if yEnd - yStart > 0:
                if xEnd - xStart > 0:
                    for i in range(xEnd - xStart - 1):
                        #print(yStart+i+1, xStart+i+1)
                        if self.mask[yStart+i+1][xStart+i+1] != 0:
                            return False
                    self.move([yStart,xStart], [yEnd, xEnd])
                    return True
                if xEnd - xStart < 0:
                    for i in range(xStart-1, xEnd, -1):
                        #print(yStart+xStart-i, i)
                        if self.mask[yStart+xStart-i][i] != 0:
                            return False
                    self.move([yStart,xStart], [yEnd, xEnd])
                    return True
            if yEnd - yStart < 0:
                #print('call to -delta y')
                if xEnd - xStart > 0:
                    #print('call to +delta x', 0 - (yEnd - yStart))
                    for i in range(0 - (yEnd - yStart)):
                        #print(yStart - i - 1, xStart + i + 1)
                        if self.mask[yStart-i-1][xStart+i+1] != 0:
                            return False, '14'
                    self.move([yStart,xStart], [yEnd, xEnd])
                    return True
                if xEnd - xStart < 0:
                    for i in range(0 - (yEnd - yStart)):
                        #print(yStart-i-1, xStart-i-1, self.mask[yStart-i-1][xStart-i-1])
                        if self.mask[yStart-i-1][xStart-i-1] != 0:
                            return False, '15'
                    self.move([yStart,xStart], [yEnd, xEnd])
                    return True
        if peice == 'Q':
            if xStart == xEnd or yStart == yEnd:#Castle code
                if xStart != xEnd:
                #print('call to delta x')
                #temp = 0
                    if xStart < xEnd:
                        #temp = 1
                        for i in range(xStart+1, xEnd, 1):
                            if self.mask[yStart][i] != 0:
                                return False, '10'
                        self.move([yStart,xStart], [yEnd, xEnd])
                        return True
                    if xStart > xEnd:
                        for i in range(xStart-1, xEnd, -1):
                            if self.mask[yStart][i] != 0:
                                return False, '11'
                        self.move([yStart,xStart], [yEnd, xEnd])
                        return True
                if yStart != yEnd:
                    #print('call to delta y')
                    if yStart < yEnd:
                        for i in range(yStart+1, yEnd, 1):
                            if self.mask[i][xStart] != 0:
                                print(self.mask[xStart][i])
                                return False, '12'
                        self.move([yStart,xStart], [yEnd, xEnd])
                        return True
                    if yStart > yEnd:
                        for i in range(yStart-1, yEnd, -1):
                            if self.mask[i][xStart] != 0:
                                return False, '13'
                        self.move([yStart,xStart], [yEnd, xEnd])
                        return True
            elif abs(xEnd - xStart) == abs(yEnd - yStart):#bishop code
                if yEnd - yStart > 0:
                    if xEnd - xStart > 0:
                        for i in range(xEnd - xStart - 1):
                            #print(yStart+i+1, xStart+i+1)
                            if self.mask[yStart+i+1][xStart+i+1] != 0:
                                return False
                        self.move([yStart,xStart], [yEnd, xEnd])
                        return True
                    if xEnd - xStart < 0:
                        for i in range(xStart-1, xEnd, -1):
                            #print(yStart+xStart-i, i)
                            if self.mask[yStart+xStart-i][i] != 0:
                                return False
                        self.move([yStart,xStart], [yEnd, xEnd])
                        return True
                if yEnd - yStart < 0:
                    #print('call to -delta y')
                    if xEnd - xStart > 0:
                        #print('call to +delta x', 0 - (yEnd - yStart))
                        for i in range(0 - (yEnd - yStart)):
                            #print(yStart - i - 1, xStart + i + 1)
                            if self.mask[yStart-i-1][xStart+i+1] != 0:
                                return False, '14'
                        self.move([yStart,xStart], [yEnd, xEnd])
                        return True
                    if xEnd - xStart < 0:
                        for i in range(0 - (yEnd - yStart)):
                            #print(yStart-i-1, xStart-i-1, self.mask[yStart-i-1][xStart-i-1])
                            if self.mask[yStart-i-1][xStart-i-1] != 0:
                                return False, '15'
                        self.move([yStart,xStart], [yEnd, xEnd])
                        return True
            else:
                return False

if __name__ == "__main__":
    game = gameBoard()
    #game.printScreen()
    #game.move([0,1],[4,2])
    game.printScreen()
    
    print(game.proccessMove('d7 to d5', False))
    print(game.proccessMove('c8 to h3', False))
    #print(game.proccessMove('e2 to a6', True))
   
    #print(game.proccessMove('d3 to d4', True))
    #game.move([6,1], [5,1])
    
    game.printScreen()
    print(game.mask)