# Gabriel Henryck de Souza Costa e Gustavo da Silveira Francisco
#Class 1 

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome  # Encapsulamento
        self.__idade = idade  # Encapsulamento 
    # Getter para o 'nome'
    def get_nome(self):
        return self.__nome

    # Setter para o 'nome'
    def set_nome(self, nome):
        self.__nome = nome

    # Getter para a 'idade'
    def get_idade(self):
        return self.__idade

    # Setter para a 'idade'
    def set_idade(self, idade):
        self.__idade = idade

    # Apresentar a pessoa
    def apresentar(self):
        return (f"\nMeu nome é {self.__nome} e eu tenho {self.__idade} anos.")

# Class 2 
class Aluno:
    def __init__(self, curso):
        self.curso = curso  # Não encapsulado

    # Getter para 'curso'
    def get_curso(self):
        return self.curso

    # Setter para 'curso'
    def set_curso(self, curso):
        self.curso = curso

    # Mostrar o curso do aluno
    def estudar(self):
        return f"Estou estudando {self.curso}."

# Criação de objetos com entradas do usuário
nome_input = input("Digite o nome: ")  # Input 1
idade_input = int(input("\nDigite a idade: "))  # Input 2

pessoa1 = Pessoa(nome_input, idade_input)
aluno1 = Aluno("Desenvolvimento de Sistemas")

# Usando variações de métodos e atributos
pessoa1.set_idade(idade_input)  # Alterando a idade
aluno1.set_curso("Engenharia de Software")  # Alterando o curso

print(pessoa1.apresentar())
print(aluno1.estudar())

print("\nPerguntunhas do allan 😎")
print("\nPipeline é: um processo de contrução automatizado para testar, construir e implementar o sistema de forma eficiente e repetitiva.")
print("\nRequitos funcionais são aqueles que o cliente utiliza, como: Login e Registrar-se ")
print("Requitos não funcionais são aqueles que ficam por trás da plataforma, como: Desempenho e Segurança")
print("\nOs pilares do modelo cascata são: Requisitos, Projeto, Implementação,Teste, Implantação, Manutenção")