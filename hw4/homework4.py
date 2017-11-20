tre=0
uno=0
with open('OL2.txt', encoding='utf-8') as f:
    text=f.read()
    text=text.replace('.','').replace(',','').replace('?','').replace('..','').replace('...','').replace('\ufeff','')
    lis=list(text.split())
for i in range(len(lis)):
    if len(lis[i])==3:
        tre+=1
    elif len(lis[i])==1:
        uno+=1
print(tre,uno)
if uno>tre:
    print('oneletter words more than threeletters words')
elif uno!=0:
    print(tre/uno,'times more')
else:
    print('No oneletter words')
