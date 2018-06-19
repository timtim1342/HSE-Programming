import os, re

docid, title, author, created, topic, tagging = [],[],[],[],[],[]

def files_in_dir(): #список файлов в дир.
    return os.listdir()

def change_dir(dir_name): #меняет директорию
    os.chdir(dir_name)

def opn(name):
    with open(name, encoding='windows-1251') as f:
        text = f.read()  
    return text

def find_inf(file_names):
    global docid, title, author, created, topic, tagging
    for file in file_names:
        txt = opn(file)
        docid.extend(re.findall(r'\<meta\scontent=\"([\w0-9\.]+)\"\sname=\"docid', txt))
        author.extend(re.findall(r'\<meta\scontent=\"([а-яА-Я\s]+)\"\sname=\"author', txt))
        created.extend(re.findall(r'\<meta\scontent=\"([0-9\.]+)\"\sname=\"created', txt))
        topic.extend(re.findall(r'\<meta\scontent=\"([\,\s\w]+)\"\sname=\"topic', txt))
        tagging.extend(re.findall(r'<meta\scontent=\"(\w+)\"\sname=\"tagging', txt))
        title.extend(re.findall(r'\<title\>([^\<]+)', txt))
                
def write_csv():
    global docid, title, author, created, topic, tagging
    with open('exam.csv','w', encoding='utf-16') as f:
        f.write('doc_id' + '\t' + 'title' + '\t' + 'author' + '\t' + 'created' + '\t' + 'topic' + '\t' + 'tagging')
        f.write('\n')
        for i in range(len(docid)):
            f.write(docid[i] + '\t' + title[i] + '\t' + author[i] + '\t' + created[i] + '\t' + topic[i] + '\t' + tagging[i])
            f.write('\n')

def main():
    change_dir('news')
    find_inf(files_in_dir())
    write_csv()
    
if __name__ == '__main__':
    main()
