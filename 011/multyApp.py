import math
print('Выберите калькулятор, максимум или анекдот')
comand = input('Введите команду: ')

# КАЛЬКУЛЯТОР
if command == "калькулятор":
    
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
        print("Частное:", num1 / num2)
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
        
# МАКСИМУМ        
elif command == "максимум":
    print('Эта подпрограмма ищет максимум из трёх чисел')
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите первое число: '))
    num3 = float(input('Введите первое число: '))

    if num1 > num2:
        if num1 > num3:
            print(num1)
        else:
            print(num3)
    else:
        if num2 > num3:
            print(num2)
        else:
            print(num3)
# АНЕКДОТ            
elif command == "анекдот":
    print('Сел медведь в машину и сгорел')
else:
    print("Неизвестная команда")
