import datetime

now = datetime.datetime.now()

class Ohce():


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

    def miror(string):
        reverse_text = string[::-1]
        if (reverse_text == string):
            print('Bien dit !')
        return reverse_text






if __name__ == '__main__':
    print(Ohce.bonjour(now))

    while (1):
        text = input('Saisissez un texte : ')
        if (text == 'quit'):
            print(Ohce.aurevoir(now))
            break
        print(Ohce.miror(text))
