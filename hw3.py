#Purpose:The function should take in a positive integer for the weight of a dog and give it a sound based on the weight.
#Input parameters: Positive values for weight of a dog
#Return value: it returns one of the four options for the sound the dog makes, 'yip','ruff', 'bark', and 'boof'
def sound(weight): 
    if weight <= 13 and weight >= 0:
        return str('Yip')
    elif weight >= 13 and weight <= 30:
        return str('Ruff')
    elif weight >= 31 and weight <= 70:
        return str('Bark')
    else:
        return str('Boof')

#Purpose: This function is a text adventure which takes user input out of the three options provided.
#input parameters: values 1,2, or 3
#Return value: invalid option or a one character string which represents the user input
        
def choice():
    x = 0
    while x != 4:
        if x == 0:
            print('What to do if you are stuck on a homework problem')
            print('1.Go to office hours')
            print('2.Send an email to the TA')
            print('3.Watch Khan academy videos')
            selection = input("Choose 1,2, or 3: ")
            if selection in ['1','2','3']:
                x = int(selection)
            else:
                print('Invalid option!')
            return str(x)

#purpose: text adventure game where the sequence of events depends on user input
#input parameters: integers 1,2, or 3
#Return value : boolean true or false depending on user choice
def adventure():
    x = 0 
    print('Welcome to the text game adventure!')
    while x != 3:
        if x == 0:
            print('option 1')
            print('option 2')
            print('option 3')
            selection = input("Choose 1,2, or 3: ")
            if selection in ['1','2','3']:
                x = int(selection)
            else:
                return False
            #print('des')
        if x == 1:
            return False
        elif x == 3:
            print('good')
            print('1.')
            print('2.')
            print('3.')
            selection = input("Choose 1,2, or 3: ")
            if x == 1:
                return False
            if x == 3:
                print('p')
            if x == 2:
                print('good choice')
        
         
def adventures():
    state = 0
    print('Welcome to the text game adventure')
    print('option 1')
    print('option 2')
    print('option 3')
    choice = input("Choose 1,2, or 3: ")
    if choice == '1':
        return False
    if choice == '3':
        state = 3
    print('option 1')
    print('option 2')
    print('option 3')
    choice = input("Choose 1,2, or 3: ")
    print(state)
    if choice == '2':
        state = 2
    if choice == '1':
        return False
    if choice == '3':
        state == '5'
    #if choice == '2':
     #   state = 2
        return True
    if choice == '1':
        return False 
   

                  
        
        
