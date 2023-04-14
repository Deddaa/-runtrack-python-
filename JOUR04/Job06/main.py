L =["a","b","c","d","e","f"]
ma_variable = L[0]

L[0] = L[-1]

L[-1] = ma_variable

print(L)
