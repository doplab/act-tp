def fct_a(mot) :

if len(mot) == 1 :
	if mot[0] == "a" :
        	return 1
        else :
        	return 0
else :
	if mot[0] == "a" :
        	return 1 + fct_a(mot[1:])
        else :
        	return 0 + fct_a(mot[1:])

print(fct_a("blablabla"))