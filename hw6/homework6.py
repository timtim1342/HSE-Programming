import random

def wordrand(a): #выбирает случайное слово. в зависимости от значения a выбирает глагол, субъект действия, объект действия, повелительный глагол или определение к субъекту
    if a == 1:
        with open('verbs.txt', encoding='utf-8') as f:
            text = f.read()
            word = text.splitlines()
        return random.choice(word)
    elif a == 2:
        with open('subj.txt', encoding='utf-8') as f:
            text = f.read()
            word = text.splitlines()
        return random.choice(word)
    elif a == 3:
        with open('objSg.txt', encoding='utf-8') as f:
            text = f.read()
            word = text.splitlines()
        return random.choice(word)
    elif a ==4:
        with open('imperative.txt',encoding='utf-8') as f:
            text = f.read()
            word = text.splitlines()
        return random.choice(word)

    else:
        with open('AdjSg.txt',encoding='utf-8') as f:
            text = f.read()
            word = text.splitlines()
        return random.choice(word)

def negative(): #отрицательное предложение
    verse = random.choice([0,1,2,3])
    if verse == 1:
        return wordrand(0).capitalize() + ' ' + wordrand(2) + ' не ' + wordrand(1) + ' ' + wordrand(3)
    elif verse == 2:
        return wordrand(0).capitalize() + ' ' + wordrand(2) + ' ' + wordrand(1) + ' не ' + wordrand(3)
    elif verse == 3:
        return wordrand(2).capitalize() + ' не ' + wordrand(1) + ' ' + wordrand(3)
    else:
        return wordrand(2).capitalize() + ' ' + wordrand(1) + ' не ' + wordrand(3)
        

def state(): #утвердительное
    verse = random.choice([0,1,2])
    if verse == 1:
        return wordrand(0).capitalize() + ' ' + wordrand(2) + ' ' + wordrand(1) + ' ' + wordrand(3)
    if verse == 2:
        return 'Я есть Грут'
    else:
        return wordrand(2).capitalize() + ' ' + wordrand(1) + ' ' + wordrand(3)

def imperative(): #повелительное
    verse = random.choice([0,1])
    if verse == 1:
        return wordrand(0).capitalize() + ' ' + wordrand(2) + ', ' + wordrand(4) + ' ' + wordrand(3)
    else:
        return wordrand(2).capitalize() + ', ' + wordrand(4) + ' ' + wordrand(3)
def conditional(): #условное
    verse = random.choice([0,1])
    if verse == 1:
        return wordrand(0).capitalize() + ' ' + wordrand(2) + ' ' + wordrand(1) + ' бы ' + wordrand(3)
    else:
        return wordrand(2).capitalize() + ' ' + wordrand(1) + ' бы ' + wordrand(3)
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
