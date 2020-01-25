
def add_contact():      #Func to add contact
     
    cont_name = input('\nInput name = ')
    number_List = ''    #Initial to store phone number
    loop = 1            #Loop condition 1st
        
    while loop == 1:
        
        #Valiate phone number input
        try:
            cont_num = int(input('\nInput phone number, one at a time = '))
        except ValueError:
            print('\nInvalid input!')
            continue
        else:
            number_List += str(cont_num)    #Storing phone number

        if len(number_List) >= 10:

            loop2 = 1       
            while loop2 == 1:       #Loop condition 2nd
                choice2 = input('\nAlready past 10 numbers, would you like to input again? (y/n) = ').upper()
            
                if choice2 == 'Y':      #1st Loop repeat condition
                    loop2 = 0
                    continue
                
                elif choice2 == 'N':    #Exit function
                    loop2 = 0
                    loop -= 1   #Exit parameter 1st loop

                else:
                    print('\nInvalid choice input!')
                    continue
                
        global contact_data     #contact_data used in main() func
        contact_data = [cont_name, number_List]               
                       
def delete_contact(target_name):

    found = 0   #Initial found parameter

    if len(contact_database) == 0:
        print('\nPhonebook is empty!')

    else:
        #Searching process
        for i in range(len(contact_database)):
            if (contact_database[i][0]).upper() == target_name.upper():
                del contact_database[i]
                found += 1
                print('\nContact successfully deleted.')
        if found == 0:
            print('\nContact not found!')

def showContact():  #Print current phonebook

    if len(contact_database) == 0:
        print('\nPhonebook is empty!')
        
    else:
        for i in range(len(contact_database)):
            print(contact_database[i][0], ':', contact_database[i][1])
    
        
def main():
    global contact_database     #The temporary phonebook 
    contact_database = []

    while True:
        print('''
WELCOME TO PHONE BOOK MINI PROGRAM
===================================
Press 1 to - Add contact
Press 2 to - Delete contact
Press 3 to - Show contact list
Press 4 to - Exit the program\n
            ''')
        try:
            choice = int(input('Your choice = '))
        except ValueError:
            print('\nInvalid input!')
            continue

        if choice == 1:
            add_contact()
            contact_database.append(contact_data)            
            continue

        elif choice == 2:
            target_name = input('\nInput name in contact you want to delete = ')
            delete_contact(target_name)
            continue

        elif choice == 3:
            showContact()
            continue

        elif choice == 4:

            if len(contact_database) > 0:   #Create files .txt storing phonebook before exiting program.
                with open('D:\Phonebook.txt','w') as f1:
                    for i in range(len(contact_database)):
                        f1.write(contact_database[i][0] + ' : ' + contact_database[i][1] + '\n')
                    f1.close()

            print('\nExiting program...')
            break

        else:
            print('\nInvalid input!')
            continue

main()




        

