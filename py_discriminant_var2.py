import math

a = int(input('Введи значение a: '))
b = int(input('Введи значение b: '))
c = int(input('Введи значение c: '))

# функция вычисления дискриминанта
def discriminant(a,b,c):
    D = b**2 - 4*a*c
    print(f'Дискриминант = {D}')
    return D

# квадратное уравнение и основной цикл
def solve(a,b,c):
    D = discriminant(a, b, c)
    if D > 0:
        x1 = int((-b - math.sqrt(D)) / (2 * a))
        x2 = int((-b + math.sqrt(D)) / (2 * a))
        return(f' Дискриминант имеет 2 корня: x1 = {x1}, x2 = {x2}')
    elif D == 0:
        x = -b / (2 * a)
        return(f'Дискриминант имеет 1 корень: x = {x}')
    else:
        return("при D<0 решение нет")


print(solve(a,b,c))
#print(discriminant(a,b,c))
#print(solve(1, 2, 1))
#print(solve(2, 5, 3))
#print(solve(1, -1, 3))
