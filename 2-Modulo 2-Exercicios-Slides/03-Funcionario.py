# Classe base
class Funcionario:
    def __init__(self, nome, salarioBase):
        self.nome = nome
        self.salarioBase = salarioBase

    def calcularSalario(self):
        return self.salarioBase

    def exibirDados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.calcularSalario():.2f}")


# Subclasse
class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, salarioBase, comissao):
        super().__init__(nome, salarioBase)
        self.comissao = comissao

    # Sobrescrita do método
    def calcularSalario(self):
        return self.salarioBase + self.comissao

    # Sobrescrita do método
    def exibirDados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário Base: R$ {self.salarioBase:.2f}")
        print(f"Comissão: R$ {self.comissao:.2f}")
        print(f"Salário Total: R$ {self.calcularSalario():.2f}")


# Instanciando objetos
funcionario1 = Funcionario("Leticia", 5000.00)
funcionario2 = FuncionarioComissionado("Camila", 8000.00, 800.00)


# Exibindo os dados
print("=== Funcionário ===")
funcionario1.exibirDados()

print("\n=== Funcionário Comissionado ===")
funcionario2.exibirDados()