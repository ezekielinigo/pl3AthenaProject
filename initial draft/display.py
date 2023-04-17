import os
import platform

def menu():
    print('┌─────────────────────────────────────────────PCGM─┐')
    print('│%-50.50s│\n│%-50.50s│\n│%-50.50s│\n│%-50.50s│\n│%-50.50s│'%(
    '    [E] end program','    [A] add credential',' [name] to edit credential','[!name] to view & copy password','[delete] to delete profile'))
    print('└──────────────────────────────────────────────────┘')

def strength(strength):
    displayBar = lambda i: '▓▓▓▓▓▓▓▓▓'*(i//9) + '▒▒▒▒▒▒▒▒▒'[:i%9] + '░'*(36-i)
    if strength<9:
        print('│%-50.50s│'%(''))
        print('│{:^50}│'.format(displayBar(strength)))
        print('│{:^50}│'.format('VERY WEAK'))
    elif strength<18:
        print('│%-50.50s│'%(''))
        print('│{:^50}│'.format(displayBar(strength)))
        print('│{:^50}│'.format('WEAK'))
    elif strength<27:
        print('│%-50.50s│'%(''))
        print('│{:^50}│'.format(displayBar(strength)))
        print('│{:^50}│'.format('MEDIUM'))
    elif strength<36:
        print('│%-50.50s│'%(''))
        print('│{:^50}│'.format(displayBar(strength)))
        print('│{:^50}│'.format('STRONG'))
    else:
        print('│%-50.50s│'%(''))
        print('│{:^50}│'.format(displayBar(strength)))
        print('│{:^50}│'.format('VERY STRONG'))

def errors(points,reqs):
    x = ['x' if i == False else ' ' for i in reqs.values()]
    print('┌──────────────────────────────────RECOMMENDATIONS─┐')
    print(f'│[{x[0]}] at least 8 characters.                        │')
    print(f'│[{x[1]}] numbers.                                      │')
    print(f'│[{x[2]}] uppercased letters.                           │')
    print(f'│[{x[3]}] lowercased letters.                           │')
    print(f'│[{x[4]}] symbols.                                      │')
    strength(points)
    print('│%-50.50s│'%(''))
    print('└──────────────────────────────────────────────────┘')

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def pause():
    if platform.system() == "Windows":
        os.system("pause")
    else:
        os.system("read -n 1 -s -p \"Press any key to continue...\"")