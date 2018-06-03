def opn():
    with open('ref.txt', encoding='utf-8') as f:
        text = f.read()  
    text = text.replace('\ufeff', '').replace('?', '.').replace('!', '.').replace(':', '').replace(';', '').replace(')', '').replace('(', '').replace('\"', '').replace('-', '').replace(',', '').split('.')
    txt = [sent.split() for sent in text]
    return txt
def cre(lst):
    res = [word + '_' + str(len(word)) for sent in lst for word in sent]
    return res
def pr(lst):
    for word in lst:
        print(word + ' ', end='')
def main():
    pr(cre(opn()))
    
if __name__ == '__main__':
    main()
