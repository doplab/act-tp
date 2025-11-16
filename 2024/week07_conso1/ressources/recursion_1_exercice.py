def recursion_1(S) :
    if len(S) == 1 :
        return S[0]
    else :
        return S[0] + recursion_1(S[1:]) + S[0]

print(recursion_1("Python"))