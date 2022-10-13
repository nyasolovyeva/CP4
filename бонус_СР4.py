delta = int(input("Введите delta: "))
A = [4, 6, 6, 2, 9]
min_el = A[0]
for i in range(1, len(A)): # перебор индексов, начиная с 1
    if A[i] < min_el: 
        min_el = A[i]
print(min_el)
k = 0
for i in range(len(A)): # перебор индексов
    if A[i] - min_el == delta:
        k+=1
print(k)
        
    