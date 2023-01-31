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

    def test_recette_1(self):
        date = datetime.datetime.now().replace(hour=19)
        self.assertEqual(Ohce('en_GB').miror('kayak'), 'kayak')
        self.assertEqual(Ohce('en_GB').bonjour(date), 'Good Evening !')
        self.assertEqual(Ohce('en_GB').aurevoir(date), 'Good night !')

    def test_recette_2(self):
        date = datetime.datetime.now().replace(hour=10)
        self.assertEqual(Ohce('fr_FR').miror('test'), 'tset')
        self.assertEqual(Ohce('fr_FR').bonjour(date), 'Allez on se réveille !')
        self.assertEqual(Ohce('fr_FR').aurevoir(date), 'On retourne se coucher !')













if __name__ == '__main__':
    unittest.main()