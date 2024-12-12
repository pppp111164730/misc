from board import gameBoard


def Main():
    turn = True
    game = gameBoard()
    running = True
    x = ''
    while running:
        game.printScreen()
        if turn:
            x = input('\x1b[34m')
        else: 
            x = input('\x1b[31m')
        if x == 'quit':
            running = False
            break
        if game.proccessMove(x, turn) == True:
           turn = not turn
Main()