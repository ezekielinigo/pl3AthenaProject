import display
import checkStrength
import generate

def edit(key,dir):
    editLoop=True
    edited=False
    flag='─EDIT'
    while editLoop:
        if edited==True:
            flag='EDIT*'
        temp=dir
        print(f'┌────────────────────────────────────────────{flag}─┐')
        print('│%-50.50s│'%(f'{key}:'))
        print('│\tusername:\t%-27.27s│'%(temp[key][0]))
        print('│\tpassword:\t%-27.27s│'%(temp[key][1]))
        print('│\thint:\t\t%-27.27s│'%(temp[key][2]))
        display.strength(temp[key][3])
        print('│%-50.50s│'%(''))
        print('└──────────────────────────────────────────────────┘')
        print('┌──────────────────────────────────────────ACTIONS─┐')
        print('│%-50.50s│\n│%-50.50s│\n│%-50.50s│\n│%-50.50s│\n│%-50.50s│\n│%-50.50s│'%(
        '[U] sername','[P] assword','[H] int','[G] enerate Password','[D] elete','[S] ave & Exit'))
        print('└──────────────────────────────────────────────────┘')
        choice=input('> ')
        display.clear()

        if choice in ['U','u']:
            print('┌─────────────────────────────────────────────EDIT─┐')
            print('│%-50.50s│'%(f'{key}:'))
            print('│\tusername:\t%-27.27s│'%('<'))
            print('│\tpassword:\t%-27.27s│'%(temp[key][1]))
            print('│\thint:\t\t%-27.27s│'%(temp[key][2]))
            display.strength(temp[key][3])
            print('│%-50.50s│'%(''))
            print('└──────────────────────────────────────────────────┘')
            tempUser=input('> ')
            if len(tempUser)>27:
                print('┌────────────────────────────────────────────ERROR─┐')
                print('│Max characters for credentials reached (27).      │')
                print('└──────────────────────────────────────────────────┘')
            else:
                temp[key][0]=tempUser
                edited=True

        elif choice in ['P','p']:
            print('┌─────────────────────────────────────────────EDIT─┐')
            print('│%-50.50s│'%(f'{key}:'))
            print('│\tusername:\t%-27.27s│'%(temp[key][0]))
            print('│\tpassword:\t%-27.27s│'%('<'))
            print('│\thint:\t\t%-27.27s│'%(temp[key][2]))
            display.strength(temp[key][3])
            print('│%-50.50s│'%(''))
            print('└──────────────────────────────────────────────────┘')
            tempPass=input('> ')
            if len(tempPass)>27:
                print('┌────────────────────────────────────────────ERROR─┐')
                print('│Max characters for credentials reached (27).      │')
                print('└──────────────────────────────────────────────────┘')
            elif ' ' in tempPass:
                print('┌────────────────────────────────────────────ERROR─┐')
                print('│Password cannot contain spaces.                   │')
                print('└──────────────────────────────────────────────────┘')
                display.pause()
            else:
                points,reqs=checkStrength.password_check(tempPass)
                display.errors(points,reqs)
                print('┌──────────────────────────────────────────CONFIRM─┐')
                print('│[C] confirm password.                             │')
                print('└──────────────────────────────────────────────────┘')
                choice=input('> ')
                if choice in ['C','c']:
                    temp[key][1]=tempPass
                    temp[key][3]=points
                    edited=True
    
        elif choice in ['H','h']:
            print('┌─────────────────────────────────────────────EDIT─┐')
            print('│%-50.50s│'%(f'{key}:'))
            print('│\tusername:\t%-27.27s│'%(temp[key][0]))
            print('│\tpassword:\t%-27.27s│'%(temp[key][1]))
            print('│\thint:\t\t%-27.27s│'%('<'))
            display.strength(temp[key][3])
            print('│%-50.50s│'%(''))
            print('└──────────────────────────────────────────────────┘')
            temp[key][2]=input('> ')
            edited=True

        elif choice in ['G','g']:
            tempPass=generate.generate()
            print(f'┌─────────────────────────────────────────────EDIT─┐')
            print('│%-50.50s│'%(f'{key}:'))
            print('│\tusername:\t%-27.27s│'%(temp[key][0]))
            print('│\tpassword:\t%-27.27s│'%(tempPass))
            print('│\thint:\t\t%-27.27s│'%(temp[key][2]))
            display.strength(36)
            print('│%-50.50s│'%(''))
            print('└──────────────────────────────────────────────────┘')
            print('┌──────────────────────────────────────────CONFIRM─┐')
            print('│Password randomized. [C] to confirm.              │')
            print('└──────────────────────────────────────────────────┘')
            choice=input('> ')
            if choice in ['C','c']:
                temp[key][1]=tempPass
                temp[key][3]=36
                edited=True

        elif choice in ['D','d']:
            print('┌──────────────────────────────────────────CONFIRM─┐')
            print('│[C] confirm deletion.                             │')
            print('└──────────────────────────────────────────────────┘')
            confirm=input('> ')
            if confirm in ['C','c']:
                del dir[key]
                editLoop=False

        elif choice in ['S','s']:
            if edited==True:
                print(f'┌────────────────────────────────────────────{flag}─┐')
                print('│%-50.50s│'%(f'{key}:'))
                print('│\tusername:\t%-27.27s│'%(temp[key][0]))
                print('│\tpassword:\t%-27.27s│'%(temp[key][1]))
                print('│\thint:\t\t%-27.27s│'%(temp[key][2]))
                display.strength(temp[key][3])
                print('│%-50.50s│'%(''))
                print('└──────────────────────────────────────────────────┘')
                print('┌──────────────────────────────────────────CONFIRM─┐')
                print('│[C] confirm changes.                              │')
                print('└──────────────────────────────────────────────────┘')
                choice=input('> ')
                if choice in ['C','c']:
                    dir.update({key:[temp[key][0],temp[key][1],temp[key][2],temp[key][3]]})
                    display.clear()
                editLoop=False
            else:
                editLoop=False

        display.clear()