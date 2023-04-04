#проверка одного из двух элементов
n = int(input("Сколько элементов?: "))

najdeno = False
for i in range(n):
    slovo = input("Введите слово: ")
    if slovo == "мумурзик" or slovo == "пепешка":
        najdeno = True
        break

if najdeno == True:
    print("ОБНАРУЖЕНО ЗАПРЕЩЁННОЕ СЛОВО")
else:
    print("Всё хорошо")