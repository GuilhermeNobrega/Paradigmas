class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
        #print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos")

if __name__ == "__main__":
  # Criando uma instância da classe Pessoa
  pessoa1 = Pessoa("Vini", 20)
  pessoa2 = Pessoa("Guima",20)

  # Acessando os atributos da instância
  #print(pessoa1.nome) #João
  #print(pessoa1.idade) #30
  #print(pessoa2.nome) #Guima
  #print(pessoa2.idade) #20

  # Chamando um método da instância
  mensagem_de_cumprimento = pessoa1.cumprimentar()
  print(mensagem_de_cumprimento)
  mensagem_de_cumprimento2 = pessoa2.cumprimentar()
  print(mensagem_de_cumprimento2)
