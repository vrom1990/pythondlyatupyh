command = input('Введите команду: ')

if command == 'помощь':
    print('Введите одну из команд:')
    print('анекдот, сказка на ночь, важная новость,')
    print('список дел, сказка на ночь, важная новость,')
elif command == 'анекдот':
    print('Идёт как-то ёжик, а навстречу ему медведь',
          '— Доброе утро, медведь!',
          '— Доброе утро, ёжик!',
          'Вот так слово за слово, и получил ёжик по морде!',
          sep='\n')  
elif command == 'сказка на ночь':
    print('Жили были и жили они долго и счастливо')
elif command == 'важная новость':
    print('С камнем в лесу сегодня опять ничего не произошло')
elif command == 'список дел':
    print('''- Помыться
- Побриться
- Поесть
- Посмотреть новое видео от Вячеслава Романькова
- Написать ему, что он лучше всех на свете
- Перевести ему денег
- Лечь спать с ощущение, что вечер прошёл не зря''')
elif command == 'создать заметку':
    note = input('Введите текст заметки: ')
elif command == 'запомнить контакт':
    fio = input('Введите ФИО: ')
    phoneNumber = input('Введите номер телефона: ')
else:
   print('Неизвестная команда')
   
print('Конец программы.')