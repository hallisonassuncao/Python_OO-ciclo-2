class AnalisadorString:
    def __init__(self, texto):
        self.__texto = texto
    
    def numero_caracteres(self):
        return len(self.__texto)
    
    def maiusculas(self):
        return self.__texto.upper()
    
    def minusculas(self):
        return self.__texto.lower()
    
    def contar_vogais(self):
        vogais = 'aeiouAEIOU'
        contador = 0

        for caracter in self.__texto:
            if caracter in vogais:
                contador += 11
        
        return contador
    
    def contem_ifb(self):
        return "IFB" in self.__texto.upper()


def main():
    texto = input("\nDigite um texto: ")
    analisador = AnalisadorString(texto)

    while True:
        print("=" * 35)
        print("       ANALISADOR DE TEXTO")
        print("=" * 35)
        print("1 - Mostrar número de caracteres")
        print("2 - Mostrar texto em maiúsculas")
        print("3 - Mostrar texto em minúsculas")
        print("4 - Contar vogais")
        print("5 - Verificar se contém IFB")
        print("6 - Mostrar análise completa")
        print("0 - Sair")
        print("=" * 35)

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print(f"\nNúmero de caracteres: {analisador.numero_caracteres()}\n")

        elif opcao == "2":
            print(f"\nTexto em maiúsculas: {analisador.maiusculas()}\n")

        elif opcao == "3":
            print(f"\nTexto em minúsculas: {analisador.minusculas()}\n")

        elif opcao == "4":
            print(f"\nNúmero de vogais: {analisador.contar_vogais()}\n")

        elif opcao == "5":
            if analisador.contem_ifb():
                print("\nA substring 'IFB' aparece no texto.\n")
            else:
                print("\nA substring 'IFB' NÃO aparece no texto.\n")

        elif opcao == "6":
            print("\n=== Análise Completa do Texto ===")
            print(f"Número de caracteres: {analisador.numero_caracteres()}")
            print(f"Em maiúsculas: {analisador.maiusculas()}")
            print(f"Em minúsculas: {analisador.minusculas()}")
            print(f"Número de vogais: {analisador.contar_vogais()}")

            if analisador.contem_ifb():
                print("A substring 'IFB' aparece no texto.")
            else:
                print("A substring 'IFB' NÃO aparece no texto.")

            print()

        elif opcao == "0":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida. Escolha novamente.\n")


if __name__ == "__main__":
    main()