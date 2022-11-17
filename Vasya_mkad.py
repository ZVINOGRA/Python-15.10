def distance(v, t):
    return v * t

v = int(input())
t = int(input())
x = distance(v, t)

if x > 109:
    result = x % 109
    print(result)
else:
    print(x)



