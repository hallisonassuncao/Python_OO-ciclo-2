
palestra_ia = set()
workshop_python = set()


def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")

    evento = input("Participou de qual evento? (IA/Python): ").lower()

    if evento == "ia":
        palestra_ia.add(nome)
        print("Aluno adicionado à palestra de IA!")
    elif evento == "python":
        workshop_python.add(nome)
        print("Aluno adicionado ao workshop de Python!")
    else:
        print("Evento inválido!")


def mostrar_ambos():
    ambos = palestra_ia.intersection(workshop_python)

    if ambos:
        print("Alunos que participaram dos dois eventos:")
        for aluno in ambos:
            print(aluno)
    else:
        print("Nenhum aluno participou dos dois eventos.")


def mostrar_somente_ia():
    somente_ia = palestra_ia.difference(workshop_python)

    if somente_ia:
        print("Alunos que participaram somente da palestra de IA:")
        for aluno in somente_ia:
            print(aluno)
    else:
        print("Nenhum aluno encontrado.")


def mostrar_pelo_menos_um():
    participantes = palestra_ia.union(workshop_python)

    if participantes:
        print("Alunos que participaram de pelo menos um evento:")
        for aluno in participantes:
            print(aluno)
    else:
        print("Nenhum aluno cadastrado.")


def verificar_aluno():
    nome = input("Digite o nome do aluno: ")

    if nome in palestra_ia and nome in workshop_python:
        print("Participou de ambos os eventos.")
    elif nome in palestra_ia:
        print("Participou somente da palestra de IA.")
    elif nome in workshop_python:
        print("Participou somente do workshop de Python.")
    else:
        print("Não participou de nenhum evento.")


def main():
    while True:
        print("\n===== MENU =====")
        print("1. Adicionar aluno a um evento")
        print("2. Mostrar alunos que participaram de ambos os eventos")
        print("3. Mostrar alunos que participaram somente da palestra de IA")
        print("4. Mostrar alunos que participaram de pelo menos um evento")
        print("5. Verificar participação de um aluno")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            mostrar_ambos()
        elif opcao == "3":
            mostrar_somente_ia()
        elif opcao == "4":
            mostrar_pelo_menos_um()
        elif opcao == "5":
            verificar_aluno()
        elif opcao == "6":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()