command = input("Введите команду: ")

while command != "выход":
    if command == "+":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print("Сумма", num1+num2)
    elif command == "-":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print("Разность", num1-num2)
    elif command == "*":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print("Произведение", num1*num2)
    elif command == "/":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print("Частное", num1/num2)
    else:
        print("Неизвестная команда")
    
    command = input("Введите команду: ")

print("Калькулятор закрыт")