import re
import display
import checkStrength
import generate

def inputinfo(dir):

    # actual input part
    inputloop=True
    while inputloop:
        print('┌────────────────────────────────────────────INPUT─┐')
        print('│%-50.50s│'%('name: <'))
        print('│\tusername:\t%-27.27s│'%(''))
        print('│\tpassword:\t%-27.27s│'%(''))
        print('│\thint:\t\t%-27.27s│'%(''))
        print('└──────────────────────────────────────────────────┘')
        key=input('> ')
        if key.isdigit()==True:
            print('┌────────────────────────────────────────────ERROR─┐')
            print('│Please enter a non-digit name.                    │')
            print('└──────────────────────────────────────────────────┘')
            display.pause()
        elif re.search(r"[!#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', key) != None:
            print('┌────────────────────────────────────────────ERROR─┐')
            print('│Please enter a name without special characters.   │')
            print('└──────────────────────────────────────────────────┘')
            display.pause()
        elif key in ['A','a','E','e']:
            print('┌────────────────────────────────────────────ERROR─┐')
            print("│Name cannot be 'A' or 'E.'                        │")
            print('└──────────────────────────────────────────────────┘')
            display.pause()
        else:
            inputloop=False
        display.clear()
    print('┌────────────────────────────────────────────INPUT─┐')
    print('│%-50.50s│'%(f'{key}:'))
    print('│\tusername:\t%-27.27s│'%('<'))
    print('│\tpassword:\t%-27.27s│'%(''))
    print('│\thint:\t\t%-27.27s│'%(''))
    print('└──────────────────────────────────────────────────┘')
    username=input('> ')
    display.clear()
    inputloop=True
    while inputloop:
        print('┌────────────────────────────────────────────INPUT─┐')
        print('│%-50.50s│'%(f'{key}:'))
        print('│\tusername:\t%-27.27s│'%(username))
        print('│\tpassword:\t%-27.27s│'%('< or [G] generate password'))
        print('│\thint:\t\t%-27.27s│'%(''))
        print('└──────────────────────────────────────────────────┘')
        password=input('> ')
        if password in ['G','g']:
            temp=generate.generate()
            print('┌────────────────────────────────────────────INPUT─┐')
            print('│%-50.50s│'%(f'{key}:'))
            print('│\tusername:\t%-27.27s│'%(username))
            print('│\tpassword:\t%-27.27s│'%(f'{temp} <'))
            print('│\thint:\t\t%-27.27s│'%(''))
            print('└──────────────────────────────────────────────────┘')
            print('┌──────────────────────────────────────────CONFIRM─┐')
            print('│Password randomized. [C] to confirm.              │')
            print('└──────────────────────────────────────────────────┘')
            choice=input('> ')
            if choice in ['C','c']:
                password=temp
                generated=True
                inputloop=False
        elif ' ' in password:
            print('┌────────────────────────────────────────────ERROR─┐')
            print('│Password cannot contain spaces.                   │')
            print('└──────────────────────────────────────────────────┘')
            display.pause()
        elif password == key:
            print('┌────────────────────────────────────────────ERROR─┐')
            print('│Password cannot be the same as username.          │')
            print('└──────────────────────────────────────────────────┘')
            display.pause()
        elif password.lower() in ['password','123','abc']:
            print('┌────────────────────────────────────────────ERROR─┐')
            print('│pre seryoso ka ba                                 │')
            print('└──────────────────────────────────────────────────┘')
            display.pause()
        else:
            generated=False
            inputloop=False
        display.clear()
    print('┌────────────────────────────────────────────INPUT─┐')
    print('│%-50.50s│'%(f'{key}:'))
    print('│\tusername:\t%-27.27s│'%(username))
    print('│\tpassword:\t%-27.27s│'%(password))
    print('│\thint:\t\t%-27.27s│'%('<'))
    print('└──────────────────────────────────────────────────┘')
    hint=input('> ')
    display.clear()
    print('┌────────────────────────────────────────────INPUT─┐')
    print('│%-50.50s│'%(f'{key}:'))
    print('│\tusername:\t%-27.27s│'%(username))
    print('│\tpassword:\t%-27.27s│'%(password))
    print('│\thint:\t\t%-27.27s│'%(hint))
    print('└──────────────────────────────────────────────────┘')

    if ((key).isspace() or (username).isspace() or (password).isspace()) == True or (key == '' or username == '' or password == ''):
        print('┌────────────────────────────────────────────ERROR─┐')
        print('│Incomplete credentials entered.                   │')
        print('└──────────────────────────────────────────────────┘')
        display.pause()
    elif len(username)>27 or len(password)>27:
        print('┌────────────────────────────────────────────ERROR─┐')
        print('│Max characters for credentials reached (27).      │')
        print('└──────────────────────────────────────────────────┘')
        display.pause()
    elif key in dir:
        print('┌───────────────────────────────────────OVERWRITE?─┐')
        print('│Entry already exists. [C] to confirm overwrite.   │')
        print('└──────────────────────────────────────────────────┘')
        choice=input('> ')
        if choice in ['C','c']:
            points, reqs = checkStrength.password_check(password)
            dir.update({key:[username,password,hint,points]})
    elif generated==True:
        points=36
    else:
        points, reqs = checkStrength.password_check(password)
    dir.update({key:[username,password,hint,points]})
    display.clear()
