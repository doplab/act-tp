import sys
if __name__ == '__main__':
    balance = 20
    try:
        balance = balance - sys.argv[1]
        solde_post = balance > 0
        match (solde_post):
            case True:
                print('Le solde de votre compte est positif.')
            case False:
                print('Le solde de votre compte est négatif ou zéro.')
                raise ValueError('Le compte ne peut pas être débité')
    except Exception as e:
        print("Une erreur est survenue")
    finally:
        print(f"Valeur finale de balance: {balance}")
