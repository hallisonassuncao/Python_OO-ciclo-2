class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("\nNenhum funcionário neste departamento.\n")
        else:
            for f in self.funcionarios:
                print(f"{f.nome} - R$ {f.salario:.2f}")

    def media_salarial(self):
        if not self.funcionarios:
            return 0
        soma = 0
        for f in self.funcionarios:
            soma += f.salario
        return soma / len(self.funcionarios)



def main():
    funcionarios = []
    departamentos = []

    while True:
        print("\n====MENU====")
        print("1- Criar funcionário")
        print("2- Criar departamento")
        print("3- Adicionar funcionário ao departamento")
        print("4- Listar funcionários de um departamento")
        print("5- Mostrar média salarial do departamento")
        print("6- Sair")

        opcao = input("\nEscolha uma opção (1-6): ")

        if opcao == "1":
            nome = input("\nNome do funcionário: ")
            salario = float(input("Salário: "))
            funcionario = Funcionario(nome, salario)
            funcionarios.append(funcionario)
            print("\nFuncionário criado com sucesso!\n")

        elif opcao == "2":
            nome = input("\nNome do departamento: ")
            departamento = Departamento(nome)
            departamentos.append(departamento)
            print("\nDepartamento criado com sucesso!\n")

        elif opcao == "3":
            if funcionarios and departamentos:
                print("\nFuncionários: ")
                for i in range(len(funcionarios)):
                    print(f"{i + 1}. {funcionarios[i].nome}")
                i_func = int(input("\nEscolha o número do funcionário: ")) - 1

                print("\nDepartamentos: ")
                for j in range(len(departamentos)):
                    print(f"{j + 1}. {departamentos[j].nome}")
                j_dep = int(input("\nEscolha o número do departamento: ")) - 1

                departamentos[j_dep].adicionar_funcionario(funcionarios[i_func])

                print("\nFuncionário adicionado ao departamento com sucesso.\n")

            else:
                print("\nCrie funcionários e departamentos primeiro.\n")

        elif opcao == "4":
            if departamentos:
                for j in range(len(departamentos)):
                    print(f"{j + 1}. {departamentos[j].nome}")
                    
                escolha = int(input("\nEscolha o número do departamento: ")) - 1

                departamentos[escolha].listar_funcionarios()
            else:
                print("\nCrie departamentos primeiro.\n")

        elif opcao == "5":
            if departamentos:
                for j in range(len(departamentos)):
                    print(f"{j + 1}. {departamentos[j].nome}")
                    
                escolha = int(input("\nEscolha o número do departamento: ")) - 1

                media = departamentos[escolha].media_salarial()

                print(f"\nMédia salarial: R$ {media:.2f}\n")
            else:
                print("\nCrie departamentos primeiro.\n")

        elif opcao == "6":
            print("\nEncerrando programa...\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")



if __name__ == "__main__":
    main()