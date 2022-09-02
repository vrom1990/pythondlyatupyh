num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
multiply = num1 * num2

if multiply > 0:
    print('Произведение положительно!')
elif multiply < 0:
    print('Произведение отрицательно!')
else:
    print('Произведение равно нулю')

print('Вот и сказочке конец, а кто слушал, тот не ноль')