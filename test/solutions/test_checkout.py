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
        self.assertEqual(checkout(u'AAAAABABBB'), 340)
        
    def test_checkout_5(self):
        self.assertEqual(checkout(u'AAAAABABBBA'), 390)
        
    def test_checkout_6(self):
        self.assertEqual(checkout(u'ABCDABCDA'), 245)
        
    def test_checkout_7(self):
        # Not unicode
        self.assertEqual(checkout("AAAA"), -1)
        
    def test_checkout_8(self):
        self.assertEqual(checkout(u'HELLOAAAAA'), -1)
        
    def test_checkout_9(self):
        self.assertEqual(checkout(u'2'), -1)
        
    def test_checkout_10(self):
        self.assertEqual(checkout(2), -1)
        
    def test_checkout_11(self):
        self.assertEqual(checkout(u'BBEE'), 110)
        
    def test_checkout_12(self):
        self.assertEqual(checkout(u'BBBEE'), 125)    


if __name__ == '__main__':
    unittest.main()
