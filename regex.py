import re
chiffre = 0
txt = "Tout est pour le mieux dans le meilleur des mondes possibles. Ou pas !"
for lettre in txt:
    x = re.search("o|O", lettre)
    if x:
        chiffre = chiffre + 1
print(chiffre)