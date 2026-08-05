def adicionar_nota(lista):
    nome = input("Nome do aluno: ")
    nota = float(input("Nota: "))
    disciplina = input("Disciplina: ")

    lista.append([nome, nota, disciplina])


def melhor_aluno_por_disciplina(lista):
    disciplinas = []


    for item in lista:
        disciplina = item[2]
        if disciplina not in disciplinas:
            disciplinas.append(disciplina)

    for disciplina in disciplinas:
        melhor_nome = ""
        melhor_nota = -1

        for item in lista:
            nome = item[0]
            nota = item[1]
            disc = item[2]

            if disc == disciplina and nota > melhor_nota:
                melhor_nota = nota
                melhor_nome = nome

        print(disciplina, "-", melhor_nome, "(", melhor_nota, ")")


def consultar_notas_por_aluno(lista):
    nome = input("Nome do aluno: ")
    encontrou = False

    for item in lista:
        if item[0] == nome:
            print(item[2], ":", item[1])
            encontrou = True

    if not encontrou:
        print("Aluno não encontrado")


def exibir_notas(lista):
    print("\nNotas cadastradas:")

    for item in lista:
        print("Aluno:", item[0], "- Nota:", item[1], "- Disciplina:", item[2])


def menu():
    print("\n--- MENU ---")
    print("1 - Adicionar nota")
    print("2 - Melhor aluno por disciplina")
    print("3 - Consultar notas por aluno")
    print("4 - Exibir todas as notas")
    print("5 - Sair")


def main():
    lista = []

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_nota(lista)

        elif opcao == "2":
            melhor_aluno_por_disciplina(lista)

        elif opcao == "3":
            consultar_notas_por_aluno(lista)

        elif opcao == "4":
            exibir_notas(lista)

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


main()

if __name__ == "__main__":
    main()
