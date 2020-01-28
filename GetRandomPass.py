import random as rd, time

#Get password function
def getPass(wrd, wrd_upper, num, sym):
    words = 'abcdefghijklmnoprstuvwxyz'
    words_upper = words.upper()
    numbers = '0123456789'
    symbols = '!@$#%&?'    
    password = []   #Initial list

    #Appending process
    for i in range(wrd):
        password.append(rd.choice(words))
    for i in range(wrd_upper):
        password.append(rd.choice(words_upper))
    for i in range(num):
        password.append(rd.choice(numbers))
    for i in range(sym):
        password.append(rd.choice(symbols))
    #Final password
    return ''.join(rd.sample(password, len(password)))

def main():
    #Start program
    print('\nWELCOME TO RANDOM PASS GEN!')

    while True:
        try:
            digit = int(input('\nHow many digit(s) you want your pass is? (numbers) = '))
        except ValueError:
            print('\nInvalid input (numbers only)!')
            continue
        else:
            #Input digit for each category
            try:
                wrd = int(input('\nNow, how many lower case word? (' + str(digit) + ' words left) = '))
                wrd_upper = int(input('\nRight, how many upper case word? (' + str(digit-wrd) + ' words left) = '))
                num = int(input('\nOkay, how many numbers in it? (' + str(digit-wrd-wrd_upper) + ' words left) = '))
                sym = int(input('\nLastly, how many symbols do you want? (' + str(digit-wrd-wrd_upper-num) + ' words left) = '))
            except ValueError:
                print('\nInvalid input (numbers only)!')
                continue
            #Digit check
            else:
                if wrd+wrd_upper+num+sym > digit:
                    print(f'\nYour wanted {digit} digits, is lower than total of each categories {wrd+wrd_upper+num+sym}!')
                    continue
                elif wrd+wrd_upper+num+sym < digit:
                    print(f'\nYour wanted {digit} digits, is higher than total of each categories {wrd+wrd_upper+num+sym}, rest will be added to symbols')
                    sym += (digit - wrd+wrd_upper+num+sym)
        
        #Call get password function
        password = getPass(wrd,wrd_upper,num,sym)
        
        #Show pass with delay
        print('\nYour password is = ', end='')
        time.sleep(1)
        print(password)
        
        #Another delay
        time.sleep(2)
        choice = input('\nAnother try? (y/n) = ').upper()
        if choice not in ('Y'):
            print('\nExiting program...')
            break

main()




