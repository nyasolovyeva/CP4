N = int(input("В ведите размерность массива:"))
D = [0] * N # заполнение массива нулями
from random import uniform # подключение функции uniform, uniform возвращает случайное вещественное число в указанном промежутке (от -7 до 7)
for i in range(N): # перебор индексов
    D[i] = round(uniform(-7,7),1) # случайные числа от -7 до 7, с округлением до 1 знака после запятой
print (D)
max_number = D[0] # записываем в max_number самый первый эл-т в массиве
imax = 0 # imax - индекс наибольшего элемента в массиве, чтобы узнать в каком месте наибольшее число, чтобы после него поставить нули
for i in range(1,N): 
    if D[i] > max_number:
        max_number = D[i]
        imax = i # приваиваем индекс наибольшего элемента
print(max_number)
for i in range(imax+1, N):
    D[i] = 0
print(D)





