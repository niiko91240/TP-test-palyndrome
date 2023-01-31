import unittest
from src.etape3.Ohce import Ohce
from src.etape3.Langues.LangueFrancaise import LangueFrancaise
from src.etape3.Langues.LangueAnglaise import LangueAnglaise
from datetime import datetime


class TestMain(unittest.TestCase):

    string_bonjour = 'ETANT DONNE un utilisateur parlant la langue {} '
    string_bonjour += '\n ET que la periode de la journée est {}'
    string_bonjour += '\n QUAND on saisit une chaine'
    string_bonjour += '\n ALORS {} de cette langue à cette période est envoyée avant tout'

    string_aurevoir = 'ETANT DONNE un utilisateur parlant la langue {} '
    string_aurevoir += '\n ET que la periode de la journée est {}'
    string_aurevoir += '\n QUAND on saisit une chaine'
    string_aurevoir += '\n ALORS {} de cette langue à cette période est envoyée en dernier'

    def test_bonjour_morning_fr(self):
        date = datetime.now().replace(hour=10)
        print(self.string_bonjour.format(LangueFrancaise.langue, Ohce(LangueFrancaise).periode(date),
                                 Ohce(LangueFrancaise).bonjour(date)))
        self.assertEqual(Ohce(LangueFrancaise).bonjour(date), 'Allez on se réveille !')

    def test_bonjour_morning_en(self):
        date = datetime.now().replace(hour=10)
        print(self.string_bonjour.format(LangueAnglaise.langue, Ohce(LangueAnglaise).periode(date),
                                 Ohce(LangueAnglaise).bonjour(date)))
        self.assertEqual(Ohce(LangueAnglaise).bonjour(date), 'Wake up !')

    def test_bonjour_moon_fr(self):
        date = datetime.now().replace(hour=12)
        print(self.string_bonjour.format(LangueFrancaise.langue, Ohce(LangueFrancaise).periode(date),
                                 Ohce(LangueFrancaise).bonjour(date)))
        self.assertEqual(Ohce(LangueFrancaise).bonjour(date), 'Bonjour !')

    def test_bonjour_moon_en(self):
        date = datetime.now().replace(hour=12)
        print(self.string_bonjour.format(LangueAnglaise.langue, Ohce(LangueAnglaise).periode(date),
                                 Ohce(LangueAnglaise).bonjour(date)))
        self.assertEqual(Ohce(LangueAnglaise).bonjour(date), 'Hello !')

    def test_bonjour_afternoon_fr(self):
        date = datetime.now().replace(hour=19)
        print(self.string_bonjour.format(LangueFrancaise.langue, Ohce(LangueFrancaise).periode(date),
                                 Ohce(LangueFrancaise).bonjour(date)))
        self.assertEqual(Ohce(LangueFrancaise).bonjour(date), 'Bonsoir !')

    def test_bonjour_afternoon_en(self):
        date = datetime.now().replace(hour=19)
        print(self.string_bonjour.format(LangueAnglaise.langue, Ohce(LangueAnglaise).periode(date),
                                 Ohce(LangueAnglaise).bonjour(date)))
        self.assertEqual(Ohce(LangueAnglaise).bonjour(date), 'Good Evening !')

    def test_aurevoir_morning_fr(self):
        date = datetime.now().replace(hour=10)
        print(self.string_bonjour.format(LangueFrancaise.langue, Ohce(LangueFrancaise).periode(date),
                                 Ohce(LangueFrancaise).aurevoir(date)))
        self.assertEqual(Ohce(LangueFrancaise).aurevoir(date), 'On retourne se coucher !')

    def test_aurevoir_morning_en(self):
        date = datetime.now().replace(hour=10)
        print(self.string_bonjour.format(LangueAnglaise.langue, Ohce(LangueAnglaise).periode(date),
                                 Ohce(LangueAnglaise).aurevoir(date)))
        self.assertEqual(Ohce(LangueAnglaise).aurevoir(date), 'Have a good morning !')

    def test_aurevoir_moon_fr(self):
        date = datetime.now().replace(hour=12)
        print(self.string_bonjour.format(LangueFrancaise.langue, Ohce(LangueFrancaise).periode(date),
                                 Ohce(LangueFrancaise).aurevoir(date)))
        self.assertEqual(Ohce(LangueFrancaise).aurevoir(date), 'Bonne journée !')

    def test_aurevoir_moon_en(self):
        date = datetime.now().replace(hour=12)
        print(self.string_bonjour.format(LangueAnglaise.langue, Ohce(LangueAnglaise).periode(date),
                                 Ohce(LangueAnglaise).aurevoir(date)))
        self.assertEqual(Ohce(LangueAnglaise).aurevoir(date), 'Bye !')

    def test_aurevoir_afternoon_fr(self):
        date = datetime.now().replace(hour=19)
        print(self.string_bonjour.format(LangueFrancaise.langue, Ohce(LangueFrancaise).periode(date),
                                 Ohce(LangueFrancaise).aurevoir(date)))
        self.assertEqual(Ohce(LangueFrancaise).aurevoir(date), 'Bonne soirée !')

    def test_aurevoir_afternoon_en(self):
        date = datetime.now().replace(hour=19)
        print(self.string_bonjour.format(LangueAnglaise.langue, Ohce(LangueAnglaise).periode(date),
                                 Ohce(LangueAnglaise).aurevoir(date)))
        self.assertEqual(Ohce(LangueAnglaise).aurevoir(date), 'Good night !')










if __name__ == '__main__':
    unittest.main()