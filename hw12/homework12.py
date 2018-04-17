import os, re

def create_list_dir():
    dir_list = str(os.listdir())
    return dir_list

def find_good_ones():
    res = re.findall(r'\'\b([а-яА-Я]+)\b\'', create_list_dir())
    return res

def our_achievements():
    ress = find_good_ones()
    print('Всего папок, сожержащих только кириллические символы, вот столько:', len(ress))
    if len(ress) != 0:
        print('Такие вот папки:')
        for i in range(len(ress)):
            print(ress[i])

if __name__ == '__main__':
    our_achievements()
