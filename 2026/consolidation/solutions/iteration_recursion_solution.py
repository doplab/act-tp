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

texte = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean molestie elit ipsum, a tincidunt urna aliquet\
 eget. Praesent et quam vitae justo hendrerit tristique. Ut malesuada ligula in mi ultricies tempor. Fusce blandit \
 turpis sapien, in gravida orci aliquet et. Morbi in metus efficitur, volutpat purus sit amet, scelerisque massa. \
 Vivamus vehicula justo quis leo feugiat fringilla. Maecenas sagittis ultrices accumsan. Cras libero est, gravida in\
  eros ac, luctus ullamcorper nisi."

print(nb_voyelles_iterative(texte))
print(nb_voyelles_recursive(texte))
