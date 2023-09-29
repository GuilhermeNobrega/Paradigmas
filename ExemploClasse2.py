from time import sleep
class Equipamento:
  def __init__(self,nome,id):
    self.nome = nome
    self.id = id
  def welcome(self):
    salve_name = float(input(f"Digite o valor do equipamento: {self.nome}:"))
    #salve_id = int(input(f"Digite o novo valor de ID do equipamento: {self.id}"))
    print("====================...PROCESSANDO...======================")
    sleep(1)
    #return f"Equipamento {self.nome} com preço: R${salve_name} || ID_novo: {salve_id} || ID_velho:{self.id}"
    return f"Equipamento {self.nome} com preço: R${salve_name} || ID: {self.id} ||"
if __name__ == "__main__":

  nome = str(input("Digites o nome do equipamento: "))
  id = int(input("Digite o ID do equipamento: "))  
  teste1 = Equipamento(nome,id)
  mensagem = teste1.welcome()
  print(mensagem)
