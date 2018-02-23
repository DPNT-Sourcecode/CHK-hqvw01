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
        # contains an int
        self.assertEqual(checkout(u'HELL1OAAAAA'), -1)
        
    def test_checkout_9(self):
        # contains an int
        self.assertEqual(checkout(u'2'), -1)
        
    def test_checkout_10(self):
        # is an int!
        self.assertEqual(checkout(2), -1)
        
    def test_checkout_11(self):
        self.assertEqual(checkout(u'BBEE'), 110)
        
    def test_checkout_12(self):
        self.assertEqual(checkout(u'BBBEE'), 125) 
        
    def test_checkout_13(self):
        self.assertEqual(checkout(u'EEEEBB'), 160)
        
    def test_checkout_14(self):
        self.assertEqual(checkout(u'BEBEEE'), 160)    

    def test_checkout_15(self):
        self.assertEqual(checkout(u'F'), 10)   
        
    def test_checkout_16(self):
        self.assertEqual(checkout(u'FF'), 20)
        
    def test_checkout_17(self):
        self.assertEqual(checkout(u'FFF'), 20)
        
    def test_checkout_18(self):
        self.assertEqual(checkout(u'FFFF'), 30)
        
    def test_checkout_19(self):
        self.assertEqual(checkout(u'FFFFF'), 40) 
        
    def test_checkout_20(self):
        self.assertEqual(checkout(u'FFFFFF'), 40) 
        
    def test_checkout_21(self):
        # Check that the prices match the expected.  This should suffice.
        self.assertEqual(checkout(u'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 965)
        
    def test_checkout_22(self):
        self.assertEqual(checkout(u'HHHHHHHHHHHHHHH'), 125)
       
    def test_checkout_23(self):
        self.assertEqual(checkout(u'KKKK'), 300)
    
    def test_checkout_24(self):
        self.assertEqual(checkout(u'KKKKK'), 380)

    def test_checkout_25(self):
        self.assertEqual(checkout(u'NNN'), 120)
        
    def test_checkout_26(self):
        self.assertEqual(checkout(u'NNNM'), 120)
        
    def test_checkout_27(self):
        self.assertEqual(checkout(u'NNNNNNM'), 240)
        
    def test_checkout_28(self):
        self.assertEqual(checkout(u'NNNNNNMM'), 240)
        
    def test_checkout_29(self):
        self.assertEqual(checkout(u'QQQRRR'), 210)
        
    def test_checkout_30(self):
        self.assertEqual(checkout(u'RRRRRRRRRQQQQ'), 480)
        
    def test_checkout_31(self):
        self.assertEqual(checkout(u'UUU'), 120)
    







if __name__ == '__main__':
    unittest.main()
