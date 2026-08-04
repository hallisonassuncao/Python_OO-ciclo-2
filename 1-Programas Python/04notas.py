# Leitura das notas
P1 = float(input("Digite a nota da Prova 1: "))
P2 = float(input("Digite a nota da Prova 2: "))
T1 = float(input("Digite a nota do Trabalho 1: "))
T2 = float(input("Digite a nota do Trabalho 2: "))

# Cálculo das médias
MP = (P1 + P2) / 2
MT = (T1 + T2) / 2
MF = 0.8 * MP + 0.2 * MT

# Verificação da situação
if MF >= 6.0:
    print("Aprovado")
else:
    print("Não aprovado")

# Exibição da média final
print(f"Média Final: {MF:.2f}")