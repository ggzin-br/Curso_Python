# Limpo dos malditos if's

# Declarações
io = int(input("$ "))

# Algoritmo
def primo(num: int) -> bool:
    isPrimo: bool = True

    # Casos acima de 2
    for i in range(num-1, 1, -1):
        isPrimo = isPrimo and bool(num % i)
        # Se caso for divisível, vai zerar tudo
    else:
        isPrimo = isPrimo and bool(num ^ 1)
    
    return isPrimo

# Parte par
print("Esse número é primo!" * bool(primo(io)))

# Parte ímpar
print("Esse número não é primo!" * bool(not primo(io)))