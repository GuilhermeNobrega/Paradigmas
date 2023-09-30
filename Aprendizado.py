from time import sleep

salarios_por_area = {
    "Segurança de Rede": 95000,
    "Segurança de Sistemas Operacionais": 100000,
    "Criptografia": 105000,
    "Pentester": 110000,
    "Computação Forense": 115000
}

experiencia_por_area = {
    "Segurança de Rede": {
        "Junior": "0-2 anos de experiência",
    },
    "Segurança de Sistemas Operacionais": {
        "Junior": "0-2 anos de experiência",
    },
    "Criptografia": {
        "Junior": "0-2 anos de experiência",
    },
    "Pentester": {
        "Junior": "0-2 anos de experiência em segurança cibernética",
    },
    "Computação Forense": {
        "Junior": "0-2 anos de experiência em investigações digitais",
    }
}

class AreasSeguranca:
    def __init__(self):
        self.area = None

    def get_apresentacao_areas(self):
        print("*================= ÁREAS DE SEGURANÇA CIBERNÉTICA ===============*\n")
        sleep(2)
        print(salarios_por_area)
        print('\n')
        response = input("Dessas áreas apresentadas acima, qual você gostaria de se especializar?: ")
        if response in salarios_por_area:
            self.area = response
            salario = salarios_por_area[response]
            print(f"A média salarial para {response} é de ${salario}.")
            return f"Área escolhida foi {response} com R$ {salario} salarial"

    def analise_experiencia(self):
        if self.area is not None:
            print(f"\nVocê escolheu se especializar em {self.area}.")
            experiencia_area = experiencia_por_area.get(self.area, {}).get("Junior")
            print(f"Experiência necessária para {self.area}: {experiencia_area}")

areas_seguranca = AreasSeguranca()
info_experiencia = areas_seguranca.get_apresentacao_areas()
print(info_experiencia)
areas_seguranca.analise_experiencia()
#-------------------------------- old---------------------------------------------
from time import sleep
salarios_por_area = {
    "Segurança de Rede": 95000,
    "Segurança de Sistemas Operacionais": 100000,
    "Criptografia": 105000,
    "Pentester": 110000,
    "Computação Forense": 115000
}
experiencia_por_area = {
    "Segurança de Rede": {
        "Junior": "0-2 anos de experiência",
    },
    "Segurança de Sistemas Operacionais": {
        "Junior": "0-2 anos de experiência",
    },
    "Criptografia": {
        "Junior": "0-2 anos de experiência",
    },
    "Pentester": {
        "Junior": "0-2 anos de experiência em segurança cibernética",
    },
    "Computação Forense": {
        "Junior": "0-2 anos de experiência em investigações digitais",
    }
}
class ÁreasSegurança:
  def __init__(self,area,salario):
    self.area = area
    self.salario = salario
  def get_apresentacao_areas(self):
    print("*================= ÁREAS DE SEGURANÇA CIBERNÉTICA ===============*\n")
    sleep(2)
    print(salarios_por_area)
    print('\n')
    response = str(input("Dessas áreas apresentadas acima, qual você gostaria de se especializar?:"))
    if response in salarios_por_area:
      receber = salarios_por_area[response]
      self.area = response
      print(f"A média salarial para {response} é de ${receber}.")
    return f"Área escolhida foi {response} com R$ {receber} salarial"

  def analise_experiencia(self):
    print("\n")
    print(f"\nVocê escolheu se especializar em {self.area}.")
    experiencia_area = experiencia_por_area[self.area]
    print(f"Experiência necessária para {self.area}: {experiencia_area}")

teste = Áreas_Segurança('','')
variavel = teste.get_apresentacao_areas()
print(variavel)
variavel1 = teste.analise_experiencia()
print(variavel1)
