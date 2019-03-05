s=[]
n=int(input('Введите кол-во элементов больше 10: '))
if n<=10:
    print('Ошибка')
else:
    print ('В строке '+str(n)+' элементов')
    while n>0:
        a=int(input('Введите число: '))
        s.append(a)
        n=n-1
    s.pop(0)
    s.pop(0)
    b=int(input('Введите добавляемый элемент: '))
    s.append(b)
    c=int(input('Введите добавляемый элемент: '))
    s.append(c)
    print(s)
