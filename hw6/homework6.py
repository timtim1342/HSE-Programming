import random

def verb(): # случайный выбор глагола
    with open('verbs.txt', encoding='utf-8') as f:
        text = f.read()
        verbs = text.splitlines()
    return random.choice(verbs)

def subj(): # случайный выбор субъекта действия
    with open('subj.txt', encoding='utf-8') as f:
        text = f.read()
        subj = text.splitlines()
    return random.choice(subj)

def obj(): # случайный выбор объекта действия
    with open('objSg.txt', encoding='utf-8') as f:
        text = f.read()
        obj = text.splitlines()
    return random.choice(obj)

def imp(): # случайный выбор глагола в повелительном наклонении 
    with open('imperative.txt',encoding='utf-8') as f:
        text = f.read()
        imper = text.splitlines()
    return random.choice(imper)

def adj(): # случайный выбор определения к субъекту
     with open('AdjSg.txt',encoding='utf-8') as f:
        text = f.read()
        ad = text.splitlines()
     return random.choice(ad)

def negative(): #отрицательное предложение
    verse = random.choice([0,1,2,3])
    if verse == 1:
        return adj().capitalize() + ' ' + subj() + ' не ' + verb() + ' ' + obj()
    elif verse == 2:
        return adj().capitalize() + ' ' + subj() + ' ' + verb() + ' не ' + obj()
    elif verse == 3:
        return subj().capitalize() + ' не ' + verb() + ' ' + obj()
    else:
        return subj().capitalize() + ' ' + verb() + ' не ' + obj()
        

def state(): #утвердительное
    verse = random.choice([0,1,2])
    if verse == 1:
        return adj().capitalize() + ' ' + subj() + ' ' + verb() + ' ' + obj()
    if verse == 2:
        return 'Я есть Грут'
    else:
        return subj().capitalize() + ' ' + verb() + ' ' + obj()

def imperative(): #повелительное
    verse = random.choice([0,1])
    if verse == 1:
        return adj().capitalize() + ' ' + subj() + ', ' + imp() + ' ' + obj()
    else:
        return subj().capitalize() + ' ' + imp() + ', ' + obj()
def conditional(): #условное
    verse = random.choice([0,1])
    if verse == 1:
        return adj().capitalize() + ' ' + subj() + ' ' + verb() + ' бы ' + obj()
    else:
        return subj().capitalize() + ' ' + verb() + ' бы ' + obj()
def question(): #вопросительное
    verse = random.choice([0,1,2,3])
    if verse == 1:
        return state() + '?' #вопросительным может стать предложение любого типа,
                             #кроме повелительного
    elif verse == 2:
        return negative() + '?'
    elif verse == 3:
        return conditional() + '?'
    else:
        return 'Я есть Грут?'
    
def randomtxt():
    a = b = c = d = e = 0
    while a == 0 or b == 0 or c == 0 or d == 0 or e == 0:
        verse1 = random.choice([0,1])
        verse2 = random.choice([0,1])
        verse3 = random.choice([0,1])
        verse4 = random.choice([0,1])
        verse5 = random.choice([0,1])
        if verse1 == 1 and a == 0:
            print(negative() + '.', end=' ')
            a += 1
        elif verse2 == 1 and b == 0:
            print(state() + '.',end=' ')
            b += 1
        elif verse3 == 1 and c == 0:
            print(question(), end=' ')
            c += 1
        elif verse4 == 1 and d == 0:
            print(imperative() + '.', end=' ')
            d += 1
        elif verse5 == 1 and e == 0:
            print(conditional() + '.', end=' ')
            e += 1
randomtxt()
