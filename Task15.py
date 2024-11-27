def send_email(*, message=None, recipient=None, sender='alexa2005@gmail.com'):
    valid_domains = ['gmail.com', 'mail.ru', 'yandex.ru', 'rambler.ru', 'hotmail.com', 'outlook.com',
                     'yahoo.com', 'aol.com', 'protonmail.com', 'iCloud.com', 'inbox.ru', 'bk.ru', 'list.ru',
                     'ukr.net', 'zoho.com', 'qq.com', '163.com', 'live.com', 'me.com',
                     'fastmail.com']  # Список правильных доменов

    while True:
        new_sender = input(
            'Хотите ли вы использовать адрес отправителя по умолчанию?(Y/N) ~~~alexa2005@gmail.com~~~\n').upper()

        # Если пользователь не захотел адрес отправителя по умолчанию
        if new_sender == 'N' or new_sender == 'NO':
            print()
            while True:
                # Ввод адреса отправителя, а также проверка на пустой текст, домен и формат
                sender = input('Введите новый адрес отправителя: ')
                if not sender.strip():
                    print('\nАдрес не может быть пустым!')
                    continue
                elif not '@' in sender:
                    print("\nНеверный формат адреса отправителя! Проверьте правильность введенных данных")
                    continue
                elif not any(sender.endswith(domains) for domains in valid_domains):
                    print('\nДомен не входит в список разрешенных! Проверьте правильность введенных данных')
                    continue
                else:
                    print(f'\nНовый адрес отправителя: {sender}')
                    break
            break

        # Если пользователь выбрал адрес отправителя по умолчанию
        elif new_sender == 'Y' or new_sender == 'YES':
            print('\nВы выбрали адрес отправителя по умолчанию')
            break

        # Если пользователь ввел неверную команду
        else:
            print('\nНеверная команда')
            continue

    while True:
        # Ввод адреса получателя, а также проверка на пустой текст, домен, формат и одинаковый адрес отправителя и получателя
        recipient = input('\nВведите адрес получателя: ')
        if not sender.strip():
            print('\nАдрес не может быть пустым!')
            continue
        elif not '@' in recipient:
            print("\nНеверный формат адреса получателя! Проверьте правильность введенных данных")
            continue
        elif not any(recipient.endswith(domain) for domain in valid_domains):
            print('\nДомен не входит в список разрешенных! Проверьте правильность введенных данных')
            continue
        elif recipient == sender:
            print('\nНельзя отправлять письма самому себе!')
            continue
        else:
            break

    message = input('\nВведите сообщение:\n')

    # Проверка на совпадение адреса отправителя по умолчанию с текущим
    if sender != 'alexa2005@gmail.com':
        print(f'\nНЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!\nПисьмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'\nПисьмо успешно отправлено с адреса {sender} на адрес {recipient}.')


send_email()