a = 25
b = 1000
c = 5
d = 19
if a<b:
    for i in range (a,b):
        remainder = i % d
        if remainder == c:
            print(i)
else:
    for i in range (b,a):
        remainder = i % d
        if remainder == c:
            print(i)