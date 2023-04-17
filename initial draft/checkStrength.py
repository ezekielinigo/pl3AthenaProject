import re

def password_check(password):
    
    a = {
        'length' : len(password),
        'digits' : len(re.findall(r"\d", password)),
        'uppercase' : len(re.findall(r"[A-Z]", password)),
        'lowercase' : len(re.findall(r"[a-z]", password)),
        'symbols' : len(re.findall(r"[@!#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password))
    }

    errors = {
        'at least 8 characters' : len(password) < 8,
        'numbers' : re.search(r"\d", password) is None,
        'uppercased letters' : re.search(r"[A-Z]", password) is None,
        'lowercased letters' : re.search(r"[a-z]", password) is None,
        'symbols' : re.search(r"[@!#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None
    }

    points = 0

    # count characters
    if a['length']<8:
        points+=0
    elif a['length']<12:
        points+=2
    elif a['length']<15:
        points+=6
    else:
        points+=15

    # count digits
    if 0.4<(a['digits']/(a['digits']+a['uppercase']+a['lowercase']))<0.6:
        points+=6
    elif 0.2<(a['digits']/(a['digits']+a['uppercase']+a['lowercase']))<0.8:
        points+=4
    else:
        points+=2

    # count symbols
    if 0.2<(a['symbols']/a['length'])<0.8:
        points+=4
    elif 0.05<(a['symbols']/a['length'])<0.95:
        points+=2
    else:
        points+=1

    # count uppercase/lowercase ratio
    if 0.4<(a['uppercase']/(a['uppercase']+a['lowercase']))<0.6:
        points+=6
    elif 0.2<(a['uppercase']/(a['uppercase']+a['lowercase']))<0.8:
        points+=4
    else:
        points+=2

    if 0.4<(a['lowercase']/(a['uppercase']+a['lowercase']))<0.6:
        points+=6
    elif 0.2<(a['lowercase']/(a['uppercase']+a['lowercase']))<0.8:
        points+=4
    else:
        points+=2
        

    # MAX POINTS POSSIBLE: 33

    # points to be used sa strength meter
    # any(errors.values()) == False, means password is ok
    return points, errors
