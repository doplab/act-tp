def recursion_2(L) :
    if len(L) == 1 :
        print(L[0])
    else :
        recursion_2(L[1:])
        print(L[0])
        recursion_2(L[1:])

Liste = ["J","adore","Python"]
recursion_2(Liste)