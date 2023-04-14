def chiffrage_cesar(message, décalage):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message_décalé = ""
    for lettre in message:
        index_lettre = alphabet.index(lettre)
        index_lettre_décalée = index_lettre + décalage
        lettre_décalée = alphabet[index_lettre_décalée % 26]
        message_décalé += lettre_décalée
    return message_décalé

print(chiffrage_cesar("abc", 1))
print(chiffrage_cesar("abc", 2))
print(chiffrage_cesar("xyz", 3))
print(chiffrage_cesar("abc", -3))