l=list(input())
for j in range(0,len(l)):
    print()
    for i in range(0,len(l)):
        print(l[-len(l)+i+j],end='')
