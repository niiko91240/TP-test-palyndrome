import unittest
from src.etape2.Ohce import Ohce
from src.etape2.Langues.LangueFrancaise import LangueFrancaise
from src.etape2.Langues.LangueAnglaise import LangueAnglaise
from datetime import datetime


class TestMain(unittest.TestCase):

    string = 'ETANT DONNE un utilisateur parlant la langue {} '
    string += '\n ET que la periode de la journée est {}'
    string += '\n QUAND on saisit une chaine'
    string += '\n ALORS {} de cette langue à cette période est envoyée avant tout'

    def test_bonjour_morning_fr(self):
        date = datetime.now().replace(hour=10)
        print(self.string.format(LangueFrancaise.langue, Ohce(LangueFrancaise).periode(date),
                                 Ohce(LangueFrancaise).bonjour(date)))
        self.assertEqual(Ohce(LangueFrancaise).bonjour(date), 'Allez on se réveille !')

    def test_bonjour_morning_en(self):
        date = datetime.now().replace(hour=10)
        print(self.string.format(LangueAnglaise.langue, Ohce(LangueAnglaise).periode(date),
                                 Ohce(LangueAnglaise).bonjour(date)))
        self.assertEqual(Ohce(LangueAnglaise).bonjour(date), 'Have a good morning !')

    def test_bonjour_moon_fr(self):
        date = datetime.now().replace(hour=12)
        print(self.string.format(LangueFrancaise.langue, Ohce(LangueFrancaise).periode(date),
                                 Ohce(LangueFrancaise).bonjour(date)))
        self.assertEqual(Ohce(LangueFrancaise).bonjour(date), 'Bonjour !')

    def test_bonjour_moon_en(self):
        date = datetime.now().replace(hour=12)
        print(self.string.format(LangueAnglaise.langue, Ohce(LangueAnglaise).periode(date),
                                 Ohce(LangueAnglaise).bonjour(date)))
        self.assertEqual(Ohce(LangueAnglaise).bonjour(date), 'Hello !')

    def test_bonjour_afternoon_fr(self):
        date = datetime.now().replace(hour=19)
        print(self.string.format(LangueFrancaise.langue, Ohce(LangueFrancaise).periode(date),
                                 Ohce(LangueFrancaise).bonjour(date)))
        self.assertEqual(Ohce(LangueFrancaise).bonjour(date), 'Bonsoir !')

    def test_bonjour_afternoon_en(self):
        date = datetime.now().replace(hour=19)
        print(self.string.format(LangueAnglaise.langue, Ohce(LangueAnglaise).periode(date),
                                 Ohce(LangueAnglaise).bonjour(date)))
        self.assertEqual(Ohce(LangueAnglaise).bonjour(date), 'Good Evening !')










if __name__ == '__main__':
    unittest.main()