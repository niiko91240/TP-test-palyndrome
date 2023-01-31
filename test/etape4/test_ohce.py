import unittest
from src.etape3.Ohce import Ohce
from src.etape3.Langues.LangueFrancaise import LangueFrancaise
from src.etape3.Langues.LangueAnglaise import LangueAnglaise
from datetime import datetime
import locale


class TestMain(unittest.TestCase):

    def test_langue_systeme(self):
        langue_systeme = locale.getdefaultlocale()[0]
        if(langue_systeme == 'en_GB'):
            self.assertEqual(Ohce(langue_systeme).bien_dit(), 'Wake up !')
        else:
            self.assertEqual(Ohce(langue_systeme).bien_dit(), 'Allez on se réveille !')










if __name__ == '__main__':
    unittest.main()