import os
def login():
    loginloop = True
    while loginloop:
        print('┌────────────────────────────────────────────LOGIN─┐')
        print('│username:\t%-35.35s│'%(' <'))
        print('│password:\t%-35.35s│'%(''))
        print('└──────────────────────────────────────────────────┘')
        mainUser = input('> ')
        os.system('cls')
        print('┌────────────────────────────────────────────LOGIN─┐')
        print('│username:\t%-35.35s│'%(mainUser))
        print('│password:\t%-35.35s│'%(' <'))
        print('└──────────────────────────────────────────────────┘')
        mainPass = input('> ')
        os.system('cls')
        print('┌────────────────────────────────────────────LOGIN─┐')
        print('│username:\t%-35.35s│'%(mainUser))
        print('│password:\t%-35.35s│'%(mainPass))
        print('└──────────────────────────────────────────────────┘')

        try:
            # check if save exists
            with open(f'{mainUser}.txt','x') as f:
                pass
            print('┌──────────────────────────────────────────────────┐')
            print('│%-50.50s│'%('This user does not exist. (y) to register.'))
            print('└──────────────────────────────────────────────────┘')
            choice = input('> ')
            
            # choice to save or not
            with open(f'{mainUser}.txt','w') as f:
                if choice == 'y':
                    f.writelines(mainPass)
                    loginloop = False
                else:
                    f.close()
                    os.remove(f'{mainUser}.txt')
                    loginloop = True
        except FileExistsError:
            # if save actually exists, check if password matches
            with open(f'{mainUser}.txt','r') as f:
                if f.readline() != mainPass:
                    print('┌───────────────────────────────────────────────┐')
                    print('│%-47.47s│'%('User exists but password is wrong.'))
                    print('└───────────────────────────────────────────────┘')
                    loginloop = True
                else:
                    loginloop = False

        os.system('pause')
        os.system('cls')