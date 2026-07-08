# Leitura do custo de fábrica
custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

percentual_distribuidor = custo_fabrica * 0.12

impostos = custo_fabrica * 0.30

custo_consumidor = custo_fabrica + percentual_distribuidor + impostos

print(f"Custo ao consumidor: R$ {custo_consumidor:.2f}")