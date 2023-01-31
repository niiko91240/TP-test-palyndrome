from datetime import datetime

class LangueFrancaise:

    def bien_dit():
        return 'Bien dit !'

    def bonjour(heure: datetime):
        texte = ""
        if (heure.hour < 11):
            texte = 'Allez on se réveille !'
        elif (heure.hour < 18):
            texte = 'Bonjour !'
        else:
            texte = 'Bonsoir !'
        return texte

