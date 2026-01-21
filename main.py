class Lixo():
    def __init__(self, tipo, categoria):
       self.tipo = tipo
       self.categoria = categoria
       self.lista_lixo = []

    def mostrar_lixo_categoria(self, tipo, categoria):
        

    def listagem(self, lista_lixo):
        item = input('Adicione os itens que vão ser jogados fora: ')
        lista_lixo.append(item)
        return lista_lixo
    
class Reciclavel(Lixo):
    def __init__(self, tipo, categoria):
        super().__init__(tipo, categoria)

    def

    