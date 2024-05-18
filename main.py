from password_class import Password, hide_password

try:
    pass_len = int(input('Укажите длину пароля (не менее 6 символов и не более 40 символов) '))
    if pass_len < 6:
        print('Ошибка: Длина пароля должна быть не меньше 6')
        exit()
    elif pass_len > 40:
        print('Ошибка: Слишком длинный пароль')
        exit()
except ValueError:
    print('Ошибка: необходимо ввести число')
    exit()

try:
    passwords_count = int(input('Укажите количество вариантов паролей (не более 10) '))
    if passwords_count < 1:
        print('Ошибка: Слишком маленькое количество паролей')
        exit()
    elif passwords_count > 10:
        print('Ошибка: Недопустимое количество вариантов')
        exit()
except ValueError:
    print('Ошибка: необходимо ввести число')
    exit()

try:
    user_choose = int(input('Настроить пароль? 1 - Да, 0 - Нет: '))
    if user_choose != 0 and user_choose != 1:
        print('Ошибка: Для ввода допустимы 1 или 0')
        exit()
except ValueError:
    print('Ошибка: необходимо ввести число')
    exit()

password_params = None

if user_choose == 1:
    try:
        upper = int(input('Добавить заглавные буквы? 1 - Да, 0 - Нет: '))
        if upper != 0 and upper != 1:
            print('Ошибка: Для ввода допустимы 1 или 0')
            exit()
    except ValueError:
        print('Ошибка: необходимо ввести число')
        exit()

    try:
        numbers = int(input('Добавить цифры? 1 - Да, 0 - Нет: '))
        if numbers != 0 and numbers != 1:
            print('Ошибка: Для ввода допустимы 1 или 0')
            exit()
    except ValueError:
        print('Ошибка: необходимо ввести число')
        exit()

    try:
        specials = int(input('Добавить спецсимволы? 1 - Да, 0 - Нет: '))
        if specials != 0 and specials != 1:
            print('Ошибка: Для ввода допустимы 1 или 0')
            exit()
    except ValueError:
        print('Ошибка: необходимо ввести число')
        exit()

    password_params = [upper, numbers, specials]


password = Password(pass_len, passwords_count, password_params)

password_result = password.generate_password()

if len(password_result) == 1:
    try:
        user_choose = int(input('Вывести пароль на экран или сохранить в файл? 1 - на экран, 0 - в файл: '))
        if user_choose != 0 and user_choose != 1:
            print('Ошибка: Для ввода допустимы 1 или 0')
            exit()
    except ValueError:
        print('Ошибка: необходимо ввести число')
        exit()

    if user_choose == 1:
        print(f'Ваш пароль: {password_result[0]}     {password.check_password(password_result[0])}')
        print(password.check_password('I?QL[UEiq'))
    else:
        secret_word = hide_password(password_result[0])
        all_passwords = ''
        with open('password.txt', 'a', encoding='utf-8') as open_file:
            open_file.write(password_result[0]+'\n')
        print(f'Пароль {secret_word} успешно сохранен')
else:
    print(f'Ваши пароли:')
    for p in password_result:
        print(f'{p}     {password.check_password(p)}')

