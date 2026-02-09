import sys

if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) == 3:
        print(f"La somme de {sys.argv[1]} et {sys.argv[2]} est {int(sys.argv[1]) + int(sys.argv[2])}")
    else:
        print("Assurez-vous de passer deux arguments à votre programme")
