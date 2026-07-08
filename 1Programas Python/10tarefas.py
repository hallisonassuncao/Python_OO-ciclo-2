def adicionar_tarefa(tarefas):
    descricao = input("\nDescrição da tarefa: ")

    prioridade = input("Prioridade (1 a 5): ")

    while not prioridade.isdigit() or int(prioridade) < 1 or int(prioridade) > 5:
        print("\nPor favor, digite um número inteiro de 1 a 5.")
        prioridade = input("Prioridade (1 a 5): ")

    tarefa = {
        "descricao": descricao,
        "prioridade": int(prioridade),
        "concluida": False
    }

    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")


def listar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\nLista de tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status_simbolo = "✓" if tarefa["concluida"] else "✗"
        status_texto = "Concluída" if tarefa["concluida"] else "Pendente"

        print(
            f"{i}. [{status_simbolo}] "
            f"{tarefa['descricao']} "
            f"(Prioridade: {tarefa['prioridade']}) "
            f"Status: {status_texto}"
        )


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    if tarefas:
        try:
            numero = int(input("\nDigite o número da tarefa concluída: "))

            if 1 <= numero <= len(tarefas):
                tarefas[numero - 1]["concluida"] = True
                print("Tarefa marcada como concluída!")
            else:
                print("Número de tarefa inválido.")

        except ValueError:
            print("Digite um número válido.")


def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    if tarefas:
        try:
            numero = int(input("\nDigite o número da tarefa que deseja excluir: "))

            if 1 <= numero <= len(tarefas):
                tarefa_removida = tarefas.pop(numero - 1)
                print(f"Tarefa '{tarefa_removida['descricao']}' excluída com sucesso!")
            else:
                print("Número de tarefa inválido.")

        except ValueError:
            print("Digite um número válido.")


def main():
    tarefas = []

    while True:
        print("\n" + "=" * 30)
        print("      GERENCIADOR DE TAREFAS")
        print("=" * 30)
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Marcar tarefa como concluída")
        print("4 - Excluir tarefa")
        print("5 - Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa(tarefas)

        elif escolha == "2":
            listar_tarefas(tarefas)

        elif escolha == "3":
            concluir_tarefa(tarefas)

        elif escolha == "4":
            excluir_tarefa(tarefas)

        elif escolha == "5":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()