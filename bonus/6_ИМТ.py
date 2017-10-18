sm=int(input('Рост(в см):'))
kg=int(input('Вес(в кг):'))
index=kg/((sm/100)**2)
print(index)
if index<=16:
    print('Выраженный дефицит массы тела')
elif index>16 and index<18.5:
    print('Дефицит массы тела')
elif index>=18.5 and index<=25:
    print('Норма')
elif index>25 and index<=30:
    print('Предожирение')
elif index>30 and index<35:
    print('Ожирение I степени')
elif index>=35 and index<=40:
    print('Ожирение II степени')
elif index>40:
    print('Ожирение III степени')
