print("Введите с клавиатуры длину катетов")

a1 = float(input())
b1 = float(input())

#print(a1, b1)

c = a1**2 + b1**2
c = c**0.5

cf = "{:.10f}".format(c)
#print(format_float)
print("Гипотенуза = ", cf)


