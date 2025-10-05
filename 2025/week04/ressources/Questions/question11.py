import sys
if __name__ == '__main__':
    balance = 20
    try:
        balance = 20 - sys.argv[1]
    except Exception as e:
        print("Une erreur est survenue")
    finally:
        print(f"Valeur finale de balance: {balance}")
