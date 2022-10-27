prodolzhit = 'y'
while prodolzhit == 'y':
    if prodolzhit == 's':
        break
    print("Введите число 1")
    a = float(input())
    oper = input("Введите операцию")
    print("Введите число 2")
    b = float(input())
    if oper == "+":
        print(a + b)
    elif oper == "-":
         print(a - b)
    elif oper == "*":
        print(a * b)
    elif oper == "/":
        print(a / b)
    elif oper == "**":
        print(a** b)
    else:
        print('error')
    prodolzhit = input("Нажмите 'y', если хотите продолжить, или 's', если вычисления окончены")




