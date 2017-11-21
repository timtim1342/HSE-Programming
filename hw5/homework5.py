a=str(input())
k=0
with open("mytxt.txt", "w", encoding="utf-8") as f:
    f.write('')
while a!='':
    with open("mytxt.txt", "a", encoding="utf-8") as f:
        f.write(a[1+k:])
        f.write('\n')
    a=str(input())
    k+=1
