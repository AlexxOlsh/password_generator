import unittest
from password_class import Password


class TestGame(unittest.TestCase):

    def test_generate_password_single(self):
        password = Password(8, 1,[1, 0, 0])
        password_result = password.generate_password()

        self.assertEqual(len(password_result[0]), 8)

    def test_generate_password_six_passwords(self):
        password = Password(8, 3,[1, 0, 0])
        password_result = password.generate_password()
        self.assertEqual(len(password_result[0]), 8)
        self.assertEqual(len(password_result[1]), 8)
        self.assertEqual(len(password_result[2]), 8)
        self.assertEqual(len(password_result), 3)

    def test_check_password_simple(self):
        password = Password(8, 1,[1, 0, 0])
        temp_pass = 'tfMvRkFq'

        self.assertEqual(password.check_password(temp_pass), 'Легкий')

    def test_check_password_simple_twoparams(self):
        password = Password(8, 1, [1, 0, 1])
        temp_pass = ';HvE`K=]'

        self.assertEqual(password.check_password(temp_pass), 'Легкий')

    def test_check_password_middle(self):
        password = Password(9, 1, [1, 0, 1])
        temp_pass = 'I?QL[UEiq'

        self.assertEqual(password.check_password(temp_pass), 'Средняя сложность')

    def test_check_password_hard(self):
        password = Password(9, 1, [1, 1, 1])
        temp_pass = 'I?QL[U8iq'

        self.assertEqual(password.check_password(temp_pass), 'Сложный')


if __name__ == '__test_password_class__':
    unittest.main()