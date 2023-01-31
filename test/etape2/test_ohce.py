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







if __name__ == '__main__':
    unittest.main()