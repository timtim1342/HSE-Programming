count=0
with open("Extinct_languages.tsv", encoding="utf-8") as f:
    for line in f:
        if len(line)>35:
            print(line)
        if 'Critically endangered' in line:
            count+=1
print('Число языков critically endangered:',count)
