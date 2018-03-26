import re
with open('Высшая школа экономики — Википедия.html', encoding='utf-8') as f:
    text = f.read().lower()
text = re.sub(r'(\<(/?[^>]+)>)','',text)
date = (re.findall('год основания\n.*([0-9]{4})',text))
with open('Дата основания.txt','w', encoding='utf-8') as f:
    f.write(date[0])
