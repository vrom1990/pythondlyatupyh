print('Здравствуйте, это конвертер!')
print('Введите число, которое нужно конвертировать')
number = float(input('Введите число: '))
print('Введите пару единиц измерения (из чего во что преобразовывать), либо команду «помощь»')
command = input('Введите пару либо команду: ')

if command == 'кг-фунт':
    print(number/0.45359237, 'в фунтах')
elif command == 'фунт-кг':
    print(number*0.45359237, 'в киллограмах')
elif command == 'цельсий-фаренгейт':
    print(number*9/5+32, 'в фаренгейтах')
elif command == 'фаренгейт-цельсий':
    print((number-32)/9*5, 'в цельсиях')
elif command == 'помощь':
    print('Есть команды: помощь, кг-фунт, фунт-кг, цельсий-фаренгейт,',
          'фаренгейт-цельсий')
else:
    print('Ошибка! Неверная команда')
    
print('Спасибо за использование конвертера')