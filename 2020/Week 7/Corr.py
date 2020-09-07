def is_matrix_right(matrix):
    i = 99999
    if matrix == [[0,7,i,i,14,i,i,i ],
                     [i,0,8,i,i,i,i,i  ],
                     [i,i,0,6,i,i,i,i  ],
                     [18,i,i,0,i,11,i,i],
                     [i,i,i,i,0,19,i,i ],
                     [i,i,i,i,i,0,4,13 ],
                     [i,i,5,i,i,i,0,9  ],
                     [i,i,9,i,i,i,i,0  ]]:
        print("Votre matrice est correcte.")
    else:
        print("Il y a une erreur dans votre matrice.")

