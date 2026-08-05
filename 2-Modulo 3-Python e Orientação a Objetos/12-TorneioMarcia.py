from abc import ABC, abstractmethod

class Lutador(ABC):

    @abstractmethod
    def obter_nome(self):
        pass 

    @abstractmethod
    def obter_poder(self):
        pass 

    @abstractmethod
    def atacar(self):
        pass 

class Saiyajin(Lutador):
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

    def obter_nome(self):
        return self.nome

    def obter_poder(self):
        return self.poder
    
    def atacar(self):
        print(f"\n{self.nome} transformação em Super Saiyajin!\n")


class Android(Lutador):
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

    def obter_nome(self):
        return self.nome

    def obter_poder(self):
        return self.poder
    
    def atacar(self):
        print(f"\n{self.nome} Golpe Maximo\n")


class Namekuseijin(Lutador):
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

    def obter_nome(self):
        return self.nome

    def obter_poder(self):
        return self.poder
    
    def atacar(self):
        print(f"\n{self.nome} Golpe Tesoura !\n")



def main():
    lutadores = []

    while True:
        print("\n===TORNEIO MACIAIS===")
        print("1. Cadastrar lutador")
        print("2. Listar lutadores")
        print("3. Simular ataque")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nTipos de lutador: ")
            print("1. Saiyajin")
            print("2. Android")
            print("3. Namekuseijin")

            tipo = input("\nEscolha o tipo: ")

            try:
                nome = input("\nNome do lutador: ").strip()

                if not nome:
                    raise Exception("O nome não pode estar vazio.")
                
                poder_input = input("\nNível do poder: ").strip()

                if not poder_input:
                    raise Exception("O nível de poder não pode estar vazio.")

                poder = int(poder_input)

                if poder <= 0:
                    raise Exception("O nível de poder deve ser um número positivo.")
                
                if tipo == "1":
                    lutador = Saiyajin(nome, poder)
                elif tipo == "2":
                    lutador = Android(nome, poder)
                elif tipo == "3":
                    lutador = Namekuseijin(nome, poder)
                else:
                    print("\nTipo inválido!\n")
                    continue
                
                lutadores.append(lutador)

                print(f"\n{lutador.obter_nome()} Scadastrado com sucesso!\n")

            except Exception as e:
                print(f"\nErro: {e}")
            
        elif opcao == "2":
            if not lutadores:
                print("\nNenhum lutador cadastrado.\n")
            else:
                print("\n---Lutadores Inscritos---")

                for i, l in enumerate(lutadores, start=1):
                    print(f"{i}. {l.obter_nome()} - Poder: {l.obter_poder()}")
        
        elif opcao == "3":
            if not lutadores:
                print("\nNenhum lutador para atacar.\n")
            else:
                print("\nLutadores do Torneio: ")
                for i, l in enumerate(lutadores, start=1):
                    print(f"{i}. {l.obter_nome()}")
                
            try:
                escolha = int(input("\nEscolha o número do lutador: "))

                if 1 <= escolha <= len(lutadores):
                    print(f"\n{lutadores[escolha - 1].obter_nome()} vai atacar!")
                    lutadores[escolha - 1].atacar()
                else:
                    raise Exception("Número inválido para escolha de lutador.")
            except Exception as e:
                print(f"\nErro: {e}")

        elif opcao == "4":
            print("\nEncerrando o sistema.\n")
            break

        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()