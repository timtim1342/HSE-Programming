a=str(input('Название языка:'))
b=[]
while a!='':
    b.append(a)
    a=str(input('Название языка:'))
for i in range(len(b)):
    with open("Extinct_languages.tsv", encoding="utf-8") as f:
        for line in f:
            if line.startswith(b[i]):
                print(line)
                break
