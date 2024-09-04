# Declarações
zeros = 0

io: int
saida = [0]
# Algoritmo
while True:

    io = int(input("$ "))
    try:
        saida[bool(not (io ^ -1) )] # Ele vai testar este caso antes
        1/io # Depois ele vai ver se é zero
    except ZeroDivisionError: # Caso for 0, dará o erro de divisão por 0
        zeros += bool(not io)
    except IndexError: # Caso o bool -> True ele vai quebrar o index
        break # O vetor tem até o 0 e eu acesso o "-1" == "1"
        
print(f"O número 0 foi digitado {zeros} vez(es).")

# Esse programa é livre dos malditos if's