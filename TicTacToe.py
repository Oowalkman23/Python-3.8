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

        row = rd.randint(0,2)
        column = rd.randint(0,2)

        if pval == board[row][column] or bval == board[row][column]:
            continue
        else:
            break
    
    board[row][column] = bval

def checkWin(pval, bval):

    # 3 win conditions with 8 total possibility 
    win_condition = []

    cond_1 = []
    for i in range(3):
        cond_1.append(''.join(board[i]))

    cond_2 = []
    for i in range(3):
        win2 = ''.join([board[x][i] for x in range(3)])
        cond_2.append(win2)

    cond_3 = []
    cond_3.append(''.join([board[x][x] for x in range(3)]))
    cond_3.append(''.join([board[0][2], board[1][1], board[2][0]]))

    win_condition.extend(cond_1 + cond_2 + cond_3)

    if pval*3 in win_condition:
        return 0
    elif bval*3 in win_condition:
        return 1
    else:
        return 2

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

        global board
        board = [['?','?','?'],['?','?','?'],['?','?','?']]

        while True:
            
            #Looping for the main game
            print('\nBoard\nYou Play =', you.val, '\n')
            for i in range(3):
                for j in range(3):
                    print(board[i][j], end='')
                print()
            
            print()
            
            #Turn
            if you.pl == 1:
                playPlayer(you.val, bot.val)
                you.pl += 1
            else:
                playBot(you.val, bot.val)
                you.pl -= 1
            
            #Check win condition
            result = checkWin(you.val, bot.val)

            if result in [0,1]:                
                break
            else:
                continue
        
        if result == 0:
            print('\nYou win!')
            for i in range(3):
                for j in range(3):
                    print(board[i][j], end='')
                print()

        else:
            print('\nYou lose the game..')
        
        #Choice for another game
        while True:
            try:
                choice = input('\nWould you like another game? (y/n) ').upper()
            except ValueError:
                print('Invalid choice input!')
                continue
            else:
                if choice == 'Y':
                    break
                elif choice == 'N':
                    print('Exiting program..')
                    play -= 1
                    break
                else:
                    print('Invalid choice input!')

main()       
        
        





    