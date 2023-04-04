#проверка — есть ли элемент из диапазона
n = int(input("Сколько элементов?: "))

najdeno = False
for i in range(n):
    num = float(input("Введите число: "))
    if 2 <= num and num <= 5:
        najdeno = True
        break

if najdeno == True:
    print("Число в заданном диапазоне найдено")
else:
    print("Таких чисел нет")
