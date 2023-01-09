command = input("Введите команду: ")

while command != "выход":
    if command == "сказка":
        print("Жили были и жили они долго и счастливо")
    elif command == "анекдот":
        print("Идёт как-то медведь по лесу.")
        print("Видит — машина горит.")
        print("Сел в неё и сгорел.")
    elif command == "мудрый совет":
        print("Ходи зимой в двух штанах.")

    elif command == "калькулятор":
        commandcalc = input("Введите команду калькулятора: ")

        while commandcalc != "выход":
            if commandcalc == "+":
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                print("Сумма", num1+num2)
            elif commandcalc == "-":
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                print("Разность", num1-num2)
            elif commandcalc == "*":
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                print("Произведение", num1*num2)
            elif commandcalc == "/":
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                print("Частное", num1/num2)
            else:
                print("Неизвестная команда")
            
            commandcalc = input("Введите команду калькулятора: ")

        print("Калькулятор закрыт")
    
    else:
        print("Не понимаю")
        
        
    command = input("Введите команду: ")
        

print("До свидания, котик")