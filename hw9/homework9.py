import re
lis=[]
with open('search.txt', encoding='utf-8') as f:
    text = f.read().lower()
    all_res = re.findall('программир(?:ова|у)[а-я][^и][а-я]*', text)
for i in range(len(all_res)):
    if all_res[i] not in lis:
        lis.append(all_res[i])
print('Все формы глагола \'программировать\' в тексте:')
lis.sort()
for word in lis:
      print(word)
