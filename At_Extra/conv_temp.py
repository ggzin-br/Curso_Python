# Declarações
io: int
# Algoritmo
io = int(input("$ "))

def conversor(celsius: float):
    # Declarações
    conta: float[2]
    # Algoritmo
    conta = [(9/5*celsius) + 32, celsius + 273.15]
    return conta

valores = conversor(io)
print(f"""
Celsius = {io}
Fahrenheit: {valores[0]}ºF
Kelvin: {valores[1]} K
""")