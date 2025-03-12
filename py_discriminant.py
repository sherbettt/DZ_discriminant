import math

a = int(input('Insert a: '))
b = int(input('Insert b: '))
c = int(input('Insert c: '))


# функция вычисления дискриминанта
def discriminant(a,b,c):
    global D
    D = b**2 - 4*a*c

# квадратное уравнение и основной цикл
def solve(a,b,c):
    discriminant()
    if D == 0:
        x = -b/2*a
        return(f' Дискриминант имеет 1 корень: x = {x}')
    elif D > 0:
        x1 = int((-b - math.sqrt(D)) / (2 * a))
        x2 = int((-b + math.sqrt(D)) / (2 * a))
        return(f' Дискриминант имеет 2 корня: x1 = {x1}, x2 = {x2}')
    if D < 0:
        raise StopIteration

print(discriminant(a,b,c))
print(solve(a,b,c))




'''
Условие/уравнение:
ax² + bx + c = 0, где a != 0
Решение:
x = (-b±D)/2·a, 
где D = b²−4ac — дискриминант квадратного уравнения.
 x = (-b±√D)/2a означает, что x1 = (-b+√D)/2a, x2 = (-b-√D)/2a.
'''