import sys

if __name__ == '__main__':
  arguments = sys.argv
  if len(arguments) == 3:
    print("La somme de {} et {} est {}".format(sys.argv[1], sys.argv[2], int(sys.argv[1])+int(sys.argv[2])))
  else:
    print("Assurez-vous de passer deux arguments à votre programme")