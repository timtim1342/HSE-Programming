import random
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
    score = 0
    keys = list(di.keys())
    random.shuffle(keys)
    for count in range(0,5):
        whatword = keys[count]
        counter = len(di[whatword])-len(whatword)-1 #циклы внутри ф не оч. оптим.
        while counter != 0:
            print(di[whatword].replace(whatword, '...'))
            thisword = input()
            if thisword == whatword:
                print('You win')
                score += 1
                break
            elif counter != 1:
                counter -= 1
                print('NoNoNo, try again.', counter)
            else:
                print('You lose')
                break
    print('Your score:', score)
if __name__ == '__main__':
    whatword(dict('words.csv', 'cont.csv'))
    


