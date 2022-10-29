command = input('Введите команду: ')
if command == '+':
    num1 = float(input('Введите первое слагаемое: '))
    num2 = float(input('Введите второе слагаемое: '))
    print("Сумма:", num1 + num2)
elif command == '-':
    num1 = float(input('Введите уменьшаемое: '))
    num2 = float(input('Введите вычитаемое: '))
    print("Разность:", num1 - num2)
elif command == '/':
    num1 = float(input('Введите делимое: '))
    num2 = float(input('Введите делитель: '))
    if num2 != 0:
        print("Частное:", num1 / num2)
    else:
        print("На ноль делить нельзя")
elif command == '*':
    num1 = float(input('Введите первый множитель: '))
    num2 = float(input('Введите второй множитель: '))
    print("Произведение:", num1 * num2)
elif command == 'корень':
    num = float(input('Введите число: '))
    print("Корень:", math.sqrt(num))
elif command == 'степень':
    num1 = float(input('Введите число: '))
    num2 = float(input('Введите, в какую степень возвести: '))
    print("Степень", num2, "числа", str(num1)+":", num1 ** num2)
else:
    print('Неверная команда')
    
