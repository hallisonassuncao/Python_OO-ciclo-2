class Participante:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email

    def emitirCertificado(self):
        return f"Certificado de participação concedido a {self._nome}."


class Aluno(Participante):
    def __init__(self, nome, email, curso):
        super().__init__(nome, email)
        self.__curso = curso

    def get_curso(self):
        return self.__curso

    def emitirCertificado(self):
        return f"Certificamos que {self.get_nome()} concluiu o curso de {self.__curso} com êxito."


class Instrutor(Participante):
    def __init__(self, nome, email, especialidade):
        super().__init__(nome, email)
        self.__especialidade = especialidade

    def get_especialidade(self):
        return self.__especialidade

    def emitirCertificado(self):
        return f"Certificamos que {self.get_nome()} participou como instrutor na área de {self.__especialidade}."


def main():
    participantes = []

    while True:
        print("\n======Sistema de Participantes😎======")
        print("1 - Novo cadastro")
        print("2 - Exibir participantes")
        print("3 - Gerar certificados")
        print("4 - Encerrar")

        opcao = input("\nInforme a opção desejada: ")

        if opcao == "1":
            print("\nEscolha o tipo de participante:")
            print("1 - Aluno")
            print("2 - Instrutor")

            tipo = input("Opção: ")

            if tipo == "1":
                nome = input("Nome: ")
                email = input("E-mail: ")
                curso = input("Curso: ")

                participantes.append(Aluno(nome, email, curso))
                print("\nCadastro de aluno realizado com sucesso!")

            elif tipo == "2":
                nome = input("Nome: ")
                email = input("E-mail: ")
                especialidade = input("Especialidade: ")

                participantes.append(Instrutor(nome, email, especialidade))
                print("\nCadastro de instrutor realizado com sucesso!")

            else:
                print("\nTipo de participante inválido!")

        elif opcao == "2":
            if not participantes:
                print("\nNão há participantes cadastrados.")
            else:
                print("\n====== Lista de Participantes ======")

                for p in participantes:
                    if isinstance(p, Aluno):
                        print("Categoria: Aluno")
                        print(f"Nome: {p.get_nome()}")
                        print(f"E-mail: {p.get_email()}")
                        print(f"Curso: {p.get_curso()}")
                        print("-" * 35)
                    else:
                        print("Categoria: Instrutor")
                        print(f"Nome: {p.get_nome()}")
                        print(f"E-mail: {p.get_email()}")
                        print(f"Especialidade: {p.get_especialidade()}")
                        print("-" * 35)

        elif opcao == "3":
            if not participantes:
                print("\nNão existem participantes cadastrados.")
            else:
                print("\n====== Certificados Emitidos ======")

                for p in participantes:
                    print(p.emitirCertificado())

        elif opcao == "4":
            print("\nSistema encerrado. Obrigado por utilizar o programa!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()