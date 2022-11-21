#N = int(input('Введите натуральное число - количество элементов в массиве'))
#a = [int(i) for i in input().split()]
N = 5
lst = [1, 2, 3, 4, 5]
i = 2
x = 4
lst.insert(i, x)
print(lst)


#for i in range(1, N):

    #for j in range(i, 0, -1):
        #if a[j] < a[j - 1]:
           # a[j], a[j - 1] = a[j - 1], a[j]
        #else:
            #break
    #print(a)