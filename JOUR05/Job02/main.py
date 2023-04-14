def draw_rectangle (width, height):
    for i in range(height):
        ligne = ""
        for j in range(width):
            if j == 0 or j == width - 1:
                ligne += "|"
            elif i != 0 and i != height -1:
                ligne +=" " 
            else:
                ligne +="-"
        print(ligne)
        
        
draw_rectangle(10, 3)
print()












