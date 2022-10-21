n=int(input('Введите размерность массива: '))
mas=[float(i) for i in input('Введите элементы массива ').split()]
def elements(mas):
    imax=0
    for i in range(1, n):
        if (mas[i] >= mas[imax]):
            imax=i
    for i in range (imax + 1, n):
        mas[i]=0
    return (mas)
print('Полученный массив: ', elements(mas))
