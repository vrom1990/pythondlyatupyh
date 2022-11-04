import math
print('Выберите калькулятор, максимум или анекдот')
command = input('Введите команду: ')

# КАЛЬКУЛЯТОР
if command == "калькулятор":
    operation = input('Введите команду: ')

    if operation == '+':
        num1 = float(input('Введите первое слагаемое: '))
        num2 = float(input('Введите второе слагаемое: '))
        print("Сумма:", num1 + num2)
    elif operation == '-':
        num1 = float(input('Введите уменьшаемое: '))
        num2 = float(input('Введите вычитаемое: '))
        print("Разность:", num1 - num2)
    elif operation == '/':
        num1 = float(input('Введите делимое: '))
        num2 = float(input('Введите делитель: '))
        if num2 == 0:
            print("На ноль делить нельзя")
        else:
            print("Частное:", num1 / num2)
    elif operation == '*':
        num1 = float(input('Введите первый множитель: '))
        num2 = float(input('Введите второй множитель: '))
        print("Произведение:", num1 * num2)
    elif operation == 'корень':
        num = float(input('Введите число: '))
        print("Корень:", math.sqrt(num))
    elif operation == 'степень':
        num1 = float(input('Введите число: '))
        num2 = float(input('Введите, в какую степень возвести: '))
        print("Степень", num2, "числа", str(num1)+":", num1 ** num2)
    else:
        print('Неверная операция')
        
# МАКСИМУМ        
elif command == "максимум":
    print('Эта подпрограмма ищет максимум из трёх чисел')
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    num3 = int(input("Введите третье число: "))

    if num1 > num2:
        if num1 > num3:
            print("Максимум:", num1)
        else:
            print("Максимум:", num3)
    else:
        if num2 > num3:
            print("Максимум:", num2)
        else:
            print("Максимум:", num3)
# АНЕКДОТ            
elif command == "анекдот":
    print('Сел медведь в машину и сгорел')
else:
    print("Неизвестная команда")