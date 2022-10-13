N1 = int(input("Введите размерность массива 1:"))
D = [0] * N1 # заполнение массива нулями
from random import randint # подключение функции randint
for i in range(N1): # перебор индексов
    D[i] = randint(-7, 7) # случайные числа от -7 до 7
print (D)
N2 = int(input("Введите размерность массива 2:"))
A = [0] * N2 # заполнение массива нулями
for j in range(N2): # перебор индексов
    A[j] = randint(-7, 7) # случайные числа от -7 до 7
print (A)
for i in D:
    for j in A:
        if i == j:
            print (i)