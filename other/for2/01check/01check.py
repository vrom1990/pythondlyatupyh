#проверка наличия элемента
n = int(input("Сколько элементов?: "))

najdeno = False
for i in range(n):
    slovo = input("Введите слово: ")
    if slovo == "мумурзик":
        najdeno = True
        break

if najdeno == True:
    print("Такое слово есть")
else:
    print("Такого слова нет")