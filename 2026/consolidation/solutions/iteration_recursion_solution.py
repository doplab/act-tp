def nb_voyelles_iterative(text) :
    c = 0
    voyelles = ['a','e','i','o','u','y']
    
    for i in text:
        if i in voyelles:
            c += 1
    return c

def nb_voyelles_recursive(text) :
    voyelles = ['a','e','i','o','u','y']

    if len(text) == 0:
        return 0
    else:
        if text[0] in voyelles:
            return 1 + nb_voyelles_recursive(text[1:])
        else:
            return 0 + nb_voyelles_recursive(text[1:])

texte = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean molestie elit ipsum, a tincidunt urna aliquet"

print(nb_voyelles_iterative(texte))
print(nb_voyelles_recursive(texte))
