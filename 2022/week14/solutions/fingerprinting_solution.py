import base64

# num est un nombre entier
def is_a_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num**.5)):
        if num % i == 0:
            return False
    return True

# p est un nombre premier et message est une chaine de caractères
def fingerprinting(p, message):
    if is_a_prime_number(p):
        result = hash(message) % p
        return result
    print(str(p) + " is not a prime number!")

# password est une chaîne de caractères et your details est un tuple avec le 
# format suivant (nombre premier, hash du mot de passe)
def login(password, your_details):
    return your_details[1] % your_details[0] == fingerprinting(your_details[0], password)

if __name__ == "__main__":
    password = "ceciestmonmotdepasse"
    your_details = (19, hash(password))
    success = login(password, your_details)

    print("Connexion réussie? " + str(success))
    if success:
        message = '''SmUgc2VyYWlzIGNvbmZpbsOpIGNoZXogbWVzIHBhcmVudHMgw
                     6AgbGEgY2FtcGFnbmUgbGVzIGRldXggcHJvY2hhaW5lIHNlbWF
                     pbmVzLCBldCBqZSBuJ2F1cmFpcyBwYXMgYWNjw6hzIMOgIEludGV
                     ybmV0LiDDgCBiaWVudMO0dCE='''
        print(base64.b64decode(message).decode())