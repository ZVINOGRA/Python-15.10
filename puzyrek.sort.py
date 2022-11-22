N = 7
a = [9, 2, 8, 5, 3, 7, 1]

for i in range(1, N): #N - 1 итераций работы алгоритма
    for j in range(0, N - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)