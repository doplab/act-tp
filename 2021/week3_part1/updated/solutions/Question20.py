import math

def aire(rayon):
  return (rayon**2)*math.pi

def perimetre(rayon):
  return 2*math.pi*rayon

if __name__ == '__main__':
    rayon = 10
    aire = aire(rayon)
    perimetre = perimetre(rayon)
    print("L'aire d'un cercle de rayon {} est égale à {}".format(rayon, aire))
    print("Le périmètre d'un cercle de rayon {} est égal à {}".format(rayon, perimetre))