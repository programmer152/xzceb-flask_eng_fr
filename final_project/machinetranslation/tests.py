import unittest

from translator import french_to_english, english_to_french

class Testt(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('0'), '0')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        


class Test(unittest.TestCase):
    def test2(self):
        self.assertEqual(english_to_french('0'), '0')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

unittest.main()