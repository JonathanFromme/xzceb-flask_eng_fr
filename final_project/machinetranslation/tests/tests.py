import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual('bonjour', english_to_french('hello'))
        self.assertNotEqual('hello', english_to_french('hello'))
        

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual('hello', french_to_english('bonjour'))
        self.assertNotEqual('bonjour', french_to_english('bonjour'))

unittest.main()