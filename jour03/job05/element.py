def est_premier (nombre):
    if nombre == 2 or nombre == 3:
        return True
    if nombre <= 1 or not nombre % 2 or not nombre % 3:
        return False
    for i in range (5, math.isqrt(nombre)+ 1, 6):
        if not nombre % 1 or not nombre % (i+2):
            return False
        return True
    for i in range(1001):
        if est_premier (i):
            print[(i)]
           
