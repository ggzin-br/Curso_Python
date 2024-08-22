## Declarações #
segundo = 0
minuto = 0
hora = 0

## Algoritmo #
segundo = int(input("Informe os segundos $ "))

if segundo > 60:
    minuto = int(segundo/60)
    segundo -= 60*int(segundo/60)
if minuto > 60:
    hora = int(minuto/60)
    minuto -= 60*int(minuto/60)

print(f"{hora}:{minuto}:{segundo}")