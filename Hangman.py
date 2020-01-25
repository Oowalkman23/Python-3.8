import random

#Database for answers
def get_hero():
    heroes = ['Superman','Ironman','Hulk','Batman','Black Widow','Hawkeye','Captain Marvel','Thor',
              'Captain America', 'Flash', 'Doctor Strange', 'Green Lantern', 'Aquaman', 'Wonder Woman']

    answer = random.choice(heroes).upper()
    
    #Get rid of 'space' being counted in len(answer)
    global num_ans
    num_ans = len(answer)
    if ' ' in answer:
        num_ans -= answer.count(' ')
    
    return answer

#Crosschecking user's guess with answer
def check(hero,guesses,guess):

    status = ''     #Guesses print initial
    matches = 0     #Initial to trigger responses 

    #Guesses print process
    for letter in hero:
        if letter in guesses:
            status += letter
        elif letter == ' ':     #Condition if there's 'space' in answer
            status += ' '
            continue
        else:
            status += '*'       #Print guess with '*'

        if letter == guess:
            matches += 1
    
    #Responses according to matched guesses
    if matches > 1:
        print('\nYes, the hero contains',matches,'"' + guess + '"' + 's')
    elif matches == 1:
        print('\nYes, the hero contains a letter "' + guess + '"')
    else:
        print('\nSorry, the hero does not contain letter "' + guess + '"')

    return status

def main():

    hero = get_hero()       #Grab answer from func get_hero()

    guesses = []            #Database to store guesses
    guessed = False

    print('\nThe hero contains',num_ans,'letters.\n')
    
    while not guessed:

        #Main opening process
        Opening = 'Please enter one letter or a {}-letter word = '.format(num_ans)
        guess = input(Opening)      
        guess = guess.upper()

        #Validate guesses with if eliminations
        if guess in guesses:
            print('\nWhoops! That letter "' + guess + '" already been guessed!\n')

        elif len(guess) == len(hero):   #Condition for guessing with the same number of char as answer
            guesses.append(guess)
            if guess == hero:           #If correct condition
                guessed = True
            else:
                print('Nice try! guess again!')

        elif len(guess) == 1:           #Condition for guessing with a word
            guesses.append(guess)   
            result = check(hero,guesses,guess)  #Calling func check() to review guesses.
            if result == hero:          #If correct condition
                guessed = True
            else:
                print(result)

        else:
            print('\nWrong entry bro, please\n')    #Condition for invalid input

    #Closing statement
    print('\nFinally, the hero is "' + hero + '"! Good job, you guessed it in',len(guesses),'tries!')

    
main()
