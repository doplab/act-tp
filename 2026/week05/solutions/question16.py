if __name__ == '__main__':
    notes_biologie = {"Charlie": 5, "Alice": 6, "Bob": 5.5}
    notes_chimie = {"Charlie": 4, "Alice": 5, "Bob": 6}
    
    # Votre code ici:
    notes_combinees = {}
    for etudiant in notes_biologie:
        notes_combinees[etudiant] = [notes_biologie[etudiant], notes_chimie[etudiant]]
    
    # Résultat:
    print(notes_combinees)
    # {"Charlie": [5, 4], "Alice": [6, 5], "Bob": [5.5, 6]}

    # Partie 2
    cnt = 0
    for val in notes_combinees.values():
        if (val[0]+val[1])/2.0 > 5:
            cnt += 1
    print(cnt) # affiche 2
