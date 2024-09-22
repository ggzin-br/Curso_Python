def seqI(num: int, isCrescente: bool):
    return num + (3 if isCrescente else -3)

def seqJ(num: int, isCrescente: bool):
    return num + (5 if isCrescente else -5)                                                                                                                                                                                                                            

def main():
    ## Declarações
    i: int
    j: int
    iteracoes: int
    isCrescenteI: int
    isCrescenteJ: int

    ## Algoritmo
    try:
        i = int(input("Digite um valor para a sequência I $ "))
        j = int(input("Digite um valor para a sequência J $ "))
        iteracoes = int(input("Número de iterações da sequencia $ "))
    except ValueError:
        print("Erro na obtenção dos valores!")
        exit(1)
    isCrescenteJ = 1 if input("A sequência J é crescente? (S/N)$ ").lower() == "s" else 0
    isCrescenteI = 1 if input("A sequência I é crescente? (S/N)$ ").lower() == "s" else 0

    for _ in range(iteracoes):
        print(f"I={i} J={j}")
        i = seqI(i, isCrescenteI)
        j = seqJ(j, isCrescenteJ)

    

if __name__ == "__main__":
    main()