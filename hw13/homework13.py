import os, re
formats = {} # словарь {расширение: количество файлов с этим расширением}

def count_formats(list_of_ext): #считает количество файлов с каждым расширением
    for ext in list_of_ext:
        if ext not in formats:
            formats[ext] = 1
        else:
            formats[ext] += 1
            
def cut_it(file_names): #обрезает все названия файлов, оставляя только расширения
    ext_names = []
    for file in file_names:
        ext_names.extend(re.findall(r'\b.+\.([a-z]+\b)', file))
    return ext_names

def folders_in_dir(file_names): #отдельно находит папки, чтобы потом по ним ходить(т.к. у них нет расширения)
    folders = []
    for file in file_names:
        if re.findall(r'\b.+\.([a-z]+\b)', file) == []:
            folders.append(file)
    return folders
    
def files_in_dir(): #список файлов в дир.
    return os.listdir()

def change_dir(dir_name): #меняет директорию
    os.chdir(dir_name)
       
def main():
    count_formats(cut_it(files_in_dir()))
    folders_here = folders_in_dir(files_in_dir())
    for folder in folders_here:
        change_dir(folder)
        main()
        change_dir(os.path.dirname(os.getcwd())) 

def find_max(): #создает из словаря formats два списка(один со значениями, другой с ключами). ищет max по списку со значениями, смотрит его индекс, по этому индексу выводит ключ из второго списка.
    ind = list(formats.values()).index(max(formats.values())) 
    print('Большего всего файлов с расширением:', list(formats.keys())[ind])
    

if __name__ == '__main__':
    main()
    find_max()
