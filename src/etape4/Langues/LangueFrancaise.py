from datetime import datetime

class LangueFrancaise:

    langue = 'Français'

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

    def aurevoir(heure: datetime):
        texte = ""
        if (heure.hour < 11):
            texte = 'On retourne se coucher !'
        elif (heure.hour < 18):
            texte = 'Bonne journée !'
        else:
            texte = 'Bonne soirée !'
        return texte