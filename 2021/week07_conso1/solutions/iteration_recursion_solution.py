def nb_voyelles_itérative(T,S) :
    c = 0
    for i in T :
        if i in S :
            c += 1
        else :
            pass
    return c

def nb_voyelles_récursive(T,S) :
    if len(T) == 1 :
        if T[0] in S :
            return 1
        else :
            return 0
    else :
        if T[0] in S :
            return 1 + nb_voyelles_récursive(T[1:],S)
        else :
            return 0 + nb_voyelles_récursive(T[1:],S)

voyelles = ['a','e','i','o','u','y']
texte = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean molestie elit ipsum, a tincidunt urna aliquet\
 eget. Praesent et quam vitae justo hendrerit tristique. Ut malesuada ligula in mi ultricies tempor. Fusce blandit \
 turpis sapien, in gravida orci aliquet et. Morbi in metus efficitur, volutpat purus sit amet, scelerisque massa. \
 Vivamus vehicula justo quis leo feugiat fringilla. Maecenas sagittis ultrices accumsan. Cras libero est, gravida in\
  eros ac, luctus ullamcorper nisi."

print(nb_voyelles_itérative(texte,voyelles))
print(nb_voyelles_récursive(texte,voyelles))