import unittest
from src.etape4.Ohce import Ohce
from src.etape4.Langues.LangueFrancaise import LangueFrancaise
from src.etape4.Langues.LangueAnglaise import LangueAnglaise
import datetime
import locale


class TestMain(unittest.TestCase):

    langue_systeme = locale.getdefaultlocale()[0]

    def test_langue_systeme(self):

        if(self.langue_systeme == 'en_GB'):
            self.assertEqual(Ohce(self.langue_systeme).bien_dit(), 'Well done !')
        else:
            self.assertEqual(Ohce(self.langue_systeme).bien_dit(), 'Bien dit !')

    def test_heure_systeme(self):
        now = datetime.datetime.now()
        if(now.hour < 11):
            self.assertEqual(Ohce(self.langue_systeme).periode(now), 'MATIN')
        elif(now.hour < 18):
            self.assertEqual(Ohce(self.langue_systeme).periode(now), 'JOURNEE')
        else:
            self.assertEqual(Ohce(self.langue_systeme).periode(now), 'SOIR')










if __name__ == '__main__':
    unittest.main()