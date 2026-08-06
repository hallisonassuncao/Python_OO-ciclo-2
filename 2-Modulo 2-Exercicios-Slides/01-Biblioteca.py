
class Livro:
    def __init__(self, titulo, autor, id_livro):
        self.__titulo = titulo
        self.__autor = autor
        self.__id_livro = id_livro

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_id_livro(self):
        return self.__id_livro

    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    def set_autor(self, novo_autor):
        self.__autor = novo_autor

    def set_id_livro(self, novo_id):
        self.__id_livro = novo_id


class Usuario:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__livros_emprestados = []

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    # Getter adicionado apenas para o menu funcionar
    def get_livros_emprestados(self):
        return self.__livros_emprestados

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula

    def emprestar_livro(self, livro):
        self.__livros_emprestados.append(livro)
        print(f"\n{self.__nome} pegou emprestado o livro '{livro.get_titulo()}'.\n")

    def devolver_livro(self, id_livro):
        for livro in self.__livros_emprestados:
            if livro.get_id_livro() == id_livro:
                self.__livros_emprestados.remove(livro)
                print(f"\n{self.__nome} devolveu o livro '{livro.get_titulo()}'.\n")
                return livro

        print(f"\n{self.__nome} não possui um livro com ID {id_livro}.\n")
        return None

    def listar_livros_emprestados(self):
        if not self.__livros_emprestados:
            print("\nNenhum livro emprestado.\n")
        else:
            print("\nLivros emprestados:")
            for livro in self.__livros_emprestados:
                print(f"- {livro.get_titulo()} ({livro.get_id_livro()})")
            print()


def main():
    livros_disponiveis = [
        Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1),
        Livro("Capitães da Areia", "Jorge Amado", 2)
    ]

    usuario1 = Usuario("Clara", "2026001")

    while True:
        print("=" * 40)
        print("         MENU DA BIBLIOTECA")
        print("=" * 40)
        print("1 - Listar livros disponíveis")
        print("2 - Emprestar livro")
        print("3 - Devolver livro")
        print("4 - Listar livros emprestados")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nLivros disponíveis:")
            if len(livros_disponiveis) == 0:
                print("Nenhum livro disponível.")
            else:
                for livro in livros_disponiveis:
                    print(f"ID: {livro.get_id_livro()} - {livro.get_titulo()} - {livro.get_autor()}")

        elif opcao == "2":
            if len(livros_disponiveis) == 0:
                print("\nNão há livros disponíveis.")
            else:
                try:
                    id_livro = int(input("Digite o ID do livro: "))
                    encontrado = False

                    for livro in livros_disponiveis:
                        if livro.get_id_livro() == id_livro:
                            usuario1.emprestar_livro(livro)
                            livros_disponiveis.remove(livro)
                            encontrado = True
                            break

                    if not encontrado:
                        print("\nLivro não encontrado.")

                except ValueError:
                    print("\nDigite um número válido.")

        elif opcao == "3":
            try:
                id_livro = int(input("Digite o ID do livro a devolver: "))
                livro = usuario1.devolver_livro(id_livro)

                if livro is not None:
                    livros_disponiveis.append(livro)

            except ValueError:
                print("\nDigite um número válido.")

        elif opcao == "4":
            usuario1.listar_livros_emprestados()

        elif opcao == "0":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    main()