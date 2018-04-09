import re
def create_text():
    with open('file.xml', encoding='utf-8') as f:
        text = f.read()
        return text
    
def count_lines():
    str_count = 0
    for line in create_text():
        if line.endswith("\n"):
            str_count += 1
    return 'Всего строк:' + str(str_count)

def write_in(txt):
    with open('exam.txt', 'a', encoding='utf-8') as f:
        f.write(txt)

def create_keys():
    keys = []
    with open('file.xml', encoding='utf-8') as f:
        for line in f:
            if line.startswith('            <w lemma='):
                keys += re.findall(r'type="([\w-]+)">', line)
    return(keys)

def create_dic():
    dic = {}
    for key in create_keys():
        if key not in dic:
            dic[key] = 1
        else:
            dic[key] += 1
    return(dic)

def write_keys():
    for k in create_dic():
        write_in('\n' + k)
        
def ex_first_sec():
    write_in(count_lines())
    write_keys()
    
if __name__ == '__main__':
    ex_first_sec()
