from abc import ABC, abstractmethod

class VeiculoTransporte(ABC):
    def __init__(self, placa, capacidadep):
        self.placa = placa
        self.capacidadep = capacidadep

    @abstractmethod
    def calcularCusto(self):
        pass

class Onibus(VeiculoTransporte):
    def __init__(self, placa, capacidadep, consumokm):
        super().__init__(placa, capacidadep)
        self.consumokm = consumokm

    def calcularCusto(self):
        return self.consumokm * 6.0

class Metro(VeiculoTransporte):
    def __init__(self, placa, capacidadep, consumoenergiakm):
        super().__init__(placa, capacidadep)
        self.consumoenergiakm = consumoenergiakm

    def calcularCusto(self):
        return self.consumoenergiakm * 0.80

def main():
    veiculos = []

    while True:
        print("\n===MENU===")
        print("1. Cadastrar Ônibus")
        print("2. Cadastrar Metrô")
        print("3. Mostrar custos operacionais")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nCadastro de Ônibus")

            try:
                placa = input("Placa: ").strip()

                if placa == "":
                    raise ValueError("A placa não pode estar vazia.")

                capacidade = int(input("\nCapacidade de passageiros: "))

                if capacidade <= 0: 
                    raise ValueError("A capacidade deve ser positiva.")

                consumo = float(input("\nConsumo por km (litros/km): "))
                
                if consumo <= 0: 
                    raise ValueError("O consumo deve ser positivo.")

                veiculos.append(Onibus(placa, capacidade, consumo))

                print("\nÔnibus cadastrado com sucesso!\n")

            except ValueError as e:
                print(f"\nErro: {e}")

        elif opcao == "2":
            print("\nCadastro de Metrô")
            
            try:
                placa = input("Identificação: ").strip()

                if placa == "":
                    raise ValueError("A identificação não pode estar vazia.")

                capacidade = int(input("\nCapacidade de passageiros: "))

                if capacidade <= 0: 
                    raise ValueError("A capacidade deve ser positiva.")

                consumo = float(input("\nConsumo por km (KWh/km): "))
                
                if consumo <= 0: 
                    raise ValueError("O consumo deve ser positivo.")

                veiculos.append(Metro(placa, capacidade, consumo))

                print("\nMetrô cadastrado com sucesso!\n")

            except ValueError as e:
                print(f"\nErro: {e}")

        elif opcao == "3":
            if not veiculos:
                print("\nNenhum veículo cadastrado!\n")
            else:
                print("\n---Custos Operacionais por km---")
                for v in veiculos:
                    tipo = "Ônibus" if isinstance(v, Onibus) else "Metrô"
                    custo = v.calcularCusto()
                    print(f"{tipo} {v.placa}: R$ {custo:.2f} por km")
                print()

        elif opcao == "0":
            print("\nEncerrando o sistema...\n")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()