import os
def inputinfo(dir):

    # actual input part
    inputloop=True
    while inputloop:
        print('┌────────────────────────────────────────────INPUT─┐')
        print('│%-50.50s│'%('key: <'))
        print('│\tusername:\t%-27.27s│'%(''))
        print('│\tpassword:\t%-27.27s│'%(''))
        print('│\thint:\t\t%-27.27s│'%(''))
        print('└──────────────────────────────────────────────────┘')
        key=input('> ')
        if key.isdigit()==True:
            print('┌───────────────────────────────────────OVERWRITE?─┐')
            print('│Please enter a non-digit key                      │')
            print('└──────────────────────────────────────────────────┘')
            os.system('pause')
        else:
            inputloop=False
        os.system('cls')
    print('┌────────────────────────────────────────────INPUT─┐')
    print('│%-50.50s│'%(f'{key}:'))
    print('│\tusername:\t%-27.27s│'%('<'))
    print('│\tpassword:\t%-27.27s│'%(''))
    print('│\thint:\t\t%-27.27s│'%(''))
    print('└──────────────────────────────────────────────────┘')
    username=input('> ')
    os.system('cls')
    print('┌────────────────────────────────────────────INPUT─┐')
    print('│%-50.50s│'%(f'{key}:'))
    print('│\tusername:\t%-27.27s│'%(username))
    print('│\tpassword:\t%-27.27s│'%('<'))
    print('│\thint:\t\t%-27.27s│'%(''))
    print('└──────────────────────────────────────────────────┘')
    password=input('> ')
    os.system('cls')
    print('┌────────────────────────────────────────────INPUT─┐')
    print('│%-50.50s│'%(f'{key}:'))
    print('│\tusername:\t%-27.27s│'%(username))
    print('│\tpassword:\t%-27.27s│'%(password))
    print('│\thint:\t\t%-27.27s│'%('<'))
    print('└──────────────────────────────────────────────────┘')
    hint=input('> ')
    os.system('cls')
    print('┌────────────────────────────────────────────INPUT─┐')
    print('│%-50.50s│'%(f'{key}:'))
    print('│\tusername:\t%-27.27s│'%(username))
    print('│\tpassword:\t%-27.27s│'%(password))
    print('│\thint:\t\t%-27.27s│'%(hint))
    print('└──────────────────────────────────────────────────┘')

    # check if already exists
    if key in dir:
        print('┌───────────────────────────────────────OVERWRITE?─┐')
        print('│Directory already exists. (y) to overwrite.       │')
        print('└──────────────────────────────────────────────────┘')
        choice=input('> ')
        if choice=='y':
            dir.update({key:[username,password,hint]})
    else:
        dir.update({key:[username,password,hint]})
    os.system('cls')

    '''
    import checkStrength
    if checkStrength==False:
        import suggestPass
    choice=input('> ')
    if choice=='y':
        dir.update({key:[username,newpassword,hint]})
    '''