def adicionar_time(times):
    nome = input("Nome do time: ")

    if nome in times:
        print("Time já cadastrado!")
    else:
        times[nome] = 0
        print("Time adicionado!")


def registrar_partida(times):
    time1 = input("Primeiro time: ")
    time2 = input("Segundo time: ")

    if time1 not in times or time2 not in times:
        print("Time não encontrado!")
        return

    gols1 = int(input("Gols do primeiro time: "))
    gols2 = int(input("Gols do segundo time: "))

    if gols1 > gols2:
        times[time1] += 3
    elif gols2 > gols1:
        times[time2] += 3
    else:
        times[time1] += 1
        times[time2] += 1

    print("Resultado registrado!")


def chave_pontos(item):
    return item[1]


def mostrar_classificacao(times):
    print("\nClassificação:")

    for time, pontos in sorted(times.items(), key=chave_pontos, reverse=True):
        print(time, "-", pontos, "pontos")


def remover_time(times):
    nome = input("Nome do time: ")

    if nome in times:
        del times[nome]
        print("Time removido!")
    else:
        print("Time não encontrado!")


def menu():
    print("\n--- MENU ---")
    print("1 - Adicionar Time")
    print("2 - Registrar Resultado de Partida")
    print("3 - Mostrar Classificação")
    print("4 - Remover Time")
    print("5 - Sair")


def main():
    times = {}

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_time(times)

        elif opcao == "2":
            registrar_partida(times)

        elif opcao == "3":
            mostrar_classificacao(times)

        elif opcao == "4":
            remover_time(times)

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()