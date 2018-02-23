import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(50, checkout(u'A'))


if __name__ == '__main__':
    unittest.main()
