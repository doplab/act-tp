def nb_voyelles_iterative(T,S) :
    c = 0
    for i in T :
        if i in S :
            c += 1
        else :
            pass
    return c

def nb_voyelles_recursive(T,S) :
    if len(T) == 1 :
        if T[0] in S :
            return 1
        else :
            return 0
    else :
        if T[0] in S :
            return 1 + nb_voyelles_recursive(T[1:],S)
        else :
            return 0 + nb_voyelles_recursive(T[1:],S)

voyelles = ['a','e','i','o','u','y']
texte = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean molestie elit ipsum, a tincidunt urna aliquet"

print(nb_voyelles_iterative(texte,voyelles))
print(nb_voyelles_recursive(texte,voyelles))