print("Здравствуйте!")
print("Вы позвонили в «Оса Телеком»")
print("Чтобы узнать подробности о тарифах, балансе и подключённых услугах, нажмите 1")
print("Чтобы узнать новые интересные предложения, нажмите 2")
print("Чтобы подключить или отключить подписки, нажмите 3")
print("Для связи с оператором нажмите 0")

num = input("Ввод цифры: ")
if num == "1":
    print("Чтобы узнать, какой тариф у вас сейчас, нажмите 1")
    print("Чтобы узнать, какие есть тарифы, нажмите 2")
    print("Чтобы узнать баланс, нажмите 3")
    print("Чтобы узнать список подключённых услуг, нажмите 4")
    print("Чтобы подключить или отключить услугу, нажмите 5")
    print("Чтобы вернуться к началу, нажмите 0")
    num = input("Ввод цифры: ")
    if num == "1":
        print("У вас тариф ЗАБУБЕННЫЙ")
    elif num == "2":
        print("У нас есть тарифы НИЧЕГО ТАК, ХОРОШЕЧНО, ЗАБУБЕННЫЙ и ЛОХ")
    elif num == "3":
        print("Ваш баланс -200 тугриков")
        print("Если хотите пополнить баланс, нажмите 1")
        print("Если хотите вернуться в основное меню, нажмите 0")
        num = input("Ввод числа: ")
        if num == "1":
            summa = input("Введите сумму пополнения")
            print("Вы пополнили баланс на ", summa, ", теперь он равен", summa-200, "тугриков.", sep ='')
    elif num == "4":
        print("У вас подключены услуги 'Совсем ничего' и '0 когда 0', а так же подписка «Вечерний Илон Маск» ")
    elif num == "5":
        print("Чтобы отключить или подключить услугу 'Совсем ничего', нажмите 1")
        print("Чтобы отключить или подключить услугу '0 когда 0', нажмите 2")
        print("Чтобы отключить или подключить услугу 'Ну привет', нажмите 3")
        print("Нажмите 0, чтобы забыть это как страшный сон")
        num = input("Ввод цифры")
        if num == "1":
            print("услуга «Совсем ничего» отключена")
        elif num == "2":
            print("услуга «0 когда 0» отключена")
        elif num == "3":
            print("услуга «Ну привет» отключена")
        elif num == "0":
            print("Ничего не было")
    elif num == "0":
        print("Итак, ещё раз...")
    else:
        print("Неправильный ввод")
elif num == "2":
    print("Предлагаем новый тариф «Лох». Работает как получится, платите сколько скажут")
    print("Чтобы подключить тариф «Лох», нажмите решётку")
    print("Чтобы прослушать всё с начала, нажмите 0")
    num = input("Ввод цифры")
    if num == "#":
        print("Тариф «Лох» успешно подключён")
    elif num == "0":
        print("Прослушайте всё сначала")
    else:
        print("Неправильный ввод")
elif num == "3":
    print("Чтобы отключить/подключить подписку на погоду, нажмите 1")
    print("Чтобы отключить/подключить подписку «Вечерний Маск», нажмите 2")
elif num == "0":
    print("Все операторы заняты!")
    print("Примерное время ожидания 10000 минут!")
    print("Оставайтесь на линии, ваш звонок очень важен для нас!")
else:
    print("Неправильный ввод")