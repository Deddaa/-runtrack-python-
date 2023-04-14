def calcul_prochain_multiple(n):
    while n % 5:
        n += 1
    return n

def arrondir_notes(liste_notes):
    liste_notes_arrondies = []
    for note in liste_notes:
        if note > 40:
            prochain_multiple = calcul_prochain_multiple(note)
            if (prochain_multiple - note < 3):
                note = prochain_multiple
        liste_notes_arrondies.append(note)
    return liste_notes_arrondies

print(arrondir_notes([83, 82, 43, 42]))