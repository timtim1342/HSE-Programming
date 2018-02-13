def dict(filename_one, filename_two): # читает файл со словами, которые надо будет угадывать. создает словарь с ключами из этих слов и значением из выражений.
    d={}
    with open(filename_one, encoding='utf-8') as f:
        text = f.read()
        words = text.split(', ')
    with open(filename_two, encoding='utf-8') as f:
        text = f.read()
        contexts = text.split(', ')
    for word in words:
        for context in contexts:
            if word in context:
                d[word] = context
    return d

def whatword(di):
    import random
    keys = list(di.keys())
    whatword = random.choice(keys)
    counter = 0
    ind = len(di[whatword])-len(whatword)-1
    while counter != ind:
        print(di[whatword].replace(whatword, '...'))
        thisword = input()
        if thisword != whatword:
            print( 'НетНетНет, осталось попыток:', ind - counter)
            counter += 1
        else:
            print('correct')
            counter = ind
    


