class Livro:
    ## Atributos
    def __init__(
                self, 
                titulo:str, autor:str,
                ano_publicacao:int,
                genero:str,
                disponibilidade:bool                 
                 ) -> None:
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._genero = genero
        self._disponibilidade = disponibilidade
        self.oi = 1

    def exibir_informacoes(self) -> None:
        print(
        f"""
        Título: {self._titulo}
        Autor: {self._autor}
        Ano de publicação: {self._ano_publicacao}
        Gênero: {self._genero}
        Disponibilidade: {self._disponibilidade}
        """)
    
    def emprestar_livro(self):
        self._disponibilidade = False

    def devolver_livro(self):
        self._disponibilidade = True

    def verificar_disponibilidade(self) -> str:
        if self._disponibilidade:
            return f"O livro {self._titulo} está disponível"
        return f"O livro {self._titulo} não está disponível"

    def atualizar_ano_publicacao(self, novo_ano: int):
        self._ano_publicacao = novo_ano

    def comparar_com_outro(self, livro) -> bool:
        if isinstance(livro, Livro): # Serve para filtrar os erros de tipo
            if (livro._autor == self._autor) and (livro._genero == self._genero):
                return True
            else: return False

####

# main
livro = Livro("C Programming Language", 
            "Dennis M. Ritchie",
            1988,
            "Científico",
            True            
              )
outroLivro = Livro("Batata",
                   "Dennis M. Ritchie",
                   2099,
                   "Científico",
                   False
                   )

livro.exibir_informacoes()

livro.emprestar_livro()
print(livro.verificar_disponibilidade())

livro.devolver_livro()
print(livro.verificar_disponibilidade())

livro.atualizar_ano_publicacao(2099)
livro.exibir_informacoes()

print(livro.comparar_com_outro(outroLivro))
        