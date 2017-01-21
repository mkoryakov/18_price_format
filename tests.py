import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_int_type(self):
        price = format_price(2014)
        self.assertEqual(price, '2 014')

    def test_float_type(self):
        price = format_price(2014.0)
        self.assertEqual(price, '2 014')

    def test_true_string_type(self):
        price = format_price('2014.00')
        self.assertEqual(price, '2 014')

    def test_false_string_type(self):
        price1 = format_price('2014,')
        price2 = format_price('2014.00.')
        price3 = format_price('A2014')
        self.assertIsNone(price1)
        self.assertIsNone(price2)
        self.assertIsNone(price3)

    def test_list_type(self):
        price = format_price([2014])
        self.assertIsNone(price)

    def test_dict_type(self):
        price = format_price({'price': 2014})
        self.assertIsNone(price)


if __name__ == '__main__':
    unittest.main()
