class Nome:
    ano_atual = 2003
    def __init__(self,nome,idade,ano):
        self.nome = nome
        self.idade = idade
        self.ano = ano

    def get_nome(self):
        return self.nome
    def __str__(self):
        ano_atual = 2022
        return f"Nome: {self.nome}, Ano: {ano_atual - self.idade} e Idade:{self.idade}"
        #print(f"Nome: {self.nome} e Idade:{self.idade} ")
    
    def get_ano_nasc(self):
        return f"shesh {self.ano}"

    def set_nome(self,novo_nome):
        self.nome = novo_nome
        return f"Nome do Participante<{self.nome}. Idade: {self.idade}"

primeiro = Nome("Guilherme",19, 19)
print(primeiro)
anos = primeiro.get_ano_nasc()
print(anos)
name = primeiro.get_nome()
print(name)
primeiro.set_nome("NAJA")
print(primeiro)
