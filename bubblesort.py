## Declarações
listaInt: list = [64, 34, 25, 12, 22, 11, 90]

## Algoritmo
for iteracoes in range(len(listaInt) - 1, 0, -1): # A cada passada o algoritmo levanta 1 número
    for index in range(iteracoes):
        if listaInt[index] > listaInt[index+1]:
            listaInt[index], listaInt[index+1] = listaInt[index+1], listaInt[index]

print(listaInt)
# Explicação:
"""
1º Um número grande é elevado (necessariamente) -> [34, ... 64, 90]

2º O maior número não precisa ser comparado novamente -> [25, ... 34, 64]
O 90 não foi comparado

3... Assim vai 
"""

