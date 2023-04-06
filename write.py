
def save(mainUser,mainPass,dir):
    with open(f'{mainUser}.txt','w') as f:
        f.writelines(f'{mainPass}\n\n')
        for key,value in dir.items():
            f.writelines(f'{key}\n')
            f.writelines(f'{value[0]}\n')
            f.writelines(f'{value[1]}\n')
            f.writelines(f'{value[2]}\n')
            f.writelines(f'{value[3]}\n\n')

def load(mainUser):    
    dir={}
    try:
        with open(f'{mainUser}.txt','r') as f:
            a=f.readlines()
            a=[i.strip() for i in a]
            a=[i for i in a if i!='']
            mainPass=a.pop(0)

            for i in range(int(len(a)/5)):
                values=[]
                key=a.pop(0)
                for i in range(3):
                    values.append(a.pop(0))
                values.append(int(a.pop(0)))
                dir[key]=values
            return dir
    except:
        return dir