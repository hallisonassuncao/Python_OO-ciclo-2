# Taxas de câmbio de exemplo
DOLAR = 5.20
EURO = 5.70
LIBRA = 6.60
IENE = 0.035

valor_reais = float(input("Digite o valor em reais (R$): "))

print("\nEscolha a moeda de destino:")
print("1. Dólar")
print("2. Euro")
print("3. Libra")
print("4. Iene")

opcao = int(input("Opção: "))

if opcao == 1:
    convertido = valor_reais / DOLAR
    print(f"R$ {valor_reais:.2f} = US$ {convertido:.2f}")

elif opcao == 2:
    convertido = valor_reais / EURO
    print(f"R$ {valor_reais:.2f} = € {convertido:.2f}")

elif opcao == 3:
    convertido = valor_reais / LIBRA
    print(f"R$ {valor_reais:.2f} = £ {convertido:.2f}")

elif opcao == 4:
    convertido = valor_reais / IENE
    print(f"R$ {valor_reais:.2f} = ¥ {convertido:.2f}")

else:
    print("Opção inválida!")