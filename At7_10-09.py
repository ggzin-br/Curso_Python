import os
## Constantes
limpeza = "clear" if os.name == "posix" else "cls"

class Livro:    
    ## Declarações 
    def __init__(self, titulo: str, autor: str, dataPublicacao: str) -> None:
        self._titulo = titulo
        self._autor = autor
        self._dataPublicação = dataPublicacao
    ## Algoritmo
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def dataPublicacao(self):
        return self._dataPublicação
    

## Declarações
listaLivros: list = []

menu: str = f"""
\tCatálogo de Livros
1. Adicionar livro
2. Remover livro
3. Buscar livro
4. Ordenar livros
5. Exibir catálogo completo
6. Sair
"""

io: int
## Algoritmo
def ordObjs() -> None: ## Bubble sort de letras
    ## 
    for iteracoes in range(len(listaLivros) - 1, 0, -1):
        for index in range(iteracoes):
            if ord(listaLivros[index].titulo[0].upper()) > ord(listaLivros[index + 1].titulo[0].upper()):
                listaLivros[index], listaLivros[index + 1] = listaLivros[index + 1], listaLivros[index]

def exCatalogo(livros: list) -> None:
    for livro in listaLivros:
        print(f"""
        Título: {livro.titulo}
        Autor: {livro.autor}
        Data de publicação: {livro.dataPublicacao}
        """)

def remLivro(titulo: str) -> None:
    for livro in listaLivros:
        if livro.titulo == titulo:
            listaLivros.remove(livro)

def buscLivro(termo: str) -> None:
    for livro in listaLivros:
        for _, atr in vars(livro).items():
            if atr == termo:
                print(f"""
                Título: {livro.titulo}
                Autor: {livro.autor}
                Data de publicação: {livro.dataPublicacao}
                """)


def main():
    while True:
        print(menu)
        try: io = int(input("Escolha uma opção $ "))
        except ValueError: continue

        os.system(limpeza)
        match io: # Por algum motivo este "case" não precisa de break
            case 1:
                listaLivros.append(
                    Livro(input("$ Digite o título do livro $ "),
                          input("Digite o autor do livro $ "),
                          input("Digite a data de publicação do livro (DD/MM/AAAA)$ ")
                          )
                )
            case 2: remLivro(input("$ Digite o título do livro $ "))
            case 3: buscLivro(input("$ Digite um atributo do livro $ "))
            case 4: ordObjs()
            case 5: exCatalogo(listaLivros)
            case _: break

        input("\nAperte enter para continuar ...")
        os.system(limpeza)


if __name__ == "__main__":
    main()
