import datetime

now = datetime.datetime.now()

class Ohce():

    def __init__(self, langue):
        self.langue = langue

    def periode(self, heure : datetime):
        if(heure.hour < 11):
            return 'MATIN'
        elif(heure.hour < 18):
            return 'JOURNEE'
        else:
            return 'SOIR'

    def bien_dit(self):
        return self.langue.bien_dit()

    def bonjour(self, heure : datetime):
        return self.langue.bonjour(heure)

    def aurevoir(self, heure : datetime):
        return self.langue.aurevoir(heure)

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
