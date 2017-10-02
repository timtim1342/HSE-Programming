print("Input a:", end='')
a=float(input())
print("Input b:", end='')
b=float(input())
print("Input c:", end='')
c=float(input())
if b!=0:
    if a%b==c:
        print("a даёт остаток c при делении на b")
    else:
        print("a не даёт остаток c при делении на b")
else:
    print("Division by zero")
if a*c+b==0 or a==0 and b==0:
    print("c является решением линейного уравнения ax + b = 0")
else:
    print('c не является решением линейного уравнения ax + b = 0')
