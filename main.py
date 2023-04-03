#import checkStrength
#import suggestPassword
#import saveRemove
import os
import login
import inputinfo

dir={}
#login.login()

mainloop=True
while mainloop:
    # display menu
    print('┌─────────────────────────ANONG GUSTO MO GAWIN ERP─┐')
    print('│%-50.50s│\n│%-50.50s│\n│%-50.50s│\n│%-50.50s│'%(
        '1. Add Credential','2. Remove Credential','3. Exit','n. Enter Key to View Password'
        ))
    print('└──────────────────────────────────────────────────┘')
    print('┌────────────────────────────────SAVED CREDENTIALS─┐')
    if len(dir)==0:
        print('│%-50.50s│'%('No saved credentials yet.'))
    for key, value in dir.items():
        print('│%-50.50s│'%(f'{key}:'))
        print('│\tusername:\t%-27.27s│'%(value[0]))
        print('│\tpassword:\t%-27.27s│'%(len(value[1])*'∙'))
        print('│\thint:\t\t%-27.27s│'%(value[2]))
        print('│%-50.50s│'%(''))
    print('└──────────────────────────────────────────────────┘')
    choice=input('> ')
    os.system('cls')

    if choice=='1': # input credentials
        inputinfo.inputinfo(dir)
    elif choice=='2': # remove something
        print('you removed something')
    elif choice=='3': # exit program 
        print('exiting')
        mainloop=False
    elif choice in dir: # unhide password
        print('┌─────────────────────────ANONG GUSTO MO GAWIN ERP─┐')
        print('│%-50.50s│\n│%-50.50s│\n│%-50.50s│\n│%-50.50s│'%(
            '1. Add Credential','2. Remove Credential','3. Exit','n. Enter Key to View Password'
            ))
        print('└──────────────────────────────────────────────────┘')
        print('┌────────────────────────────────SAVED CREDENTIALS─┐')
        if len(dir)==0:
            print('│%-50.50s│'%('No saved credentials yet.'))
        for key, value in dir.items():
            print('│%-50.50s│'%(f'{key}:'))
            print('│\tusername:\t%-27.27s│'%(value[0]))
            if key==choice:
                print('│\tpassword:\t%-27.27s│'%(value[1]))
            else:
                print('│\tpassword:\t%-27.27s│'%(len(value[1])*'∙'))
            print('│\thint:\t\t%-27.27s│'%(value[2]))
            print('│%-50.50s│'%(''))
        print('└──────────────────────────────────────────────────┘')
        os.system('pause')
        os.system('cls')
