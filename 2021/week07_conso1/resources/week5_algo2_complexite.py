# L liste de nombres entiers
def algo2(L):
    n = len(L)

    for i in range(n):
        for j in range(n):
            if i != j and L[i] == L[j]:
                return True
    
    return False