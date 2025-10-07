import unittest
from main import remainder

class TestRemainder(unittest.TestCase):

    def test_remainder_success(self):
        # проверяем корректные случаи
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(25, 5), 0)
        self.assertEqual(remainder(7, 2), 1)

    def test_remainder_negative(self):
        # проверяем работу с отрицательными числами
        self.assertEqual(remainder(-7, 3), 2)
        self.assertEqual(remainder(7, -3), -2)

    def test_remainder_by_zero(self):
        # проверяем, что выбрасывается исключение при делении на ноль
        self.assertRaises(ValueError, remainder, 5, 0)

if __name__ == '__main__':
    unittest.main()
