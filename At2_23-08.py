## Declarações #
operacoes: dict = {
    "Rafael": lambda x, y: pow((3*x), 2) + pow(y, 2),
    "Beto": lambda x, y: 2 * pow(x, 2) + pow((5 * y), 2),
    "Carlos": lambda x, y: -100*x + pow(y, 3)
} 
resultados: list = []
nome: str

valores:list = []
io: str = ""

## Algoritmo #
io = input("$ ").split(" ")
valores = [ int(io[i]) for i in range(2) ] # Conversão de valores

nome = "Rafael"
maior = operacoes[nome](valores[0], valores[1])
for lamb in operacoes.keys(): # Algoritmo para obter o maior resultado
    if operacoes[lamb](valores[0], valores[1]) > maior:
        maior = operacoes[lamb](valores[0], valores[1])
        nome = lamb

print(nome+" ganhou")

