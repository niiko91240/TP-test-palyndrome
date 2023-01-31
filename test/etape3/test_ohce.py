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

    def test_bonjour_fr(self):
        date = datetime.now().replace(hour=10)
        print(self.string.format(LangueFrancaise.langue,Ohce(LangueFrancaise).periode(date),Ohce(LangueFrancaise).bonjour(date)))
        self.assertEqual(Ohce(LangueFrancaise).bonjour(date), 'Allez on se réveille !')







if __name__ == '__main__':
    unittest.main()