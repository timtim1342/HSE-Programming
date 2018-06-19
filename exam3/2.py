import os, re#не успел перевести все в один файл

abr = {}

def files_in_dir(): #список файлов в дир.
    return os.listdir()

def change_dir(dir_name): #меняет директорию
    os.chdir(dir_name)

def opn(name):
    with open(name, encoding='windows-1251') as f:
        text = f.read()  
    return text

def find_abr(file_names):
    global abr
    for file in file_names:
        txt = opn(file)
        ab = []
        ab.extend(re.findall(r'lex=\"([А-Я]+)\"', txt))
        for name in ab:
            if name in abr.keys():
                abr[name] += 1
            else:
                abr[name] = 1
        

def write_csv():
    global abr
    with open('exam2.csv','w', encoding='utf-16') as f:
        for key in abr.keys():
            f.write(key + '\t' + str(abr[key]))
            f.write('\n')
        
def main():
    change_dir('news')
    find_abr(files_in_dir())
    write_csv()
    
if __name__ == '__main__':
    main()
