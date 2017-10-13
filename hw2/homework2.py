a = str(input('Input word:')).replace("з","").replace("З","").replace("я","").replace("Я","")
for i in reversed(a):
    print(i,end='')
