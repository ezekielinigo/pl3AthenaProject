import login # handles creation of saved txt
import inputinfo # input credentials
import edit
import display
import write
import os
import generate

dir={}
mainUser, mainPass = login.login()
dir = write.load(mainUser)
display.clear()

mainloop=True
while mainloop:
    # display menu
    display.menu()
    print('┌────────────────────────────────SAVED CREDENTIALS─┐')
    if bool(dir) == False:
        print('│%-50.50s│'%('No saved credentials yet.'))
    else:
        for key, value in dir.items():
            print('│%-50.50s│'%(f'{key}:'))
            print('│\tusername:\t%-27.27s│'%(value[0]))
            print('│\tpassword:\t%-27.27s│'%(len(value[1])*'∙'))
            print('│\thint:\t\t%-27.27s│'%(value[2]))
            display.strength(value[3])
            print('│%-50.50s│'%(''))
    print('└──────────────────────────────────────────────────┘')
    choice=input('> ')
    display.clear()

    try:
        if choice in ['E','e']: # exit program
            print('┌──────────────────────────────────────────CONFIRM─┐')
            print('│[S] save to file and quit.                        │')
            print('│[Q] quit without saving.                          │')
            print('│[C] cancel and go back to menu.                   │')
            print('└──────────────────────────────────────────────────┘')
            choice=input('> ')

            if choice in ['S','s']:
                write.save(mainUser,mainPass,dir)
                mainloop=False
            elif choice in ['Q','q']:
                mainloop=False

        elif choice in ['A','a']: # input credential
            inputinfo.inputinfo(dir)
        elif choice in dir: # unhide password
            edit.edit(choice,dir)
        elif choice[0]=='!' and choice[1:] in dir:
            display.menu()
            print('┌────────────────────────────────SAVED CREDENTIALS─┐')
            for key, value in dir.items():
                print('│%-50.50s│'%(f'{key}:'))
                print('│\tusername:\t%-27.27s│'%(value[0]))
                if key==choice[1:]: # only unhide the chosen key
                    print('│\tpassword:\t%-27.27s│'%(value[1]))
                    generate.copy(value[1])
                else:
                    print('│\tpassword:\t%-27.27s│'%(len(value[1])*'∙'))
                print('│\thint:\t\t%-27.27s│'%(value[2]))
                display.strength(value[3])
                print('│%-50.50s│'%(''))
            print('└──────────────────────────────────────────────────┘')
            print('┌──────────────────────────────────────────────────┐')
            print('│Password copied to clipboard.                     │')
            print('└──────────────────────────────────────────────────┘')
            display.pause()
        elif choice.lower() == 'delete':
            display.clear()
            print('┌──────────────────────────────────────────WARNING─┐')
            print('│Are you sure you want to delete your profile?     │')
            print('│All info will be lost.                            │')
            print('│Enter your password to continue.                  │')
            print('└──────────────────────────────────────────────────┘')
            choice=input('> ')
            if choice==mainPass:
                os.remove(f'{mainUser}.txt')
                print('Profile deleted and the program will now exit.')
                display.pause()
                mainloop=False
    except:
        continue
    display.clear()
