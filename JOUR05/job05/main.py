def calcul_gardien(nb_marches, hauteur_marche_cm):
    resultat_cm = 7 * 5 * 2 * nb_marches * hauteur_marche_cm
    resultat_m = resultat_cm / 100
    print("Pour "+str(nb_marches)+" marches de "+str(hauteur_marche_cm)+" cm, le gardien parcours "+str(resultat_m)+" m par semaine.")
    
calcul_gardien(100, 15)