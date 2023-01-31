import unittest
from src.etape1.Ohce import Ohce
from datetime import datetime


class TestMain(unittest.TestCase):
    print('test')

    def test_hello_morning(self):
        date = datetime.now().replace(hour=10)
        self.assertEqual(Ohce.bonjour(date), 'Allez on se réveille !')

    def test_hello_moon(self):
        date = datetime.now().replace(hour=12)
        self.assertEqual(Ohce.bonjour(date), 'Bonjour !')

    def test_hello_afternoon(self):
        date = datetime.now().replace(hour=19)
        self.assertEqual(Ohce.bonjour(date), 'Bonsoir !')

    def test_goodbye_morning(self):
        date = datetime.now().replace(hour=10)
        self.assertEqual(Ohce.aurevoir(date), 'On retourne se coucher !')

    def test_goodbye_moon(self):
        date = datetime.now().replace(hour=14)
        self.assertEqual(Ohce.aurevoir(date), 'Bonne journée !')

    def test_goodbye_afternoon(self):
        date = datetime.now().replace(hour=19)
        self.assertEqual(Ohce.aurevoir(date), 'Bonne soirée !')

    def test_mirror_true(self):
        self.assertEqual(Ohce.miror('kayak'), 'kayak')

    def test_mirror_false(self):
        self.assertEqual(Ohce.miror('test'), 'tset')





if __name__ == '__main__':
    unittest.main()