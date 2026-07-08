saldo = 1000.00

while True:
    print("\n===== BANCO =====")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Consultar Saldo")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor para depósito: "))
        if valor > 0:
            saldo += valor
            print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
        else:
            print("Valor inválido.")

    elif opcao == "2":
        valor = float(input("Digite o valor para saque: "))
        if valor <= 0:
            print("Valor inválido.")
        elif valor <= saldo:
            saldo -= valor
            print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
        else:
            print("Saldo insuficiente.")

    elif opcao == "3":
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")