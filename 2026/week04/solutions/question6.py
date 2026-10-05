import math

def aire(rayon):
  return (rayon**2)*math.pi

def perimetre(rayon):
  return 2*math.pi*rayon

if __name__ == '__main__':
    rayon = 10
    aire_resultat = aire(rayon)
    perimetre_resultat = perimetre(rayon)
    print(f"L'aire d'un cercle de rayon {rayon} est égale à {aire_resultat}")
    print(f"Le périmètre d'un cercle de rayon {rayon} est égal à {perimetre_resultat}")