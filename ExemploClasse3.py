class Pedido:
  def __init__(self,pedido,extra,acucar):
    self.pedido = pedido
    self.extra = extra
    self.acucar = acucar
  def receber(self):
    pedido = str(input("O que você deseja?"))
    if pedido =='cafe' or pedido=='Cafe':
      extra = str(input("O que deseja para por de extra no seu café?"))
      print(f"Pedido anotado: {pedido} com {extra}")
    else:
      extra = str(input(f"O que deseja para por de extra no seu {pedido}?"))
      print(f"Ok! Pedido anotado {pedido} com {extra}")
    return f"Vish maria rodouu?"
if __name__=="__main__":
  print("Vamos começar a funcionar...")
  pedido1 = Pedido('','','')
  envio = pedido1.receber()
  print(envio)

#------------------------------ Outro método também----------------------------------------
class Pedido:
    def __init__(self):
        self.pedido = ''
        self.extra = ''
        self.acucar = ''

    def receber(self):
        self.pedido = input("O que você deseja?")
        if self.pedido.lower() == 'cafe':
            self.extra = input("O que deseja adicionar como extra no seu café?")
        else:
            self.extra = input(f"O que deseja adicionar como extra no seu {self.pedido}?")
        print(f"Pedido anotado: {self.pedido} com {self.extra}")

if __name__ == "__main__":
    print("Vamos começar a funcionar...")
    pedido1 = Pedido()
    pedido1.receber()
