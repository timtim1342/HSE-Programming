def wor(file_name): #возвр. текст без знаков пункт.
    with open(file_name, encoding='utf-8') as f:
        text = f.read()
        s_text = text.replace(',','').replace('.','').replace('!','').replace('?','').split()
    return s_text

def dic(s_text): #создает словарь( слово: количество употреблений в тексте)
    d = {}
    for word in s_text:
        if word.endswith('hood') or word.endswith('hoods'):
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    return d

def sub_count(d): # сколько всего сущ с -hood в тексте
    tot = 0
    for count in d.values():
        tot += count    
    return tot

def get_key(d, value): #возвращает ключ по значению
    for k, v in d.items():
        if v == value:
            return k
        
def min_freq(d): #возвращает слово с мин частотой
    for value in sorted(d.values()):
        return get_key(d, value)
        
def s(d): #возвращает слова, от которых образованы сущ с -hood
    lis = d.keys()
    st = ''
    for word in lis:
        word = (word.replace('hoods','').replace('hood','') + ' ')
        if word not in st: #чтобы не вышло, что neigbhbourhood и neighbourhoods образованны от разных слов
            st += word + ' '
    
    return st

def main():
    name = str(input()) + '.txt'
    print('Всего',sub_count(dic(wor(name))), 'сущ. с "-hood"')
    print('Минимальная частотность у слова:', min_freq(dic(wor(name))))
    print('Образ. от:',s(dic(wor(name))))
if __name__ == '__main__':
    main()
    
    
                         

    

        
