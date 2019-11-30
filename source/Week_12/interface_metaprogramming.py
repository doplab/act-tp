class InterfaceChecker(type):
    def __init__(self, _, __, dic):
        methods = {
            "move": ("speed",),
            ""
        }
        
        for i in methods:
            if i not in dic:
                raise Exception("VOUS N'AVEZ PAS IMPLÉMENTÉ TOUTES LES MÉTHODES DE L'INTERFACE")
            elif dic[i].__code__.co_varnames != methods[i]:
                raise Exception("La méthode %s n'a pas implémenté les bons arguments" % i)