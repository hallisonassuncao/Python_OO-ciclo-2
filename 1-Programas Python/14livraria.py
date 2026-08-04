def adicionar_livro(estoque):
    titulo = input("Título do livro: ")
    quantidade = int(input("Quantidade: "))

    if titulo in estoque:
        estoque[titulo] += quantidade
    else:
        estoque[titulo] = quantidade

    print("Livro adicionado ao estoque!")


def remover_unidades(estoque):
    titulo = input("Título do livro: ")

    if titulo not in estoque:
        print("Livro não encontrado no estoque!")
        return

    quantidade = int(input("Quantidade a remover: "))

    if quantidade >= estoque[titulo]:
        estoque[titulo] = 0
        print("Estoque zerado!")
    else:
        estoque[titulo] -= quantidade
        print("Estoque atualizado!")


def consultar_livro(estoque):
    titulo = input("Título do livro: ")

    if titulo in estoque:
        print("Quantidade disponível:", estoque[titulo])
    else:
        print("Livro não está no estoque!")


def mostrar_estoque(estoque):
    print("\n--- ESTOQUE ---")

    for titulo in sorted(estoque):
        print(titulo, "-", estoque[titulo], "unidades")


def menu():
    print("\n--- MENU ---")
    print("1 - Adicionar livro")
    print("2 - Remover unidades de um livro")
    print("3 - Consultar quantidade de um livro")
    print("4 - Mostrar todos os livros")
    print("5 - Sair")


def main():
    estoque = {}

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro(estoque)

        elif opcao == "2":
            remover_unidades(estoque)

        elif opcao == "3":
            consultar_livro(estoque)

        elif opcao == "4":
            mostrar_estoque(estoque)

        elif opcao == "5":
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()