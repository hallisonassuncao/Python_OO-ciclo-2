def reservar_assento(assentos):
    numero = int(input("Digite o número do assento (1 a 10): "))

    if numero < 1 or numero > 10:
        print("Assento inválido!")
    elif assentos[numero - 1]:
        print("Esse assento já está ocupado.")
    else:
        assentos[numero - 1] = True
        print("Assento reservado com sucesso!")


def liberar_assento(assentos):
    numero = int(input("Digite o número do assento (1 a 10): "))

    if numero < 1 or numero > 10:
        print("Assento inválido!")
    elif not assentos[numero - 1]:
        print("Esse assento já está livre.")
    else:
        assentos[numero - 1] = False
        print("Assento liberado com sucesso!")


def mostrar_mapa(assentos):
    print("\nMapa de Ocupação:")
    for i in range(10):
        if assentos[i]:
            print(f"Assento {i + 1}: Ocupado")
        else:
            print(f"Assento {i + 1}: Livre")
    print()


def main():
    assentos = [False] * 10

    while True:
        print("=== Menu do CINEMA ===")
        print("1. Reservar um assento")
        print("2. Liberar um assento")
        print("3. Mostrar mapa de ocupação")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            reservar_assento(assentos)
        elif opcao == "2":
            liberar_assento(assentos)
        elif opcao == "3":
            mostrar_mapa(assentos)
        elif opcao == "4":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()