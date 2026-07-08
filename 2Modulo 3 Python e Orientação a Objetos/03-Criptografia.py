class Criptografador:
    def __init__(self, frase):
        self.__frase = frase
    
    def criptografar(self):
        substituicoes = {
            'a':'4','A':'4',
            'e':'3','E':'3',
            'i':'1','I':'1',
            'o':'0','O':'0',
            'u':'8','U':
        }

        frase_criptografada = ""

        for caracter in self.__frase:
            if caracter in substituicoes:
                frase_criptografada += substituicoes[caracter]
            else:
                frase_criptografada += caracter
            
        return frase_criptografada


def main():
    frase = input("\nDigite uma frase para criptografar: ")
    criptografador = Criptografador(frase)

    while True:
        print("=" * 35)
        print("       CRIPTOGRAFADOR")
        print("=" * 35)
        print("1 - Criptografar frase")
        print("2 - Digitar uma nova frase")
        print("3 - Mostrar frase criptografada")
        print("0 - Sair")
        print("=" * 35)

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            resultado = criptografador.criptografar()
            print("\nFrase criptografada:")
            print(resultado)
            print()

        elif opcao == "2":
            frase = input("\nDigite uma nova frase: ")
            criptografador = Criptografador(frase)
            print("\nNova frase carregada.\n")

        elif opcao == "3":
            resultado = criptografador.criptografar()
            print("\nResultado atual:")
            print(resultado)
            print()

        elif opcao == "0":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()