def divisores(num: int):
    # Declarações
    divs = []
    # Algoritmo
    for i in range(1, num+1, 1):
        if num % i == 0: divs.append(i)
    return divs

print(f"L={divisores(int(input('$ ')))}")