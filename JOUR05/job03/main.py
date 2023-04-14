def affiche_tapis(x):
    diagonale = x + 1
    for i in range(x + 3):
        ligne = ""
        for j in range(x + 3):
            if (i ==0 or i ==x + 2) and (j == 0 or j == x +2):
                ligne += "+"
            elif i == 0 or i == x +2:
                ligne +="-"
            elif j == 0 or j == x + 2:
                ligne += "|"
            elif j == diagonale:
                ligne += ""
                diagonale -= 1
            else:
                ligne += "#"
        print(ligne)
        
affiche_tapis(10)
print()
affiche_tapis(20)
         