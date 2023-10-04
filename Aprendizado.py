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
         "Analista de Segurança": "2-4 anos de experiência",
        "Engenheiro de Segurança": "5+ anos de experiência",
    },
    "Segurança de Sistemas Operacionais": {
        "Junior": "0-2 anos de experiência",
         "Analista de Sistemas": "0-2 anos de experiência",
        "Especialista em Linux": "3-5 anos de experiência",
    },
    "Criptografia": {
        "Junior": "0-2 anos de experiência",
    },
    "Pentester": {
        "Junior": "0-2 anos de experiência em segurança cibernética (Pentester-junior)",
        "Sênior":"Requer 3-5 anos de experiência em segurança cibernética.",
    },
    "Computação Forense": {
        "Junior": "0-2 anos de experiência em investigações digitais",
        "Analista Forense Junior": "0-2 anos de experiência em investigações digitais",
        "Investigador Digital Sênior": "3-5 anos de experiência em investigações digitais",
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
class ExperienciaCargo(AreasSeguranca):
    def __init__(self):
        super().__init__()
        self.cargo = None

    def escolher_cargo(self):
        if self.area is not None:
            print(f"Você escolheu se especializar em {self.area}.")
            experiencia_area = experiencia_por_area.get(self.area, {}).get("Junior")
            print(f"Experiência necessária para {self.area}: {experiencia_area}")
            response = input(f"Qual cargo de {self.area} você deseja? ")
            self.cargo = response

    def mostrar_info_cargo(self):
        if self.cargo is not None:
            salario = salarios_por_area.get(self.area)
            print(f"Você escolheu o cargo de {self.cargo} em {self.area}.")
            print(f"A média salarial para {self.area} é de ${salario}.")

    def verificar_experiencia_usuario(self):
        if self.area is not None and self.cargo is not None:
            experiencia_necessaria = experiencia_por_area.get(self.area, {}).get(self.cargo)
            if experiencia_necessaria:
                print(f"Experiência necessária para o cargo de {self.cargo} em {self.area}: {experiencia_necessaria}")
            else:
                print(f"Não foi encontrada informação de experiência para o cargo de {self.cargo} em {self.area}.")

if __name__ == '__main__':
    experiencia_cargo = ExperienciaCargo()
    info_experiencia = experiencia_cargo.get_apresentacao_areas()
    print(info_experiencia)
    experiencia_cargo.analise_experiencia()
    experiencia_cargo.escolher_cargo()
    experiencia_cargo.mostrar_info_cargo()
    experiencia_cargo.verificar_experiencia_usuario()
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
  def __init__(self):
    self.area = None
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
    if self.area is not None:
      print(f"\nVocê escolheu se especializar em {self.area}.")
      experiencia_area = experiencia_por_area.get(self.area, {}).get("Junior")
      print(f"Experiência necessária para {self.area}: {experiencia_area}")


teste = ÁreasSegurança()
variavel = teste.get_apresentacao_areas()
print(variavel)
variavel1 = teste.analise_experiencia()
print(variavel1)
