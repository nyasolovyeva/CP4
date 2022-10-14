N = int(input("В ведите размерность массива:"))
D = [0] * N #заполнение массива нулями
for i in range (N):
    D[i] = float(input("Введите элемент массива: "))
print (D)
max_number = D[0]
imax = 0
for i in range(1,N):
    if D[i] > max_number:
        max_number = D[i]
        imax = i
for i in range(imax+1, N):
    D[i] = 0
print (D)
