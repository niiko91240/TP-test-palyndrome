import unittest
from src.etape2.Ohce import Ohce
from src.etape2.Langues.LangueFrancaise import LangueFrancaise
from src.etape2.Langues.LangueAnglaise import LangueAnglaise
from datetime import datetime


class TestMain(unittest.TestCase):
    print('test')

    def test_bien_dit_fr(self):
        self.assertEqual(Ohce(LangueFrancaise).bien_dit(), 'Bien dit !')

    def test_bien_dit_en(self):
        self.assertEqual(Ohce(LangueAnglaise).bien_dit(), 'Well done !')

    def test_hello_morning_fr(self):
        date = datetime.now().replace(hour=10)
        self.assertEqual(Ohce(LangueFrancaise).bonjour(date), 'Allez on se réveille !')

    def test_hello_morning_en(self):
        date = datetime.now().replace(hour=10)
        self.assertEqual(Ohce(LangueAnglaise).bonjour(date), 'Wake up !')

    def test_hello_moon_fr(self):
        date = datetime.now().replace(hour=12)
        self.assertEqual(Ohce(LangueFrancaise).bonjour(date), 'Bonjour !')

    def test_hello_moon_en(self):
        date = datetime.now().replace(hour=12)
        self.assertEqual(Ohce(LangueAnglaise).bonjour(date), 'Hello !')

    def test_hello_aftermoon_fr(self):
        date = datetime.now().replace(hour=19)
        self.assertEqual(Ohce(LangueFrancaise).bonjour(date), 'Bonsoir !')

    def test_hello_aftermoon_en(self):
        date = datetime.now().replace(hour=19)
        self.assertEqual(Ohce(LangueAnglaise).bonjour(date), 'Good Evening !')







if __name__ == '__main__':
    unittest.main()