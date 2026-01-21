# SAIL - Sistema de Agrupamento e Identificação de Lixo
class Lixo():
    def __init__(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome
    
    def categoria(self):
        return 'Desconhecida.'
    
    def descricao_descarte(self):
        return 'Descrição não definida.'
    
class Reciclavel(Lixo):
    def categoria(self):
        return 'Reciclável.'
    
    def descricao_descarte(self):
        return 'Deve ser devidamente lavado. Procure uma de nossas lixeiras inteligentes para descartá-lo corretamente.'
    
class Organico(Lixo):
    def categoria(Lixo):
        return 'Orgânico.'
    
    def descricao_descarte(self):
        return 'Deve ser descartado em lixeiras específicas ou compostado. Não misture com outros tipos de lixo.'
    
class Residuos(Lixo):
    def categoria(self):
        return 'Resíduos.'
    
    def descricao_descarte(self):
        return 'Pode ser descartado no lixo comum. Evite misturar com outros tipos de lixo'
    
class Eletronicos(Lixo):
    def categoria(self):
        return 'Eletrônicos.'
    
    def descricao_descarte(self):
        return 'Não deve ser descartado no lixo comum. Vá à uma lixeira inteligente para o descarte adequado.'
    



    

    
