# Declarações
isdiv3 = 0
isdiv5 = 0
isdiv7 = 0
mod: int

io: int
saida = [0]
# Algoritmo
while True:

    io = int(input("$ "))
    try:
        saida[bool(not (io ^ -1) )]
    except IndexError: # Caso o bool -> True ele vai quebrar o index
        break # O vetor tem até o 0 e eu acesso o "-1" == "1"

    # NÃO [ |0| OU [|0| + 0] ] -> bool (True)

    mod = io % 3
    isdiv3 += bool( not ( abs(mod) or (mod + abs(mod)) ) )

    mod = io % 5
    isdiv5 += bool( not ( abs(mod) or (mod + abs(mod)) ) )

    mod = io % 7
    isdiv7 += bool( not ( abs(mod) or (mod + abs(mod)) ) )

## Interface
print(f"""
\t{isdiv3} valor(es) divisível(is) por 3
\t{isdiv5} valor(es) divisível(is) por 5
\t{isdiv7} valor(es) divisível(is) por 7
""")

# Esse programa é livre dos malditos if's