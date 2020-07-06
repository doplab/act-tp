# Exercice 16
def extraire_longs_mots(sentence):
    # sentence.split(' ') retourne la liste des mots qui sont séparés par un espace
    words = [word.lower() for word in sentence.split(' ') if len(word) > 3]
    # lower() permet de mettre chaque mot en miniscule
    words = sorted(words)
    # la fonction sorted prends une liste en paramètre et renvoie la liste triée. Par défaut, sorted renvoie une liste d'éléments triés par ordre alphabétique (pour des chaînes de caractères)
    return ','.join(words)

print(extraire_longs_mots('Je Suis Content'))
