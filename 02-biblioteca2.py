class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade


class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
    
    def criar_livro(self, titulo, ano, autor):
        livro = Livro(titulo, ano, autor)
        self.livros.append(livro)
        return livro
    
    def listar_livros(self):
        print(f"\nLivros disponíveis na biblioteca '{self.nome}': ")
        for livro in self.livros:
            print(f"- Título: {livro.titulo}, Ano: {livro.ano}, Autor: {livro.autor.nome} ({livro.autor.nacionalidade})")
        print()

class Usuario:
    def __init__(self, nome, biblioteca):
        self.nome = nome
        self.biblioteca = biblioteca

    def pegar_emprestado(self, livro):
        if livro in self.biblioteca.livros:
            print(f"\n{self.nome} pegou emprestado o livro {livro.titulo}.\n")
        else:
            print(f"\nLivro '{livro.titulo}' não está disponível na biblioteca {self.biblioteca.nome}\n")


def main():
    autor1 = Autor("Machado de Assis", "Brasileiro")
    autor2 = Autor("J. K. Rowling", "Britânica")

    biblioteca = Biblioteca("Biblioteca do IFB")

    livro1 = biblioteca.criar_livro("Dom Casmurro", 1899, autor1)
    livro2 = biblioteca.criar_livro("Harry Potter e a Pedra Filosofal", 1997, autor2)

    biblioteca.listar_livros()

    usuario = Usuario("Carlos", biblioteca)

    usuario.pegar_emprestado(livro1)
    usuario.pegar_emprestado(livro2)
    usuario.pegar_emprestado(Livro("A Trança do Rei Careca", 2020, autor1))


if __name__ == "__main__":
    main()