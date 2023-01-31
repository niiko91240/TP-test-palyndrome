import datetime

now = datetime.datetime.now()

class Ohce():

    def __init__(self, langue):
        self.langue = langue

    def bien_dit(self):
        return self.langue.bien_dit()

    def bonjour(heure : datetime):
        texte = ""
        if (heure.hour < 11):
            texte = 'Allez on se réveille !'
        elif (heure.hour < 18):
            texte = 'Bonjour !'
        else:
            texte = 'Bonsoir !'
        return texte

    def aurevoir(heure : datetime):
        texte = ""
        if (heure.hour < 11):
            texte = 'On retourne se coucher !'
        elif (heure.hour < 18):
            texte = 'Bonne journée !'
        else:
            texte = 'Bonne soirée !'
        return texte

    def miror(self, string):
        reverse_text = string[::-1]
        if (reverse_text == string):
            print(self.bien_dit())
        return reverse_text






"""if __name__ == '__main__':
    ohce = Ohce(LangueAnglaise)
    print(ohce.langue.bien_dit())
    #print(ohce.bonjour(now))

    while (1):
        text = input('Saisissez un texte : ')
        if (text == 'quit'):
            print(ohce.aurevoir(now))
            break
        print(ohce.miror(text))"""
