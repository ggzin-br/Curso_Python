## Bibliotecas
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def info(self): ...

class Carro(Veiculo):
    ## Atributos
    def __init__(self, marca:str, ano:str, modelo:str, preco:str) -> None:
        self._marca = marca
        self._ano = ano
        self._modelo = modelo
        self.__preco = preco
    
    ## Métodos
    def info(self):
        print(
        f"""
        Marca: {self._marca}
        Ano: {self._ano}
        Modelo: {self._modelo}
        Preço: {self.__preco}
        """)

    @property
    def getPreco(self):
        return self.__preco
    
    # Por algum motivo não consegui configurar o .setter
    def setPreco(self, preco:str):
        self.__preco = preco

class Bicicleta(Veiculo):
    ## Atributos
    def __init__(self, marca:str, tipo: str) -> None:
        self._marca = marca
        self._tipo = tipo
    
    ## Métodos
    def info(self):
        print(
        f"""
        Marca: {self._marca}
        Tipo: {self._tipo}
        """)

class Garagem:
    ## Atributos
    _veiculosGaragem: list = []
    def __init__(self, *args) -> None:
        for veiculo in args:
            if isinstance(veiculo, Veiculo):
                self._veiculosGaragem.append(veiculo)
    
    ## Métodos
    def veiculos(self) -> str:
        veics: str = "\n"
        for veiculos in self._veiculosGaragem:
            for chave, valor in vars(veiculos).items():
                veics += f"{chave}: {valor}\n"
            veics += "\n"
        return veics

    def setVeiculos(self, *args):
        for veiculos in args:
            if isinstance(veiculos, Veiculo):
                self._veiculosGaragem.append(veiculos)


def principal():
    ## Declarações
    bicicletaDoAuto = Bicicleta("Caloi", "Montain Bike")
    mecaDoPaldes = Carro("BMW", 2023, "320i", "R$1.000.000,00")
    bicicletaDoTiago = Bicicleta("Monark", "Cidade")
    garagemDoRavier = Garagem(bicicletaDoAuto, mecaDoPaldes)

    ## Algoritmo
    bicicletaDoAuto.info()
    mecaDoPaldes.info()

    mecaDoPaldes.setPreco("R$1.200.000,00")
    print(mecaDoPaldes.getPreco)

    print(garagemDoRavier.veiculos())
    garagemDoRavier.setVeiculos(bicicletaDoTiago)
    print(garagemDoRavier.veiculos())
    

if __name__ == "__main__": principal()