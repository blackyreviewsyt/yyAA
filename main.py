while True:
    num_1 = int(input("Введите первое число: "))
    sign = input("Введите знак арифметической операции или '0' что бы выйти : ")
    if sign == '0':
        break
    num_2 = int(input("Введите второе число: "))
    if sign in ('+', '-', '*', '/'):
        if sign == '+':
            print(num_1 + num_2)
        if sign == '-':
             print(num_1 - num_2)
        if sign == '*':
             print(num_1 * num_2)
        if sign == '/':
            if num_2 == 0:
                print("Нельзя делить на ноль")
            else:
                print(num_1 / num_2)
   else:
        print("Введен неверный знак арифметической операции")


