N = int(input())
a = [i for i in range(1, N-1)]
b = [i**2 for i in a if i**2 < N]
print(b)