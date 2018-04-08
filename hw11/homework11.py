import re
def opn():
    with open('Лингвистика — Википедия.txt', encoding='utf-8') as f:
        text = f.read()
    return text
            
def shashlik_mashlik():
    return re.sub(r'\bЯзык([иауео]?[хмв]?и?)\b', r'Шашлык\1', re.sub(r'\bязык([иауео]?[хмв]?и?)\b', r'шашлык\1', opn()))

def make_shashlik():
    with open('shashlik.txt', 'w', encoding='utf-8') as f:
        f.write(shashlik_mashlik())
if __name__ == '__main__':
    make_shashlik()
