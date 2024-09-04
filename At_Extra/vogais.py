# Declarações
vogais:tuple = ("a", "e", "i", "o", "u")
io: str
# Algoritmos
io = input("$ ")

for c in io:
    if vogais.__contains__(c.lower()):
        print(c.lower(), end=" ")
print("")