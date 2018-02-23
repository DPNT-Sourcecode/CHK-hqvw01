import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout_1(self):
        self.assertEqual(50, checkout(u'A'))
        
    def test_checkout_2(self):
        self.assertEqual(130, checkout(u'AAA'))
        
    def test_checkout_3(self):
        self.assertEqual(180, checkout(u'AAAA'))
        
    def test_checkout_4(self):
        self.assertEqual(checkout(u'AAAAABABBB'), 350)
        
    def test_checkout_5(self):
        self.assertEqual(checkout(u'AAAAABABBBA'), 400)


if __name__ == '__main__':
    unittest.main()
