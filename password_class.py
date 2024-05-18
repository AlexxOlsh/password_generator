import string
import secrets
import random


def hide_password(password):
    secret_word = ''
    for c in password:
        secret_word += '*'
    return secret_word


class Password:
    # params Uppercase, numbers, specials
    def __init__(self, pass_len, passwords_count, params=None):
        if params is None:
            params = [0, 0, 0]
        self.pass_len = pass_len
        self.params = params
        self.symbols = string.ascii_lowercase
        self.passwords_count = passwords_count

        if self.params[0] == 1:
            self.symbols += f'{string.ascii_uppercase}'

        if self.params[1] == 1:
            self.symbols += f'{(string.digits)}'

        if self.params[2] == 1:
            self.symbols += f'{string.punctuation}'

        self.symbols = ''.join(random.sample(self.symbols, len(self.symbols)))

    def generate_password(self):
        passwords = []
        password = ''
        symbols_count = 0
        upper_count = 0
        lower_count = 0
        numbers_count = 0
        for i in range(self.passwords_count):
            while len(password) < self.pass_len:
                ch = secrets.choice(self.symbols)
                if ch.islower():
                    lower_count += 1
                if self.params[0] and ch.isupper():
                    upper_count += 1
                elif self.params[1] == 1 and ch.isdigit():
                    numbers_count += 1
                elif self.params[2] == 1 and string.punctuation.find(ch) != -1:
                    symbols_count += 1

                if len(password) > self.pass_len/2:
                    if self.params[0] == 1 and upper_count == 0:
                        password += f'{(secrets.choice(string.ascii_uppercase))}'
                        upper_count += 1
                    elif self.params[1] == 1 and numbers_count == 0:
                        password += f'{(secrets.choice(string.digits))}'
                        numbers_count += 1
                    elif self.params[2] == 1 and symbols_count == 0:
                        password += f'{(secrets.choice(string.punctuation))}'
                        symbols_count += 1
                    else:
                        password += f'{(secrets.choice(self.symbols))}'
                else:
                    password += f'{(secrets.choice(self.symbols))}'

            # passwords.append([password, lower_count, upper_count, numbers_count, symbols_count])
            passwords.append(password)
            lower_count = 0
            upper_count = 0
            numbers_count = 0
            symbols_count = 0
            password = ''

        # return [passwords, lower_count, upper_count, numbers_count, symbols_count]
        return passwords

    def check_password(self, password):
        res = 0
        symbols_count = 0
        upper_count = 0
        numbers_count = 0
        if self.pass_len > 8:
            res = 1

        for ch in password:
            if self.params[0] and ch.isupper():
                upper_count += 1
            elif self.params[1] == 1 and ch.isdigit():
                numbers_count += 1
            elif self.params[2] == 1 and string.punctuation.find(ch) != -1:
                symbols_count += 1

        if upper_count > 0:
            res += 1

        if numbers_count > 0:
            res += 1

        if symbols_count > 0:
            res += 1

        if res > 3:
            return 'Сложный'

        if res > 2:
            return 'Средняя сложность'

        if res <= 2:
            return 'Легкий'
