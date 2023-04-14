L = [8,24,27,48,2,16,9,7,84,91]
dim = len(L)
svp = 0
for i in range(dim) :
    if L[i]  %2 == 0 :
        svp == svp + L[i]
print(svp)