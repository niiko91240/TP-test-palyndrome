from datetime import datetime


class LangueAnglaise:

    langue = 'Anglais'

    def bien_dit():
        return 'Well done !'

    def bonjour(heure: datetime):
        texte = ""
        if (heure.hour < 11):
            texte = 'Wake up !'
        elif (heure.hour < 18):
            texte = 'Hello !'
        else:
            texte = 'Good Evening !'
        return texte

    def aurevoir(heure: datetime):
        texte = ""
        if (heure.hour < 11):
            texte = 'Have a good morning !'
        elif (heure.hour < 18):
            texte = 'Bye !'
        else:
            texte = 'Good night !'
        return texte