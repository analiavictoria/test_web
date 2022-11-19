class Automovel:
    def __init__(self,placa="ABC-123",cor="Rosa", marca="New beetle"):
        #atributo da classe
        self.placa = placa
        self.cor = cor
        self.marca = marca

carroDaLia = Automovel()
print(carroDaLia.placa)
print(carroDaLia.cor)
print(carroDaLia.marca)

print(Automovel())