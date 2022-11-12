import math
x = float(input())
y = x*10 - math.floor(x)*10
if y >= 5:
    z = math.ceil(x)
else:
    z = math.floor(x)
print(z)





