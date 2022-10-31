def check_name(nom):
   
    if type(nom) != str or nom == "":
        raise ValueError("Invalid type of argument")
    else:
        print("Bonjour", nom)
    

