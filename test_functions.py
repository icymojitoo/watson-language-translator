import unittest

from functions import to_french, to_german

class TestFrench (unittest.TestCase):
    def test1(self):
        self.assertEqual(to_french("what is your name?"), "Quel est votre nom?")

class TestGerman (unittest.TestCase):
    def test1(self):
        self.assertEqual(to_german("what is your name?"), "Was ist dein Name?")

unittest.main()