import random as rd

#Assign attribute 'val' for later input
class player:
    def __init__(self, pl=None):
        self.pl = pl
        if pl == 1:
            self.val = 'O'
        else:
            self.val = 'X'

def playPlayer(pval, bval):
    
    #Player turn
    while True:
        try:
            row = int(input('Choose the row for your input (1-3) = '))
            column = int(input('Choose the column for your input (1-3) = '))
    
            if pval == board[row-1][column-1] or bval == board[row-1][column-1]:
                print('Already inputted!')
                continue
            else:
                print('\nInput successful!')
                break
        except IndexError:
            print('Invalid input (out of range)')
            continue
        except ValueError:
            print('Invalid input type!')
            continue
    board[row-1][column-1] = pval            

def playBot(pval, bval):
    #Bot turn
    while True:
        Mid = (1,1)
        Sides = [(0,2), (1,1), (1,2), (2,1)]  
        
        if board[1][1] == '?':
            bot_move = Mid
        elif [board[x][y].count('?') for x in [0,2] for y in [0,2]] == 0:
            bot_move = (rd.randint(0,2), rd.randint(0,2)) 
        else:
            if sum([board[x][y].count(pval) for x in [0,2] for y in [0,2]]) == 0:
                bot_move = (rd.choice([0,2]), rd.choice([0,2])) 
            elif sum([board[x][y].count(pval) for x in [0,2] for y in [0,2]]) == 1:
                bot_move = (rd.choice([0,2]), rd.choice([0,2])) 
            elif sum([board[x][y].count(pval) for x in [0,2] for y in [0,2]]) == 2:
                bot_move = ((rd.choice(Sides))[0], (rd.choice(Sides))[1])            
            else:
                bot_move = (rd.randint(0,2), rd.randint(0,2))       

        if board[bot_move[0]][bot_move[1]] == pval or board[bot_move[0]][bot_move[1]] == bval:
            continue
        else:
            break
    board[bot_move[0]][bot_move[1]] = bval

def checkWin(xval):
    # 3 win conditions with 8 total possibilities     
    win_condition = []
    w1 = [''.join(board[0])]
    w2 = [''.join(board[1])]
    w3 = [''.join(board[2])]
    w4 = [''.join([board[x][0] for x in range(3)])]
    w5 = [''.join([board[x][1] for x in range(3)])]
    w6 = [''.join([board[x][2] for x in range(3)])]
    w7 = [''.join([board[x][x] for x in range(3)])]
    w8 = [''.join([board[0][2], board[1][1], board[2][0]])]
    win_condition.extend(w1+w2+w3+w4+w5+w6+w7+w8)

    if xval*3 in win_condition:
        return True
    else:
        return False

def printBoard():
    for i in range(3):
        for j in range(3):
            print(board[i][j], end='')
        print()            
    print()

def main():
    play = 1

    #Start program
    while play==1:
        print('\nWELCOME TO TIC-TAC-TOE GAME!')
        
        while True:
            try:
                choose_player = int(input('\nAre you player 1 or 2? (ans=1/2) = '))
            except ValueError:
                print('\nInvalid input!')
                continue
            else:
                if choose_player in (1,2):
                    break
                else:
                    print('\nInvalid player input!')
                    continue
        
        #Assign class for player and bot
        you = player(choose_player)
        bot = player(3-choose_player)

        board = [['?','?','?'],['?','?','?'],['?','?','?']]
        result = 0        
        
        while True:            
            #Print board
            print('\nBoard\nYou Play =', you.val, '\n')
            printBoard()
            
            #Turn
            if you.pl == 1:
                playPlayer(you.val, bot.val)
                you.pl += 1
                if checkWin(you.val):
                    result += 1               
                    break   
            else:
                playBot(you.val, bot.val)
                you.pl -= 1
                if checkWin(bot.val):
                    result -= 1               
                    break
                      
            hasil = []
            for i in board:
                hasil.extend(i)
            if '?' not in hasil:
                break
        
        if result == 1:
            print('\nYou win!\n')            
        elif result == -1:
            print('\nYou lose the game..\n')
        else:
            print("\nIt's a tie game!\n")
        
        printBoard()

        #Choice for another game
        while True:
            try:
                choice = input('Would you like another game? (y/n) ').upper()
            except ValueError:
                print('\nInvalid choice input!')
                continue
            else:
                if choice == 'Y':
                    break
                elif choice == 'N':
                    print('\nExiting program..')
                    play -= 1
                    break
                else:
                    print('\nInvalid choice input!')

main()   
