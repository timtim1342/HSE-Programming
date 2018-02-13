def dict(filename_one, filename_two): # читает файл со словами, которые надо будет угадывать. создает словарь с ключами из этих слов и значением из выражений.
    d={}
    with open(filename_one, encoding='utf-8') as f:
        text = f.read()
        words = text.split(',')
    with open(filename_two, encoding='utf-8') as f:
        text = f.read()
        contexts = text.split(',')
    for word in words:
        for context in contexts:
            if word in context:
                d[word] = context
    return d
def whatword(di):
    import random
    keys = list(di.keys())
    whatword = random.choice(keys)
    print(whatword)
    print(di[whatword].replace(whatword, '...'))

whatword(dict('words.csv','cont.csv'))
