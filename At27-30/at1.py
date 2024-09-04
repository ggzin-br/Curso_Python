# Valores negativos são True
# Declarações
positivos = 0
negativos = 0
zeros = 0
io: float

saida = [0]
# Algoritmo
while True:

    io = float(input("$ "))
    try: # Gambiarra total: sistema de saída do programa
        # Dar false caso não for -1
        # Dar true caso for -1
        # NOT[ -1 XOR -1 ] -> bool (True)
        saida[bool( not (int(io) ^ -1) )]
    except IndexError:
        break
        # Não apague esse try/catch e o vetor de saida
    
    # Número positivo/negativo
    # 65 + |65| -> bool (True)
    # -20 E [ NÃO [-20 + |20|] ] -> bool (True)
    positivos += bool( io + abs(io) )
    negativos += bool( io and ( not (io + abs(io)) ) )

    # Número zero
    # NÃO [ |0| OU [|0| + 0] ] -> bool (True)
    zeros += bool( not ( abs(io) or (io + abs(io)) ) )


## Interface
print(f"""
\t{positivos} valor(es) positivo(s)
\t{negativos} valor(es) negativo(s)
\t{zeros} valor(es) zero(s)
""")
    
# Esse programa é livre dos malditos if's 