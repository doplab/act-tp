def fonction_p(x) :
    if x == 0 :
        pass
    else :
        fonction_p(x-1)
        print(x)

fonction_p(5)