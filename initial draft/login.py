import os
import display
import write

def login():
    loginloop = True
    while loginloop:
        display.clear()
        print('┌────────────────────────────────────────────LOGIN─┐')
        print('│username:\t%-35.35s│'%(' <'))
        print('│password:\t%-35.35s│'%(''))
        print('└──────────────────────────────────────────────────┘')
        mainUser = input('> ')
        display.clear()
        print('┌────────────────────────────────────────────LOGIN─┐')
        print('│username:\t%-35.35s│'%(mainUser))
        print('│password:\t%-35.35s│'%(' <'))
        print('└──────────────────────────────────────────────────┘')
        mainPass = input('> ')
        display.clear()
        print('┌────────────────────────────────────────────LOGIN─┐')
        print('│username:\t%-35.35s│'%(mainUser))
        print('│password:\t%-35.35s│'%(mainPass))
        print('└──────────────────────────────────────────────────┘')

        if (mainUser.isspace() or mainPass.isspace()) or (mainUser=='' or mainPass==''):
            print('┌────────────────────────────────────────────ERROR─┐')
            print('│Incomplete credentials entered.                   │')
            print('└──────────────────────────────────────────────────┘')
            display.pause()
            display.clear()
            continue

        try:
            # check if save exists
            with open(f'{mainUser}.txt','x') as f:
                pass
            print('┌──────────────────────────────────────────────────┐')
            print('│This user does not exist. [R] to register.        │')
            print('└──────────────────────────────────────────────────┘')
            choice = input('> ')
            
            # choice to save or not
            with open(f'{mainUser}.txt','w') as f:
                if choice in ['R','r']:
                    f.writelines(mainPass)
                    return mainUser, mainPass
                else:
                    f.close()
                    os.remove(f'{mainUser}.txt')
        except FileExistsError:
            # if save actually exists, check if password matches
            with open(f'{mainUser}.txt','r') as f:
                if (f.readline()).strip() != mainPass:
                    print('┌───────────────────────────────────────────────┐')
                    print('│User exists but password is wrong.             │')
                    print('└───────────────────────────────────────────────┘')
                else:
                    return mainUser, mainPass

        display.pause()
        display.clear()
